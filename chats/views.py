from django.shortcuts import render
from .models import privatechat,Messages
from django.core.cache import cache
from main.models import Users
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

# Create your views here.
current_user=cache.get('uservar')
def chats(request):
    current_user=request.user.email
    list_of_chats=[]
    x=privatechat.objects.all()
    for i in x:
        print(current_user,i.user1,i.user2)
        print(i.user1==current_user)
        print(type(str(i.user1)),type(current_user))
        if str(i.user1)==current_user and i.user2 not in list_of_chats:
            
            list_of_chats.append(i.user2)
        if str(i.user2)==current_user and i.user1 not in list_of_chats:
            list_of_chats.append(i.user1)
    context={}
    print(list_of_chats)
    context['list_of_chats']=list_of_chats
    return render(request,"chats.html",context)
def add_to_Messages(request):
    
    current_user=request.user.email

    
    list_of_chats=[]
    x=privatechat.objects.all()
    
    chat=0
    
    print("hi")
    if request.method=='POST':
        print("hi 1")
        message=request.POST.get('message')
        print("hi 2")
        receiver_user = get_object_or_404(Users, email=request.POST.get('receiver'))
        current_user= get_object_or_404(Users, email=current_user)
        print(receiver_user)
        
        #for main add_to_Messages
        try:
            chat=privatechat.objects.get(user1=current_user,user2=receiver_user)
            print("check add_to_Messages in try 1")
        except privatechat.DoesNotExist:
            try:
                chat=privatechat.objects.get(user1=receiver_user,user2=current_user)
                print("check add_to_Messages in try 2")
            except privatechat.DoesNotExist:
                chat=privatechat.objects.create(user1=current_user,user2=receiver_user)
                print("check add_to_Messages in except")
        sender=current_user
        content=message
        print("check add_to_Messages")
        Messages_save=Messages(chat=chat,sender=sender,content=content)
        Messages_save.save()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'}, status=400)

def past_messages(request,receiver):
    #for past messages
    past_messages={}
    current_user=request.user.email
    print(current_user)
    y=Users.objects.get(email=current_user)
    z=Users.objects.get(email=receiver)
    print(1)
    try:
        x=privatechat.objects.get(user1=z,user2=y)
        print(1)
    except:
        x=privatechat.objects.get(user1=y,user2=z)
        print(1)
    instance_of_msg=Messages.objects.filter(chat=x)
    j=0
    for i in instance_of_msg:
        if str(i.sender)==current_user:
            print('sender')
            past_messages[f'sender{j}']=i.content
            j+=1
        if str(i.sender)==receiver:
            print("receiver")
            past_messages[f'receiver{j}']=i.content
            j+=1
    print(past_messages)
    return JsonResponse(past_messages)