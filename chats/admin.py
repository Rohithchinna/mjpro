from django.contrib import admin
from .models import privatechat,Messages
# Register your models here.
@admin.register(privatechat)
class privatechatadmin(admin.ModelAdmin):
    list_display = ('user1', 'user2', 'created_at')
    list_filter = ('user1','user2', 'created_at')
    search_fields = ('user1', 'user2','created_at')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)

@admin.register(Messages)
class MessagesAdmin(admin.ModelAdmin):
    list_display=['chat','sender','content','image','video','send_timestamp','received_timestamp']
    list_filter=['chat','sender','content','send_timestamp','received_timestamp']
    search_fields=['chat','sender','content','send_timestamp','received_timestamp']
    readonly_fields=['send_timestamp','received_timestamp']
    ordering=['-send_timestamp','-received_timestamp']