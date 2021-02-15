from django.forms import model_to_dict
from rest_framework import filters
from rest_framework import viewsets, status, generics
from rest_framework.response import Response

from .models import Shoes
from .serializers import ShoesSerializer, ShoesUploadSerializer


class ShoesViewSet(viewsets.ModelViewSet):
    queryset = Shoes.objects.all()
    serializer_class = ShoesSerializer
    search_fields = ['name', 'brand']
    filter_backends = (filters.SearchFilter,)


class ShoesUploadAPIView(generics.CreateAPIView):
    serializer_class = ShoesUploadSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']

        content = ShoesUploadSerializer.handler_csv(file)

        response = []
        for row_data in content:
            exists = Shoes.objects.filter(**row_data).exists()
            if exists:
                continue

            serializer = ShoesSerializer(data=row_data)
            serializer.is_valid()
            instance = serializer.save()
            response.append(model_to_dict(instance))

        return Response(status=status.HTTP_201_CREATED, data=response)
