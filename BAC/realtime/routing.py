from django.urls import path
from .consumers import PacketMonitorConsumer

websocket_urlpatterns = [
    path("ws/packet-monitor/", PacketMonitorConsumer.as_asgi()),
]
