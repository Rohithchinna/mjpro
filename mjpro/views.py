from django.shortcuts import render,redirect
from django.template import loader
from django.http import HttpResponse
from main.models import Users
from django.contrib import messages
from django.contrib.auth.hashers import check_password,make_password
from django.contrib.auth.models import User
from django.contrib import auth
from main.templates import *
from django.core.cache import cache
from main.globals import uservar
from django.views.decorators.csrf import csrf_protect
from profiles.models import *
from main import urls


def homepage(request):
  template = loader.get_template('homepage.html')
  return render(request,"homepage.html")

def register(request):
  template=loader.get_template("register.html")
  return render(request, "register.html")

def login(request):
  return render(request, "login.html")


model_names = ["jellelalaxman@gmail.com","rohithenduri665@gmail.com","devsothmadhu2003@gmail.com","kummarigovardhan1234@gmail.com","sreethikamodala@gmail.com"]
def regsubmit(request):
    if request.method == 'POST':
      email = request.POST.get('email')
      ph_no = request.POST.get('phone')
      password = request.POST.get('password')  # Note: Hash this password before saving!
      password=make_password(password) #hashing password

      # Basic validation (you can expand this as needed)
      if email and ph_no and password:
          # Create a new User object and save it to the database
          user = Users(email=email, ph_no=ph_no, password=password)  # Consider hashing the password
          print(email,password)
          x=User(email=email,password=password,username=email)
          x.save()
          user=user.save()
          au=auth.authenticate(request,email=str(email))
          print(au)
          auth.login(request,user)
          messages.success(request, "Registration successful!")
          cache.set('authentication',True,timeout=60*15)
          pro_user=profiles(user_name=x,email=x.email,is_online=True)
          pro_user.save()
          return redirect("home")  # Redirect to a success page or another view
      else:
          messages.error(request, "All fields are required.")

    return render('some error occured')

@csrf_protect
def logsubmit(request):
   if request.method== 'POST':
      email=request.POST.get("email")
      password=request.POST.get("password")

      try:
            # Retrieve the user by email
            user = User.objects.get(email=email)
            print(user)

            # Compare the submitted password with the stored password
            if check_password(password, user.password):
                # Password is correct, proceed with login or other logic
                messages.success(request, "Login successful!")
                global uservar
                uservar=user.email
                print(user.email,user.password)
                au=auth.authenticate(request,email=str(user.email))
                print(au)
                auth.login(request,user)
                cache.set('uservar', user.email, timeout=60*15)
                cache.set('authentication',True,timeout=60*15)
                print(cache.get('authentication'))
                stat=profiles.objects.get(user_name=request.user)
                stat.is_online=True
                stat.save()
                return redirect("home") # Redirect to a success page
            else:
                # Password is incorrect
                messages.error(request, "Invalid password.")
                return HttpResponse(' password failed')
      except Users.DoesNotExist:
            # User with the provided email does not exist
            messages.error(request, "User  does not exist.")
            return HttpResponse('user does not exist')
   return HttpResponse('some error occured')   