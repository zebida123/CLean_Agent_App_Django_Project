import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        user = self.scope.get('user')
        if user is None or user.is_anonymous:
            await self.close()
            return
        self.room_name = f'chat_{user.id}'
        await self.channel_layer.group_add(self.room_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data.get('message')
        await self.channel_layer.group_send(self.room_name, {
            'type': 'chat.message',
            'message': message,
        })

    async def chat_message(self, event):
        await self.send(text_data=json.dumps({'message': event['message']}))
