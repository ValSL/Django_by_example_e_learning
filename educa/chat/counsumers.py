import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import async_to_sync
from django.utils import timezone


class ChatConsumer(AsyncWebsocketConsumer):
    """
        Отправка сообщений самому себе в функции receive
    """

    async def connect(self):
        self.user = self.scope["user"]
        # Every consumer has a scope with information about its connection, arguments passed by the URL, and the authenticated user, if any.
        self.id = self.scope["url_route"]["kwargs"]["course_id"]
        # Build the group name with the id of the course that the group corresponds to.
        self.room_group_name = "chat_%s" % self.id
        # join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        # accept connection
        await self.accept()

    async def disconnect(self, close_code):
        # leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        now = timezone.now()
        # send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat_message",
                "message": message,
                "user": self.user.username,
                "datetime": now.isoformat(),
            },
        )

    # receive message from room group
    async def chat_message(self, event):
        # Send message to WebSocket
        await self.send(text_data=json.dumps(event))
