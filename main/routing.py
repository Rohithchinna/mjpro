# routing.py
from django.urls import re_path
from .consumer import *
from notifications.consumer import *

websocket_urlpatterns = [
    #path("ws/notifications/", NotificationConsumer.as_asgi()),
    #re_path(r'ws/main/networks/(?P<receiver_email>[\w.@+-]+)/$', NetworkConsumer.as_asgi()),
    re_path(r'ws/notifications/(?P<receiver_email>[\w.@+-]+)/$', NotificationConsumer.as_asgi()),

]