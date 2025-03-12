
import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from BAC.realtime import routing


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BAC.settings')
django_app = get_asgi_application()
application = ProtocolTypeRouter({
    "http": django_app,
    "websocket": URLRouter(routing.websocket_urlpatterns),
})
