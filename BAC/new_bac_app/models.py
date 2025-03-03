from django.db import models
from django.contrib.auth.models import User
from simple_history.models import HistoricalRecords

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    history = HistoricalRecords()  # Tracks changes
