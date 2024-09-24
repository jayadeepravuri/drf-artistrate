from django.db import models
from django.contrib.auth.models import User
from geolocation.models import Geolocation


class Art(models.Model):
    
    categories = [
        ('generative-art', 'Generative Art'),
        ('digital-illustrations-and-paintings', 'Digital Illustrations and Paintings'),
        ('pixel-art', 'Pixel Art'),
        ('3d-artwork', '3D Artwork'),
        ('photography', 'Photography'),
        ('augmented-reality-art', 'Augmented Reality Art'),
        ('collage-art', 'Collage Art'),
        ('interactive-art', 'Interactive Art'),
        ('music-and-audio-art', 'Music and Audio Art'),
        ('ai-generated-art', 'AI-Generated Art'),
        ('fine-art-nfts', 'Fine Art NFTs'),
        ('other', 'Other'),
                  ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    category = models.CharField(
        max_length=250,
        blank=True,
        null=True,
        default=None,
        choices=categories
    )
    image = models.ImageField(
        upload_to='images/', default='../default_art_image_axpg76', blank=True
    )
    tagged_user = models.ForeignKey( User,on_delete=models.CASCADE, related_name='tagged_user',
        blank=True,
        null=True,
        default=None
    )
    geolocation = models.ForeignKey(
        Geolocation,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )


    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'