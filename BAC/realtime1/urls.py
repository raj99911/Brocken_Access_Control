from django.urls import path
from .views import IntrusionLogListView

urlpatterns = [
    path('api/intrusions/', IntrusionLogListView.as_view(), name='intrusion-list'),
]
