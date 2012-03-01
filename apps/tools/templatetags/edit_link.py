from django import template
from django.core import urlresolvers
register = template.Library()


@register.simple_tag
def edit_link(obj):
    try:
        app_label = obj.__module__.split('.')[-2].lower()
        model_name = obj.__class__.__name__.lower()
        url = urlresolvers.reverse(
                            'admin:%s_%s_change' %
                            (app_label, model_name),
                            args=(obj.pk,))
    except AttributeError:
        url = None
    return url
