from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .threads import run_sniffer


class IDSMonitorAPIView(APIView):
    def get(self, request):
        run_sniffer()  # Start the sniffer
        return Response({"message": "Packet monitoring started"}, status=status.HTTP_200_OK)
