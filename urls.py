from django.conf.urls.defaults import patterns, include, url
from apps.personal_info.views import main_page
from apps.tools.views import requests
import os
project_dir = os.getcwd()

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tiny_mce/(?P<path>.*)$', 'django.views.static.serve',
                {'document_root': '%s/media/js/tiny_mce/' % project_dir}),

    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': '%s/media/static/' % project_dir}),

    url(r'^$', main_page, name='main'),
    url(r'^requests/$', requests, name='requests'),
)
