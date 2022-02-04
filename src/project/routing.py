import os

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
from conversare.routing import websocket_urlpatterns as conversare_routing
from notifications.routing import websocket_urlpatterns as notifications_routing

absolute_path = conversare_routing + notifications_routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

application = ProtocolTypeRouter({
    
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            absolute_path
        )
    ),
})