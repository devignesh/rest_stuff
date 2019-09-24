from rest_framework import serializers


class TokenSerializer(serializers.Serializer):
    token = serializers.CharField()


class RefreshSerializer(serializers.Serializer):
    token = serializers.CharField()
    