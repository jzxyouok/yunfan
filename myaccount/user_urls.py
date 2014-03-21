from users_views import user, wwj
from mygroups.models import  GroupMember
from django.conf.urls.defaults import patterns, url


username = r'(?P<username>[-\w]+)/' 
urlpatterns = patterns('',
    url(r'^%s$'%username , user),

)
