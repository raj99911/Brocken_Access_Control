from django.urls import path
from .consumers import PacketMonitorConsumer
from .views import IDSMonitorAPIView

urlpatterns = [
    path("ws/packet-monitor/", IDSMonitorAPIView.as_view()),
]
