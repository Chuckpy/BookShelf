from .consumers import NotificationConsumer

from django.urls import re_path

websocket_urlpatterns = [
    re_path('stories/notification_testing/',NotificationConsumer.as_asgi()),
]
