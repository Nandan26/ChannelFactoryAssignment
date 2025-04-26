from rest_framework import serializers

class LocationInpSerializer(serializers.Serializer):
    origin = serializers.CharField()
    destination = serializers.CharField()
