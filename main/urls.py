from django.contrib import admin
from django.urls import path,include
from . import views
from mjpro import views as mjviews
from main.models import Users
from chats import views as chatviews



urlpatterns= [
    path('',views.home,name="home"),
    path("signout/",views.signout,name="signout"),
    #path('chats/',views.chats,name="chats"),
    path('networks/',views.networks,name="networks"),
    path('addfriend/<str:username>',views.addfriend,name="addfriend"),
    

]