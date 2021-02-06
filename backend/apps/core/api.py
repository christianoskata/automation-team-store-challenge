from rest_framework import routers

# Settings
from .api_views import ShoesViewSet

api = routers.DefaultRouter()
api.trailing_slash = '/?'

# Users API
api.register(r'shoes', ShoesViewSet)
