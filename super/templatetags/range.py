from django import template
from builtins import range as __range__


register = template.Library()

@register.filter(name='range')
def range(value, zero_index=True):
    if not zero_index:
        return __range__(1, value, 1) 
    return __range__(value)

