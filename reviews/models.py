from django.db import models
from django.conf import settings
from bookings.models import Booking

class Review(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)
    provider = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField()
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
