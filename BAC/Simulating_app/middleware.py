import logging
from django.http import JsonResponse

logger = logging.getLogger(__name__)

class BrokenAccessControlMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Detect Unauthorized Access (403)
        if response.status_code == 403:
            user = request.user if request.user.is_authenticated else "Anonymous"
            logger.warning(f"Potential BAC attempt: {user} tried accessing {request.path}")

        return response
