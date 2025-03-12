from rest_framework.response import Response
from rest_framework.views import APIView
from .models import IntrusionLog
from .serializers import IntrusionLogSerializer

class IntrusionLogListView(APIView):
    def get(self, request):
        logs = IntrusionLog.objects.all().order_by('-timestamp')[:50]  # Fetch latest 50 logs
        serializer = IntrusionLogSerializer(logs, many=True)
        return Response(serializer.data)
