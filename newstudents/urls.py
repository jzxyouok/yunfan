from django.conf.urls import patterns, include, url
from views import navigation,baoding

urlpatterns = patterns('',
    url(r'^navigation', navigation),
    url(r'^baoding', baoding),
    )