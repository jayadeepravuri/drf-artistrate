from django.db import models
from django.contrib.auth.models import User


class Geolocation(models.Model):

    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    display_name = models.CharField(max_length=75, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)


    def __str__(self):
        return self.display_name
