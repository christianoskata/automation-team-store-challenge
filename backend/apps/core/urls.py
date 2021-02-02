from django.urls import re_path

from apps.core.api_views import ShoesUploadAPIView

app_name = 'core'

urlpatterns = [
    re_path(r'shoes/csv/?', ShoesUploadAPIView.as_view(), name='csv_post'),
]
