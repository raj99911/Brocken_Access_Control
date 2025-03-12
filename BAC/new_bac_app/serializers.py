from rest_framework import serializers
from django.core.validators import validate_ipv46_address

class BruteForceScanSerializer(serializers.Serializer):
    url = serializers.URLField(required=True)
    ip = serializers.CharField(
        required=False,
        allow_blank=True,
        validators=[validate_ipv46_address]
    )
    method = serializers.ChoiceField(choices=['GET', 'POST'], default='POST')
    username_param = serializers.CharField(required=False, default="username")
    password_param = serializers.CharField(required=False, default="password")
    username_value = serializers.CharField(required=True)
    password_list = serializers.ListField(child=serializers.CharField(), required=True)
    max_attempts = serializers.IntegerField(default=5)
