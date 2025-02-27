from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns= [
path('',views.chats,name="chats"),
path('add_to_Messages/',views.add_to_Messages,name="add_to_Messages"),
path('past_messages/<str:receiver>/',views.past_messages,name="past_messages"),
]