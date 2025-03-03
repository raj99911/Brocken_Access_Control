from rest_framework import permissions
import  logging
logger = logging.getLogger()
class AdminOnlyAccess(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated or not request.user.is_staff:
            self.log_unauthorized_access(request)
            return False
        return True

    def log_unauthorized_access(self, request):
        user = request.user if request.user.is_authenticated else "Anonymous"
        logger.warning(f"Unauthorized access attempt: {user} to {request.path}")
