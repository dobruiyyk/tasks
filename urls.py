from django.conf.urls.defaults import patterns, include, url
from apps.personal_info.views import main_page
from apps.tools.views import requests
from django.contrib.auth import views as auth_views
from apps.personal_info.views import main_page_form
import os

from django.contrib import admin
admin.autodiscover()

project_dir = os.getcwd()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    (r'^admin/jsi18n', 'django.views.i18n.javascript_catalog'),

    url(r'^tiny_mce/(?P<path>.*)$', 'django.views.static.serve',
                {'document_root':
                  '%s/media/js/tiny_mce/' % project_dir}),

   url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': '%s/media/static/' % project_dir}),

    url(r'^form/photo/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': '%s/media/photo/' % project_dir}),

     url(r'^photo/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': '%s/media/photo/' % project_dir}),

    url(r'^login/$', auth_views.login,
                        {'template_name': 'registration/login.html'},
                        name='auth_login'),
    url(r'^logout/$', auth_views.logout,
                        {'template_name': 'registration/logout.html'},
                        name='auth_logout'),

    url(r'^$', main_page, name='main'),
    url(r'^requests/$', requests, name='requests'),
    url(r'^form/$', main_page_form,
                    name='form'),
)
