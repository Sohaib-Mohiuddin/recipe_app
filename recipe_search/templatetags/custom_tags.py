from django import template
from django.utils.safestring import mark_safe, SafeData
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def split_as_option(value, splitter='|', autoescape=None):
    if not isinstance(value, SafeData):
        value = mark_safe(value)
    value = value.split(splitter)
    result = ""
    for v in value:
        result += '<option value="%s">%s</option>\n' % (v, v)
    return mark_safe(result)