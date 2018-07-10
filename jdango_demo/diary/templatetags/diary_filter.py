from django import template

register = template.Library()

@register.filter
def bin2str(value):
    return value.encode("utf-8")