from django.urls import path
from rest_framework import routers

from dafiti_challenge.core import api_views

app_name = 'dafiti_challenge.core'

urlpatterns = [
    path('shoes/csv/', api_views.ShoesUploadAPIView.as_view(), name='csv_post'),
]

router = routers.DefaultRouter()
router.register(r'shoes', api_views.ShoesViewSet)
