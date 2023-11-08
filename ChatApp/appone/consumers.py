import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Receive
from asgiref.sync import sync_to_async


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        uid = data['uid']
        saved_message_id = await self.save_message(message, uid)
        saved_message = await self.get_saved_message(saved_message_id)
        print(saved_message)
        # await self.send(text_data=json.dumps({'message': saved_message}))

    @sync_to_async
    def save_message(self, message, uid):
        obj23 = Receive(msg=message, uid=str(uid))
        obj23.save()
        return obj23.id

    @sync_to_async
    def get_saved_message(self, message_id):
        try:
            saved_message = Receive.objects.get(id=message_id)
            return saved_message
        except Receive.DoesNotExist:
            return None
        
        
