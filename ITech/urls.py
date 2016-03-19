from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import RedirectView

from ITech import settings
from bookwormsunite.views import *

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'ITech.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       # Index
                       url(r'^$', index, name='index'),

                       # REST API
                       url(r'^autocomplete_search/$', autocomplete_search, name='get_readathons'),
                       url(r'^calendar/(?P<offset>\-?[0-9]+)/$', calendar, name='calendar'),
                       url(r'^user/upload_pic/$', upload_pic, name="upload_pic"),
                       url(r'^login/$', login, name='login'),
                       url(r'^logout/$', logout, name='logout'),
                       url(r'^register/$', register, name='register'),

                       url(r'^readathon/(?P<readathon_name_slug>[\w\-]+)/join/$', readathon_join,
                           name='readathon_join'),

                       url(r'^user/upload_picture/', upload_pic, name='upload_pic'),
                       url(r'^twitter/(?P<query>[\w|\W-]+)/$', search_twitter_hashtag, name='search_twitter_hashtag'),
                       url(r'^search/books/(?P<query>[\w|\W]+)/$', search_book, name='search_book'),
                       url(r'^save_accomplishment/$', save_accomplishment, name='save_accomplishment'),

                       # Readathons
                       url(r'^readathon/$', RedirectView.as_view(pattern_name='index'), name='readathon'),
                       url(r'^readathon/(?P<readathon_name_slug>[\w\-]+)/$', readathon_info, name='readathon_info'),

                       # Users
                       url(r'^user/(?P<uid>[0-9]+)/$', user_info, name="user_info"),
                       url(r'^user/(?P<uid>[0-9]+)/summary/$', user_summary),

                       # Others
                       url(r'^about/$', about, name="about"),

                       # Admin
                       url(r'^admin/', include(admin.site.urls)),
                       )

if settings.DEBUG:
    urlpatterns += patterns(
            'django.views.static',
            (r'^media/(?P<path>.*)',
             'serve',
             {'document_root': settings.MEDIA_ROOT}), )
