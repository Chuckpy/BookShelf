from .consumers import ChatConsumer

from django.urls import re_path

websocket_urlpatterns = [
    re_path('^ws/$', ChatConsumer.as_asgi()),
]
