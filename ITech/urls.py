from django.conf.urls import patterns, include, url
from django.contrib import admin

from bookwormsunite.views import index, readathon_info, user_info, user_summary, login, register, search

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'ITech.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^$', index),
                       url(r'^readathon/(?P<readathon_name_slug>[\w\-]+)/$', readathon_info),
                       url(r'^user/(?P<uid>[0-9]+)/$', user_info),
                       url(r'^user/(?P<uid>[0-9]+)/summary/$', user_summary),
                       url(r'^login/$', login),
                       url(r'^register/$', register),
                       url(r'^search/$', search),
                       url(r'^admin/', include(admin.site.urls)),

                       )
