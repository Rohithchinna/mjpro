from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Activity)
class MessagesAdmin(admin.ModelAdmin):
    list_filter=['profile','activity','activity_desc','time']
    search_fields=['profile','activity','activity_desc','time']
    readonly_fields=['time']
    ordering=['-time']