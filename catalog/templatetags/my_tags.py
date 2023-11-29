from django import template
from django.utils.html import conditional_escape
register = template.Library()

# тег
@register.simple_tag()
def mediapath(text):
    return f'/media/{text}'

# фильтр
@register.filter()
def mediapath(text):
    return f'/media/{text}'