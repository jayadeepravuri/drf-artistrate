from rest_framework import serializers
from .models import Geolocation

class GeolocationSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Geolocation
        fields = [
            'id',
            'owner',
            'display_name',
            'latitude',
            'longitude',
            'city',
            'country',
        ]

    def __str__(self):
        return self.name