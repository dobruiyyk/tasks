from django.contrib import admin
from apps.tools.models import HttpRequest, DbEntry


class HttpRequestOrderAdmin(admin.ModelAdmin):
    '''HttpRequest admin interface
    '''
    list_display = ('ip', 'time', 'request_path', 'request_method', 'user')

    list_filter = ('request_method', 'time', 'ip', 'request_path')


class DbEntryAdmin(admin.ModelAdmin):
    list_display = ('model', 'object', 'comment', 'time', 'pk')
    list_filter = ('model', 'comment', 'time')

admin.site.register(HttpRequest, HttpRequestOrderAdmin)
admin.site.register(DbEntry, DbEntryAdmin)
