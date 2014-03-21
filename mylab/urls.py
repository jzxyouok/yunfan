from views import *
from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('',   
    url(r'^ajax$',ajax),
    url(r'^sendemail$',sendemail),

    

)