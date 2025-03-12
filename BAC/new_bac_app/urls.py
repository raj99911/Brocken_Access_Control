# from django.urls import path
# from .views import CustomTokenObtainPairView
# from rest_framework.throttling import UserRateThrottle
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,  # For login (get access + refresh token)
#     TokenRefreshView,      # To refresh expired access tokens
# )
# from .views import AdminView
#
# urlpatterns = [
#     path('',AdminView.as_view(),name="bac"),
#     path("api/token/", CustomTokenObtainPairView.as_view(throttle_classes = [UserRateThrottle]), name="token_obtain_pair"),  # Login
#     path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),  # Refresh token
#
# ]
#new
from django.urls import path
from .views import BruteForceScannerAPIView

urlpatterns = [
    path('api/scan-brute-force/', BruteForceScannerAPIView.as_view(), name='brute_force_scan'),
]

