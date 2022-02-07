from .consumers import NotificationConsumer

from django.urls import re_path

websocket_urlpatterns = [
    re_path('notifications/(?P<client_id>\w+)/$',NotificationConsumer.as_asgi()),
]

