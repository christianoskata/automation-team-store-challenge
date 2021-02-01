import csv
import io

from django.forms import model_to_dict
from rest_framework import viewsets, status, generics
from rest_framework.response import Response

from dafiti_challenge.core.models import Shoes
from dafiti_challenge.core.serializers import ShoesSerializer, ShoesUploadSerializer


class ShoesViewSet(viewsets.ModelViewSet):
    queryset = Shoes.objects.all()
    serializer_class = ShoesSerializer


class ShoesUploadAPIView(generics.CreateAPIView):
    serializer_class = ShoesUploadSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']

        with io.TextIOWrapper(file, encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            headers = next(reader, None)

            response = []
            for row in reader:
                row_data = {}
                for header, value in zip(headers, row):
                    row_data[header] = value

                serializer = ShoesSerializer(data=row_data)
                response.append(row_data)
                serializer.is_valid()
                instance = serializer.save()
                response.append(model_to_dict(instance))

        return Response(status=status.HTTP_201_CREATED, data=response)
