from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .permissions import AdminOnlyAccess


class AdminView(APIView):
    permission_classes = [IsAuthenticated, AdminOnlyAccess]

    def get(self, request):
        return Response({"message": "Welcome, Admin! You have access to this view."})

