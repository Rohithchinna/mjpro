from django.db import models
from django.contrib.auth.models import *
from profiles.models import profiles
# Create your models here.
class myPosts(models.Model):
    profile=models.ForeignKey(profiles,on_delete=models.CASCADE,related_name="myposts")
    post=models.FileField(upload_to="posts/",blank=True,null=True)
    title=models.CharField(max_length=125)
    description=models.CharField(max_length=256)
    resource=models.URLField(blank=True,null=True)
    posted_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
class likes(models.Model):
    post=models.ForeignKey(myPosts,on_delete=models.CASCADE,related_name="likes")
    likes=models.IntegerField(default=0)
    liked_by=models.ManyToManyField(profiles,related_name="liked_by")
    def __str__(self):
        return f"{self.post} likes"