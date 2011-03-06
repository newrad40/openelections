from django.conf.urls.defaults import *

urlpatterns = patterns('openelections.petitions.views',
    (r'^$', 'index'),
    (r'^(?P<issue_slug>[\w-]+)/?$', 'detail'),
    (r'^(?P<issue_slug>[\w-]+)/sign$', 'sign'),
    (r'^api/count/(?P<issue_slug>[\w-]+)/$', 'api_count'),
    (r'^(?P<issue_slug>[\w-]+)/addpaper$', 'add_signatures'),
    (r'^(?P<issue_slug>[\w-]+)/viewpaper$', 'view_signatures'),


)