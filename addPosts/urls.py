from django.contrib import admin
from django.urls import path,include
from .views import UploadPost
from . import views


urlpatterns= [
    path('',views.addPosts,name="addPosts"),
    path('uploadPost',UploadPost.as_view(),name="uploadPost"),
    path('addLike',views.addLike,name="addLike"),
]