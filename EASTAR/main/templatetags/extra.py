from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def FindPhoto(value):
    if "%photo%" in str(value):
        return True
    else:
        return False


@register.filter
@stringfilter
def ReplacePhoto(value):
    return value.replace("%photo%","")
