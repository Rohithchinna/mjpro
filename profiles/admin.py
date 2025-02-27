from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(profiles)
class pofilesAdmin(admin.ModelAdmin):
    search_fields = ('first_name', 'middle_name','last_name')

@admin.register(basic)
class basicAdmin(admin.ModelAdmin):
    list_filter = ('date_of_birth',)
    search_fields = ('date_of_birth',)

admin.site.register(interests)

@admin.register(education)
class educationAdmin(admin.ModelAdmin):
    list_filter = ('profile','school_name','degree','percentage')
    search_fields = ('profile','school_name','degree','percentage')

admin.site.register(hobbies)

admin.site.register(skills)

@admin.register(workExperience)
class workExperienceAdmin(admin.ModelAdmin):
    list_filter = ('profile','work_place_name','work_place_job','work_place')
    search_fields = ('profile','work_place_name','work_place_job','work_place')

admin.site.register(achievements)

admin.site.register(contact_info)