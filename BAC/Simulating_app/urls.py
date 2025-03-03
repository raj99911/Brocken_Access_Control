from django.urls import path

from .views import AdminView

urlpatterns = [
    path('BAC/',AdminView.as_view(),name="bac")
]