from django.contrib import admin
from .models import myPosts,likes
# Register your models here.
@admin.register(myPosts)
class myPostsadmin(admin.ModelAdmin):
    ordering = ('-posted_at',)

admin.site.register(likes)