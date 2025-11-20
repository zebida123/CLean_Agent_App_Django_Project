from django.db import models
from django.conf import settings

class ProviderProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    about = models.TextField(blank=True)
    is_verified = models.BooleanField(default=False)
    location = models.CharField(max_length=255, blank=True)
    rating = models.FloatField(default=0)
