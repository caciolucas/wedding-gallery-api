from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from core.serializers import PictureSerializer
from core.models import Picture


class PictureViewSet(ModelViewSet):
    serializer_class = PictureSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Picture.objects.all()
        return Picture.objects.filter(approved=True)

    def partial_update(self, request, *args, **kwargs):
        if 'approved' in request.data and not request.user.is_authenticated:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        return super().partial_update(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        if 'approved' in request.data and not request.user.is_authenticated:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        return super().update(request, *args, **kwargs)