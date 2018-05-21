# chat/routing.py
from django.conf.urls import url

from . import consumers2

websocket_urlpatterns = [
    url(r'^ws/chat/(?P<room_name>[^/]+)/$', consumers2.ChatConsumer),
]
