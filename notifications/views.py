from django.shortcuts import render,redirect
from django.core.cache import cache
from django.contrib import messages
from .models import Notification
from main.models import Users
from django.contrib.auth.models import User
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.layers import get_channel_layer
from django.contrib.auth.decorators import login_required
from asgiref.sync import async_to_sync
#from .consumer import NotificationConsumer

# Create your views here.
@login_required
def notifications(request):
    current_user=cache.get('uservar')
    if request.user:
        notifications_list={'list':[],'user':request.user}
        get_instance_current_user=Users.objects.get(email=request.user.email)
        x=Notification.objects.filter(notif_to_user=get_instance_current_user)
        for i in x:
            if i.notif_content=="add_friend":
                notifications_list['list'].insert(0,f'{i.notif_from_user} wants to add you to the Network')
        print(notifications_list)
        return render(request,"notifications.html",notifications_list)
    else:
        return render(request,"home.html")


def add_to_notifications(sender,receiver,type):
    print(sender,receiver,"hi")
    get_instance_sender=Users.objects.get(email=sender)
    get_instance_receiver=Users.objects.get(email=receiver)
    x=Notification(notif_from_user=get_instance_sender,is_seen=False,notif_content=type,notif_to_user=get_instance_receiver)
    x.save()
    channel_layer = get_channel_layer()
    dic={'type':type,'sender':sender}
    print("in add_to not")
    #NotificationConsumer.send_notification(self=None,text_data=dic)
    print(async_to_sync(channel_layer.group_send)(
        f"user_{str(receiver).replace("@","_")}",  # Group name
        {
            'type': type,
            'message': "wants to add to the Network",
            'receiver_email':receiver
        }
    ))