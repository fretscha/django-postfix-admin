from django import template
import unicodedata

register = template.Library()


@register.filter("truncate")
def truncate(value, size):
    if len(value) > size:
        return value[0:size]
    else:
        return value


@register.filter("truncate_dot")
def truncate_dot(value, size):
    if value:
        if len(value) > size and size > 3:
            return value[0:(size - 3)] + '...'
        elif len(value) > size:
            return value[0:size]
        else:
            return value
    else:
        return value


@register.filter("strip_accents")
def strip_accents(value, encoding='ASCII'):
    try:
        return ''.join(
            (c for c in unicodedata.normalize('NFD', unicode(value))
             if unicodedata.category(c) != 'Mn'))
    except:
        return value


@register.filter("zero2unlimited")
def zero2unlimited(value, unit=''):
    try:
        if value == 0:
            return "unlimited"
        else:
            return "{0}{1}{2}".format(value, " ", unit)
    except:
        return "{0}{1}{2}".format('(', value, ')')
