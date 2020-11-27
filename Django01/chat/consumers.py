# chat/consumers.py
from chat.models import user
from .models import client, models
from channels.layers import get_channel_layer
from Django01.settings import CHANNEL_LAYERS
import json
import channels
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from django.utils import timezone

#在程序开始时将所有在线成员表清空
client.objects.all().delete()


class ChatConsumer(AsyncWebsocketConsumer):
    room_name = ''
    cur_user = None
    client = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.all_online_user_group = 'all_online_users'

    async def connect(self):

        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.user_id = self.scope['url_route']['kwargs']['user_name']
        self.cur_user = await sync_to_async(user.objects.filter(id=int(self.user_id)).first)()
        self.client = await sync_to_async(client.objects.create)(user_name=self.cur_user, channel_name=self.channel_name,
                                                   login_time=timezone.now())
        # Join room group

        # await self.channel_layer.group_add(
        #     self.room_name,
        #     self.channel_name
        # )
        await self.accept()

    async def disconnect(self, close_code):

        #self.r.hdel('online_users', (self.user_id,))
        result = await sync_to_async(self.client.delete)()
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_name,
            self.channel_name
        )

    # Receive message from WebSocket

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        message_type = text_data_json['message_type']
        print(self.cur_user.name)
        print(message)
        if message_type == 'user_to_group_message':
            # Send message to room group
            group_id = text_data_json['receiver']
            await self.channel_layer.group_send(
                group_id,
                {
                    'type': 'chat_message',
                    'sender': self.cur_user.name,
                    'message': message
                }
            )
        else:
            sender_name = text_data_json['receiver']
            sender = await sync_to_async(user.objects.get)(name=sender_name)
            receiver_client = await sync_to_async(client.objects.filter(user_name=sender).first)()
            await self.channel_layer.send(receiver_client.channel_name, {
                'type': 'chat_message',
                'sender': self.cur_user.name,
                'message': message
            })

    # Receive message from others
    async def chat_message(self, event):
        message = event['message']
        sender = event['sender']
        print(self.channel_name)
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'sender': sender,
            'message': message
        }))
