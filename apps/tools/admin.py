from django.contrib import admin
from apps.tools.models import HttpRequest


class HttpRequestOrderAdmin(admin.ModelAdmin):
    '''HttpRequest admin interface
    '''
    list_display = ('ip', 'time', 'request_path', 'request_method', 'user')

    list_filter = ('request_method', 'time', 'ip', 'request_path')

admin.site.register(HttpRequest, HttpRequestOrderAdmin)
