from django.urls import path
from django.conf.urls import include
from rest_framework.routers import DefaultRouter

from core.views import PictureViewSet

router = DefaultRouter()

router.register(r'pictures', PictureViewSet, basename='picture')
urlpatterns = [
    path("", include(router.urls)),
]
