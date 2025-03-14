"""
URL configuration for mjpro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views
from main.models import Users
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homepage,name="homepage"),
    path('register/',views.register,name="register"),
    path('login/',views.login,name="login"),
    path('regsubmit/',views.regsubmit,name="regsubmit"),
    path('logsubmit/',views.logsubmit,name="logsubmit"),

    path('main/', include('main.urls')),
    path('chats/', include('chats.urls')),
    path('notifications/',include('notifications.urls')),
    path('profile/',include('profiles.urls')),
    path('activity/',include('activity.urls')),
    path('addPosts/',include('addPosts.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
