from django.db import models
from main.models import Networks,Users
# Create your models here.
class privatechat(models.Model):

    user1 = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='user1_chats')
    user2 = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='user2_chats')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Chat between {self.user1.email} and {self.user2.email}"
    

class Messages(models.Model):
    chat = models.ForeignKey(privatechat, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(Users, on_delete=models.CASCADE)
    content = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    video = models.FileField(upload_to='videos/', blank=True, null=True)
    send_timestamp = models.DateTimeField(auto_now_add=True)
    received_timestamp=models.DateTimeField(auto_now_add=True)# "NEED TO CHANGE LATER"

    def __str__(self):
        return f"Message from {self.sender.email} at {self.send_timestamp}"