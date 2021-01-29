from rest_framework import viewsets

from dafiti_challenge.core.models import Shoes
from dafiti_challenge.core.serializers import ShoesSerializer


class ShoesViewSet(viewsets.ModelViewSet):
    queryset = Shoes.objects.all()
    serializer_class = ShoesSerializer
