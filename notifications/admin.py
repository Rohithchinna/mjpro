from django.contrib import admin
from .models import Notification
# Register your models here.
@admin.register(Notification)
class Notification_admin(admin.ModelAdmin):
    list_display=['notif_from_user','is_seen','notif_content','notif_send_time','notif_received_time','notif_to_user']
    list_filter=['notif_from_user','is_seen','notif_content','notif_send_time','notif_received_time','notif_to_user']
    search_fields=['notif_from_user','is_seen','notif_content','notif_to_user']
    readonly_fields=['notif_send_time','notif_received_time',]
    ordering=['notif_content','notif_send_time','notif_received_time']