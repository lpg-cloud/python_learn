
# chat/consumers.py
from pytz import unicode

from chat.models import clients, models
from channels.layers import get_channel_layer
from Django01.settings import CHANNEL_LAYERS
import json
import channels
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import async_to_sync

import redis

pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)


class ChatConsumer(AsyncWebsocketConsumer):
    room_name = ''
    user_id = ''
    r = redis.Redis(host='localhost', port=6379, decode_responses=True)
    async def connect(self):

        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.user_id = self.scope['url_route']['kwargs']['user_name']
        # 将用户名和用户当前连接名存到redis中的
        self.r.hset('online_users', self.user_id, self.channel_name)
        # Join room group
        await self.channel_layer.group_add(
            self.room_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):

        self.r.hdel('online_users',(self.user_id,))
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

        if message_type == 'user_to_group_message':
            # Send message to room group
            group_id = text_data_json['receiver']
            await self.channel_layer.group_send(
                group_id,
                {
                    'type': 'chat_message',
                    'sender': self.user_id,
                    'message': message
                }
            )
        else:
            receiver_id = text_data_json['receiver']
            receiver_channel_name = self.r.hget('online_users', receiver_id)
            await self.channel_layer.send(receiver_channel_name, {
                'type': 'chat_message',
                'sender': self.user_id,
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

    