#coding=utf-8
from views2 import register,login_view,logout_view


from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('',
    
	url(r'^$',login_view),
	url(r'^register/$',register),
    url(r'^login/$',login_view),
    url(r'^logout/$',logout_view),

)
