from django.core.cache import cache
from django.http import JsonResponse
from django.core.mail import send_mail
from django.utils.timezone import now
import logging

logger = logging.getLogger(__name__)

class BlockUnauthorizedUsersMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip = request.META.get('REMOTE_ADDR')

        # Check if the IP is already blocked
        if cache.get(f"blocked_{ip}"):
            logger.warning(f"Blocked access attempt from {ip}")
            return JsonResponse({"error": "Too many unauthorized attempts. Try later."}, status=403)

        response = self.get_response(request)

        # If unauthorized access detected (401), track attempts
        if response.status_code == 401:
            attempts = cache.get(f"attempts_{ip}", 0) + 1
            cache.set(f"attempts_{ip}", attempts, timeout=600)  # Store for 10 minutes

            if attempts >= 5:
                cache.set(f"blocked_{ip}", True, timeout=1800)  # Block for 30 minutes
                logger.warning(f"IP {ip} temporarily blocked due to excessive unauthorized access.")
                alert_admin_on_intrusion(ip, request.path)

        return response


def alert_admin_on_intrusion(ip, path):
    subject = " Intrusion Alert: Unauthorized Access Attempt "
    message = f"Time: {now()}\nIP Address: {ip}\nAttempted Access: {path}"
    send_mail(subject, message, 'devtestusr02@gmail.com', ['rohn2100@gmail.com'])
    logger.warning(f"Admin alerted: {message}")

