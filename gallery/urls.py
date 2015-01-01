from django.conf.urls import patterns, url

from gallery import views
from syashin import settings


urlpatterns = patterns('',
        #url(r'^$', views.index, name='index'),
        url(r'^$', views.IndexView.as_view(), name='index'),
        url(r'^(?P<image_id>\d+)/$', views.detail, name='detail'),
        url(r'^(?P<image_id>\d+)/change/$', views.change, name='change'),
)
