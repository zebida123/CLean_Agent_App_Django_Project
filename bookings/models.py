from django.db import models
from django.conf import settings
from services.models import Service

class Booking(models.Model):
    STATUS_CHOICES = (
        ('pending','Pending'),
        ('accepted','Accepted'),
        ('in_progress','In Progress'),
        ('completed','Completed'),
        ('cancelled','Cancelled'),
    )
    client = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='client_bookings', on_delete=models.CASCADE)
    provider = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='provider_bookings', null=True, blank=True, on_delete=models.SET_NULL)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    scheduled_at = models.DateTimeField()
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
