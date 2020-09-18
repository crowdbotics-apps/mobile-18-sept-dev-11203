from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import BngvnbvnbViewSet

router = DefaultRouter()
router.register("bngvnbvnb", BngvnbvnbViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
