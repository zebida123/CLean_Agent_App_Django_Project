from django.db import models
from accounts.models import Agent
from clients.models import Client

class Service(models.Model):
    service_name = models.CharField(max_length=100)
    description = models.TextField()
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_requested = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Pending')

    def __str__(self):
        return f"{self.service_name} - {self.client.name}"
