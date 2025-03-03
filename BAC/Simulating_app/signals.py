from django.contrib.auth.signals import user_login_failed
from django.utils.timezone import now
import logging

logger = logging.getLogger(__name__)

print("lala")
def login_failed_handler(sender, credentials, request, **kwargs):
    logger.warning(
        f"Failed login attempt for {credentials.get('username', 'unknown')} from {request.META.get('REMOTE_ADDR')}")


user_login_failed.connect(login_failed_handler)
