from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import RedirectView

from bookwormsunite.views import *

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'ITech.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^$', index, name='index'),
                       url(r'^calendar/(?P<offset>\-?[0-9]+)/$', calendar, name='calendar'),
                       url(r'^readathon/$', RedirectView.as_view(pattern_name='index'), name='readathon'),
                       url(r'^readathon/(?P<readathon_name_slug>[\w\-]+)/$', readathon_info),
                       url(r'^user/(?P<uid>[0-9]+)/$', user_info, name="user_info"),
                       url(r'^user/(?P<uid>[0-9]+)/summary/$', user_summary),
                       url(r'^login/$', login, name='login'),
                       url(r'^logout/$', logout, name='logout'),
                       url(r'^register/$', register, name='register'),
                       url(r'^search/$', search),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^user/(?P<uid>[0-9]+)/upload_picture/$', upload_pic, name='upload_pic'),
                       )
