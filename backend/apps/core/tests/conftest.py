import pytest
from django.core.files.uploadedfile import InMemoryUploadedFile
from rest_framework.test import APIClient

from apps.core.serializers import ShoesSerializer


@pytest.fixture
def shoe_data():
    data = {
        'name': 'Tenis Bolado',
        'brand': 'Nide',
        'ref': '1232312121',
        'material': 'Pano',
        'color': 'Preto',
        'description': '',
        'size': 42,
        'quantity': 10,
        'weight': 1.0,
        'net_price': '150.00',
        'tax': '20.00'
    }
    return data


@pytest.fixture()
def csv_file():
    file_bin = open("apps/core/tests/shoes.csv", "rb")
    file = InMemoryUploadedFile(file_bin, 'file', 'shoes.csv', 'application/octet-stream', 569, None)
    data = {'encoding': 'utf-8', 'file': file}
    return data


@pytest.fixture()
def api_client(django_user_model):
    api_client = APIClient()

    return api_client


@pytest.fixture()
def shoe(shoe_data):
    serializer = ShoesSerializer(data=shoe_data)
    serializer.is_valid()
    serializer.save()
    return serializer.data


@pytest.fixture()
def shoes_list(shoe_data):
    for i in range(10):
        serializer = ShoesSerializer(data=shoe_data)
        serializer.is_valid()
        serializer.save()
