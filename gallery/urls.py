from django.conf.urls import patterns, url

from gallery import views
from syashin import settings


urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^(?P<image_id>\d+)/$', views.detail, name='detail'),
)
