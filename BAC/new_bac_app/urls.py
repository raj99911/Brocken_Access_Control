from django.urls import path
from rest_framework.throttling import UserRateThrottle
from rest_framework_simplejwt.views import (
    TokenObtainPairView,  # For login (get access + refresh token)
    TokenRefreshView,      # To refresh expired access tokens
)
from .views import AdminView

urlpatterns = [
    path('',AdminView.as_view(),name="bac"),
    path("api/token/", TokenObtainPairView.as_view(throttle_classes = [UserRateThrottle]), name="token_obtain_pair"),  # Login
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),  # Refresh token

]