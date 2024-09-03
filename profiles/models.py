from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=75, blank=True)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)
    location = models.CharField(max_length=100, blank=True)
    wallet_address = models.CharField(max_length=255, blank=True)
    verified_creator = models.BooleanField(default=False)
    blockchain_platform = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.owner}'s profile"

def create_profile(sender, instance, created, **kwargs):
    """
    Signal handler function to create a user profile when a new user is created
    """
    if created:
        Profile.objects.create(owner=instance)

post_save.connect(create_profile, sender=User)
