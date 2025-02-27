import json
from django.shortcuts import redirect
from django.core.cache import cache
from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from notifications.models import Notification

class NotificationConsumer(AsyncWebsocketConsumer):
    #consumer_user=cache.get('uservar')
    #get_instance_receiver=Users.objects.get(email=receiver)
    async def connect(self):
        #from main.models import Users
        print('in connect')
        self.x= self.scope['url_route']['kwargs']['receiver_email']
        self.x=self.x.replace('@','_')
        self.channel_name=self.x
        self.group_name = f'chat_{self.channel_name}'
        print(self.channel_name,self.group_name)
        # Join the user's group
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()
        print(self.channel_layer,self.group_name)

    async def disconnect(self, close_code):
        print("in disconnect")
        # Leave the group
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    
        
        #self.disconnect()
    #receive from client
    async def receive(self, text_data):
        print("in receive")
        text_data=json.loads(text_data)
        message = text_data['message']
        receiver_email=text_data['receiver_email']
        type=text_data['type']
        print("in receive")
        print(text_data,message,receiver_email,type)
        print(self.channel_name,self.group_name)
        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'send_notification',
                'receiver_email': receiver_email,
                'message':str(receiver_email+message),
                
            }
        
        )
        print(self.channel_layer,self.group_name)
        
        print("in receive")
        #await self.send_notification(json.dumps(text_data))
    async def send_notification(self, event):
        print("in send_notification")
        #type = event['type']
        receiver_email=event['receiver_email']
        message=event['message']
        from main.models import Users
        user=cache.get('uservar')
        get_instance_sender=await sync_to_async(Users.objects.get)(email=user)
        get_instance_receiver=await sync_to_async(Users.objects.get)(email=receiver_email)
        await sync_to_async(Notification.objects.create)(notif_from_user=get_instance_sender,is_seen=False,notif_content="add_friend",notif_to_user=get_instance_receiver)
        
        # Send to websocket
        await self.send(text_data=json.dumps({
            'type': "add_friend",
            'receiver_email':receiver_email,
            'message':message
        }))
    async def again_send(self,text_data):
        print("in again_send")
        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'send_notification',
                'message':json.loads(text_data)
            }
        )
        
    