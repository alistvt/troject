from django import template
from tasks.models import Task

register = template.Library()

@register.simple_tag
def getColor(index):
    return Task.Groups.colors[index]
