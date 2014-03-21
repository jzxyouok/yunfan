#coding=utf-8
from views import show_all_information, show_information_by_id,search_by_title,show_by_categories,show_by_tag,view
from django.conf.urls.defaults import patterns, url
from view.create_info import create_info,show_user

urlpatterns = patterns('',
    url(r'^$',show_all_information),
    url(r'^i/(?P<info_id>\d+)/$',show_information_by_id),
    url(r'^create/$',create_info),
    url(r'^show_user/$',show_user),
    
   (r'^categories/(?P<categories>\d+)$',show_by_categories),
   (r'^tag/(?P<tag>[^/]+)$',show_by_tag),

   (r'^search/$',search_by_title),
   #关注
   (r'^view/(?P<info_id>\d+)/$',view),


)