from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns= [
    path('',views.profile,name="profile"),
    path('update_profile_details',views.update_profile_details,name="update_profile_details"),
    path('updateProfilePic',views.updateProfilePic,name="updateProfilePic"),
] 