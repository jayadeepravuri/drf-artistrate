

from rest_framework import generics
from .models import Geolocation
from .serializers import GeolocationSerializer

class GeolocationList(generics.ListCreateAPIView):
   
    queryset = Geolocation.objects.all()
    serializer_class = GeolocationSerializer


class GeolocationDetail(generics.RetrieveUpdateDestroyAPIView):
  
    queryset = Geolocation.objects.all()
    serializer_class = GeolocationSerializer