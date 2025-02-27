from django.db import models
from django.contrib.auth.models import User
from main.models import Users
from datetime import date
# Create your models here.
class profiles(models.Model):
    profile_pic=models.ImageField(upload_to="profilePictures/",blank=True)
    user_name=models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_name")
    first_name=models.CharField(max_length=128,blank=False)
    middle_name=models.CharField(max_length=128,blank=True)
    last_name=models.CharField(max_length=128,blank=False)
    email=models.EmailField(unique=True)
    is_online=models.BooleanField(default=False)
    def __str__(self):
        if self.first_name:
            return f'{self.first_name} {self.middle_name} {self.last_name}'
        else:
            return f'{self.user_name}'
        

class basic(models.Model):
    profile=models.ForeignKey(profiles,on_delete=models.CASCADE,related_name="basic")
    date_of_birth=models.DateField(blank=True)
    phone_number=models.IntegerField(blank=False)
    languages=models.TextField(blank=True,default='[]')


    @property
    def age(self):
        today = date.today()
        age = today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
        return age
    
    def __str__(self):
        return f'{self.profile.first_name} {self.profile.middle_name} {self.profile.last_name} basic details'

class interests(models.Model):
    profile=models.ForeignKey(profiles,on_delete=models.CASCADE,related_name="interests")
    interests=models.TextField(default='[]')

    def __str__(self):
        return f'{self.profile.first_name} {self.profile.middle_name} {self.profile.last_name} interest'
    
class education(models.Model):
    profile=models.ManyToManyField(profiles,related_name="education")
    school_name=models.CharField(max_length=254,blank=True)
    degree=models.CharField(max_length=128,blank=True)
    percentage=models.DecimalField(max_digits=3,decimal_places=3,blank=True)
    def __str__(self):
        return f'{self.profile.first_name} {self.profile.middle_name} {self.profile.last_name} {self.degree} education details'
    
class hobbies(models.Model):
    profile=models.ForeignKey(profiles,on_delete=models.CASCADE,related_name="hobbies")
    hobbies=models.TextField(default='[]')

    def __str__(self):
        return f'{self.profile.first_name} {self.profile.middle_name} {self.profile.last_name} hobbies'
    
class skills(models.Model):
    profile=models.ForeignKey(profiles,on_delete=models.CASCADE,related_name="skills")
    skills=models.TextField(default='[]')

    def __str__(self):
        return f"{self.profile.first_name} {self.profile.middle_name} {self.profile.last_name} skills"
    
class workExperience(models.Model):
    profile=models.ManyToManyField(profiles,related_name="workExperience")
    work_place_name=models.CharField(max_length=256,blank=True)
    work_place_job=models.CharField(max_length=128,blank=True)
    work_place_startdate=models.DateField(blank=True)
    work_place_enddate=models.DateField(blank=True)
    work_place=models.CharField(max_length=128,blank=True)

    def __str__(self):
        return f'{self.profile.first_name} {self.profile.middle_name} {self.profile.last_name} {self.work_place_name} work experience'

class achievements(models.Model):
    profile=models.ForeignKey(profiles,on_delete=models.CASCADE,related_name="acheivements")
    achievements=models.TextField(default='[]')

    def __str__(self):
        return f'{self.profile.first_name} {self.profile.middle_name} {self.profile.last_name} achievements'
    
class contact_info(models.Model):
    profile=models.ForeignKey(profiles,on_delete=models.CASCADE,related_name="contact_info")
    address=models.CharField(max_length=256,blank=True)
    linkedin_link=models.URLField(blank=True)
    github_link=models.URLField(blank=True)

    def __str__(self):
        return f'{self.profile.first_name} {self.profile.middle_name} {self.profile.last_name} contact_info'