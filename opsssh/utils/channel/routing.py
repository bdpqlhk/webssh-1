from django.conf.urls import url
from opsssh.utils.channel import websocket

websocket_urlpatterns = [
    url('webssh/', websocket.WebSSH),
]