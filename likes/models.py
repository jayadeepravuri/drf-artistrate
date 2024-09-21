from django.db import models
from django.contrib.auth.models import User
from arts.models import Art


class Like(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    art = models.ForeignKey(
        Art, related_name='likes', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'art']

    def __str__(self):
        return f'{self.owner} {self.art}'