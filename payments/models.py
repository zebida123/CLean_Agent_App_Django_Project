from django.db import models
from django.conf import settings

class Transaction(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    mpesa_receipt = models.CharField(max_length=200, blank=True, null=True)
    status = models.CharField(max_length=30, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
