from django.conf.urls import url
from rest_framework import routers

from dafiti_challenge.core import api_views

app_name = 'dafiti_challenge.core'

urlpatterns = [
    url('shoes/csv/$', api_views.ShoesUploadAPIView.as_view())
]

router = routers.DefaultRouter()
router.register(r'shoes', api_views.ShoesViewSet)
