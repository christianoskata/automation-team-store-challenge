from rest_framework import routers

from dafiti_challenge.core import api_views

router = routers.DefaultRouter()
router.register(r'shoes', api_views.ShoesViewSet)
