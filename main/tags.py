# myapp/templatetags/my_tags.py
from django import template
from .views import my_view

register = template.Library()

@register.simple_tag
def call_my_view():
    return my_view()