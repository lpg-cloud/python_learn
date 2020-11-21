# # chat/consumers.py
# import json
# from asgiref.sync import async_to_sync
# from channels.generic.websocket import WebsocketConsumer
#
# class ChatConsumer(WebsocketConsumer):
#     def connect(self):
#         self.room_name = self.scope['url_route']['kwargs']['room_name']
#         self.room_group_name = 'chat_%s' % self.room_name
#
#         # Join room group
#         async_to_sync(self.channel_layer.group_add)(
#             self.room_group_name,
#             self.channel_name
#         )
#
#         self.accept()
#
#     def disconnect(self, close_code):
#         # Leave room group
#         async_to_sync(self.channel_layer.group_discard)(
#             self.room_group_name,
#             self.channel_name
#         )
#
#     # Receive message from WebSocket
#     def receive(self, text_data):
#         text_data_json = json.loads(text_data)
#         message = text_data_json['message']
#
#         # Send message to room group
#         async_to_sync(self.channel_layer.group_send)(
#             self.room_group_name,
#             {
#                 'type': 'chat_message',
#                 'message': message
#             }
#         )
#
#     # Receive message from room group
#     def chat_message(self, event):
#         message = event['message']
#
#         # Send message to WebSocket
#         self.send(text_data=json.dumps({
#             'message': message
#         }))

# chat/consumers.py
from .models import user
from .models import clients, models
from channels.layers import get_channel_layer
from Django01.settings import CHANNEL_LAYERS
import json
import channels
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from django.utils import timezone


class ChatConsumer(AsyncWebsocketConsumer):
    room_name = ''
    user_id = ''

    async def connect(self):

        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.user_id = self.scope['url_route']['kwargs']['user_name']
        cur_user =await sync_to_async(user.objects.filter)(id=int(self.user_id))

        print(self.user_id)
        print(self.room_name)
        await sync_to_async(clients.objects.create)(user_name=cur_user.id,channel_name=self.channel_name,login_time=timezone.now())
        self.all_online_user_group='all_online_users'
        # Join room group
        
        # await self.channel_layer.group_add(
        #     self.room_name,
        #     self.channel_name
        # )
        await self.accept()

    async def disconnect(self, close_code):
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
            user_id = text_data_json['receiver']
            print(self.channel_name)
            print(user_id)
            await self.channel_layer.send(user_id, {
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

    