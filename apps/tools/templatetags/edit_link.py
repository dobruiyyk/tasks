from django import template
from django.core import urlresolvers
#from django.template.Library import simple_tag

register = template.Library()


@register.simple_tag
def edit_link(obj):
    app_label = obj.__module__.split('.')[-2].lower()
    model_name = obj.__class__.__name__.lower()
    url = urlresolvers.reverse(
                            'admin:%s_%s_change' %
                            (app_label, model_name),
                            args=(obj.pk,))
    link = "<a href='%s'</a>" % url
    return link
'''
def edit_link(parser, token):
    objct = token.split_contents()
    if len(objct) != 2:
        raise template.TemplateSyntaxError("""'edit_link'
        tag takes exactly one argument""")

    return EditLinkNode(objct)


class EditLinkNode(template.Node):
    def __init__(self, objct):
        self.object = objct
        self.app_label = self.object.__module__.split('.')[-2]
        self.model_name = self.object.__class__.__name__

    def render(self, context):
        link = urlresolvers.reverse(
                            "<a href='admin:%s_%s_change'</a>" %
                            (self.app_label, self.model_name),
                            args=(self.object.id))
        return link

register.tag('edit_link', edit_link)
'''
