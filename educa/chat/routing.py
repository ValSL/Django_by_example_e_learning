from django.urls import re_path
from . import counsumers

websocket_urlpatterns = [
    re_path(r'ws/chat/room/(?P<course_id>\d+)/$', counsumers.ChatConsumer),
]

