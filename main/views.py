from django.shortcuts import render
from mjpro.templates import *
from django.shortcuts import redirect
from .models import *
from .globals import uservar
from django.core.cache import cache
import json
from notifications.views import add_to_notifications
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from activity.models import *
from profiles.models import *
from datetime import datetime
from addPosts.models import myPosts
# Create your views here.
@login_required
def home(request):
    ss=myPosts.objects.prefetch_related('likes').all()
    print(ss,request.user)
    sug=User.objects.all()
    context={'ss':ss,'sug':sug}
    return render(request,"home.html",context)
@login_required
def signout(request):
    print(request.user)
    x=profiles.objects.filter(is_online=True).count()
    Activity(profile=request.user,activity="signout",activity_desc=f"You have been Signed Out at {datetime.now()}",count=x).save()
    x=profiles.objects.get(user_name=request.user)
    x.is_online=False
    x.save()
    logout(request)
    return redirect("homepage")
'''def chats(request):
    return render(request,"chats.html")'''
@login_required
def networks(request):
    print(request.user)
    z=cache.get('uservar')
    #add user to networks
    try:
        x = Networks.objects.get(current_user=request.user)
        print("try")
    except:
        x = Networks(current_user=request.user, network_users=json.dumps([]))  # Initialize with an empty JSON array
        x.save()  # Save the new instance
    
    #suggestions
    suggestedusers=[]
    netw=[]
    netw2=[]
    global uservar
    y=[]
    print(z)
    try:
        networkuser=Networks.objects.get(current_user=request.user)
        y=networkuser.get_items()
    except:
        pass
    
    
    listOfUsers=Users.objects.all()
    print(request.user,uservar)
    x=str(request.user)
    for i in listOfUsers:
        if i not in y:

            print(request.user==str(i.email))
            if(request.user==i.email or i.email in json.loads(Networks.objects.get(current_user=request.user).network_users)):
                continue
            else:
                suggestedusers.append(i)
    try:
        for i in json.loads(Networks.objects.get(current_user=request.user).network_users):
            if(len(netw)>len(netw2)):
                netw2.append(i)
            else:
                netw.append(i)
            print(i)
    except:
        netw=[]
    return render(request,"networks.html",{"suggestedusers":suggestedusers,"netw":netw,"netw2":netw2})
@login_required
def addfriend(request,username):
    print("in addfriend")
    #z = cache.get('uservar')  # Assuming 'uservar' is stored in the cache
    print(username,request.user)
    #if z is None:
    #    return render(request, "networks.html", {'error': 'User  not found in cache.'})
    add_to_notifications(request.user,username,"add_friend")
    # Check if a Networks instance already exists for the current user
    '''try:
        x = Networks.objects.get(current_user=z)
        # If it exists, add the new friend
        x.add_item(username)
    except Networks.DoesNotExist:
        # If it does not exist, create a new instance with the default network_users
        x = Networks(current_user=z, network_users=json.dumps([]))  # Initialize with an empty JSON array
        x.save()  # Save the new instance
        x.add_item(username)  # Now add the new friend'''
    print("in addfriend 2")
    return redirect('networks')
    


