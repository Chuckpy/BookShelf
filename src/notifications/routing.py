from .consumers import NotificationConsumer

from django.urls import re_path

websocket_urlpatterns = [
    re_path('client_id/notifications/',NotificationConsumer.as_asgi()),
]
