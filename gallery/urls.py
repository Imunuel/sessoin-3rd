from django.urls import path
from .views import ExhibitionsViewSet
from rest_framework import routers



router = routers.SimpleRouter()
router.register(r'exhibitions', ExhibitionsViewSet)

urlpatterns = router.urls





