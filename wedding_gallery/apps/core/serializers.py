from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers

from core.models import Picture


class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = '__all__'

    def create(self, validated_data):
        # If the user is authenticated, set approved to True
        if self.context['request'].user.is_authenticated:
            validated_data['approved'] = True
        else:
            validated_data['approved'] = False
        return super().create(validated_data)
