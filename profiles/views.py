from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib.auth.models import User
import json
from django.http import JsonResponse
from .models import *
import ast
# Create your views here.
@login_required
def profile(request):
    user=request.user
    context={'profilepic':"",
            'firstname':"",
            'middlename':"",
            'lastname':"",
            'username':"",
            'email':"",
            'dob':"",
            'phno':"",
            'interests':"",
            'hobbies':"",
            'skills':"",
            'achievements':"",}
    try:
        pro_user=profiles.objects.get(user_name=user)
        context["username"]=user.username
        context["email"]=user.email
        context["profilepic"]=pro_user.profile_pic
        context["firstname"]=pro_user.first_name
        context["middlename"]=pro_user.middle_name
        context["lastname"]=pro_user.last_name

        basic_instance=basic.objects.get(profile=pro_user)
        context["dob"]=basic_instance.date_of_birth
        context["phno"]=basic_instance.phone_number

        interests_inst=interests.objects.get(profile=pro_user)
        context["interests"]=ast.literal_eval(interests_inst.interests)

        hobbies_inst=hobbies.objects.get(profile=pro_user)
        context["hobbies"]=ast.literal_eval(hobbies_inst.hobbies)

        skills_inst=skills.objects.get(profile=pro_user)
        context["skills"]=ast.literal_eval(skills_inst.skills)

        achievements_inst=achievements.objects.get(profile=pro_user)
        context["achievements"]=ast.literal_eval(achievements_inst.achievements)
    except:
        #pro_user=profiles(user_name=user,email=user.email,is_online=True)
        #pro_user.save()
        context["username"]=user.username
        context["email"]=user.email
        
    return render(request,"profile.html",context)
@login_required
def update_profile_details(request):
    if request.method=="POST":
        firstname=request.POST.get("firstname")
        middlename=request.POST.get('middlename')
        lastname=request.POST.get("lastname")
        username=request.POST.get('username')
        email=request.POST.get("email")
        dob=request.POST.get('dob')
        print(dob,type(dob))
        dob=dob.split("-")
        print(dob,type(dob))
        phno=request.POST.get("phno")
        interest=json.loads(request.POST.get('interests'))
        hobbie=json.loads(request.POST.get("hobbies"))
        skill=json.loads(request.POST.get('skills'))
        achievement=json.loads(request.POST.get("achievements"))
        print(firstname,middlename,lastname,username,email,dob,phno,interest,hobbie,skill,achievement)
        #middlename=request.POST.get('middlename')
        prof=profiles(user_name=request.user,first_name=firstname,middle_name=middlename,last_name=lastname,email=request.user.email)
        prof.save()
        bas=basic(profile=prof,date_of_birth=date(int(dob[0]),int(dob[1]),int(dob[2])),phone_number=phno)
        bas.save()
        inte=interests(profile=prof,interests=interest)
        inte.save()
        hob=hobbies(profile=prof,hobbies=hobbie)
        hob.save()
        skils=skills(profile=prof,skills=skill)
        skils.save()
        achi=achievements(profile=prof,achievements=achievement)
        achi.save()


    return JsonResponse({'firstname':firstname,
                            'middlename':middlename,
                            'lastname':lastname,
                            'username':username,
                            'email':email,
                            'dob':dob,
                            'phno':phno,
                            'interests':interest,
                            'hobbies':hobbie,
                            'skills':skill,
                            'achievements':achievement,})

@login_required
def updateProfilePic(request):
    if request.method=="POST" and request.FILES['image']:
        pr=profiles.objects.get(user_name=request.user)
        image = request.FILES['image']
        pr.profile_pic.save(image.name,image)
    return JsonResponse({'a':'a'})