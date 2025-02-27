from django.db import models
from main.models import Networks,Users
from chats.models import Messages,privatechat
# Create your models here.
class Notification(models.Model):
    notif_from_user=models.ForeignKey(Users,on_delete=models.CASCADE,related_name="notif_from_user")
    is_seen=models.BooleanField(default=False)
    notif_content=models.TextField()
    notif_send_time=models.DateTimeField(auto_now_add=True)
    notif_received_time=models.DateTimeField(null=True,blank=True)
    notif_to_user=models.ForeignKey(Users,on_delete=models.CASCADE,related_name="notif_to_user")
    def __str__(self):
        return f'{self.notif_from_user} sent a Notification to {self.notif_to_user}'
        