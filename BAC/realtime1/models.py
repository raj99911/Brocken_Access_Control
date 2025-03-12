from django.db import models

class IntrusionLog(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    source_ip = models.GenericIPAddressField()
    destination_ip = models.GenericIPAddressField()
    protocol = models.CharField(max_length=10)
    alert_message = models.TextField()

    def __str__(self):
        return f"{self.timestamp} - {self.source_ip} -> {self.destination_ip} ({self.protocol})"
