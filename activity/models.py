from django.db import models
from profiles.models import *
# Create your models here.
class Activity(models.Model):
    profile=models.ForeignKey(User,on_delete=models.CASCADE,related_name="activity")
    activity=models.CharField(max_length=256)
    activity_desc=models.CharField(max_length=300)
    time=models.DateTimeField(auto_now_add=True)
    count=models.IntegerField(default=0)


    def __str__(self):
        return f"{self.profile.username}'s {self.activity}"