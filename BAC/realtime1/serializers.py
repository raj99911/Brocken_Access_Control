from rest_framework import serializers
from .models import IntrusionLog

class IntrusionLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = IntrusionLog
        fields = '__all__'
