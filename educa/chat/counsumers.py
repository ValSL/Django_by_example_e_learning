import json
from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    """
        Отправка сообщений самому себе в функции receive
    """
    def connect(self):
        # accept connection
        self.accept()
        text = {'asdasda': 1}
        data = json.lods(text)
        print(data)

    def disconnect(self):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        self.send(text_data=json.dumps({'message': message}))

