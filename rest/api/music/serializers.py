from rest_framework import serializers
from .models import Songs

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Songs
        fields = ("title", "artist")
        

class TokenSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=255)