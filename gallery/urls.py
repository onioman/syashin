from django.conf.urls import patterns, url

from gallery import views
from syashin import settings


urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^image/new/$', views.imageCreate, name='imageCreate'),
        url(r'^(?P<image_id>\d+)/$', views.detail, name='detail'),
        url(r'^(?P<image_id>\d+)/change/$', views.change, name='change'),
        url(r'^album/(?P<album_id>\d+)/$', views.albumIndex, name='albumIndex'),
        url(r'^album/new/$', views.albumCreate, name='albumCreate'),
        url(r'^album/(?P<album_id>\d+)/remove/(?P<image_id>\d+)/$', views.albumRemoveImage, name='albumRemoveImage'),
)
