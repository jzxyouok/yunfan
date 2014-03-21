from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myyunfan.views.home', name='home'),
    # url(r'^myyunfan/', include('myyunfan.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^$', 'myyunfan.views.home', name='home'),
    url(r'^aboutus$', 'myyunfan.views.aboutus', name='aboutus'),

    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),
    url(r'^rest/', include('rest_test.urls')),
    url(r'^mygroups/', include('mygroups.urls')),
    url(r'^myre/', include('myrelationships.urls')),
    url(r'^myme/', include('mymessages.urls')),
    url(r'^avatar/', include('avatar.urls')),
    url(r'^newstudents/', include('newstudents.urls')),
    url(r'^mylab/', include('mylab.urls')),
    url(r'^captcha/', include('captcha.urls')),

    
)

#apps
urlpatterns += patterns('',
    url(r'^question/', include('myapps.urls')),
    url(r'^info/', include('info.urls')),
    
)

urlpatterns += patterns('',
    url(r'^accounts/', include('myaccount.urls')),
    url(r'^users/', include('myaccount.user_urls')),
)

urlpatterns += staticfiles_urlpatterns()


#to use media
from django.conf.urls.static import static
from django.conf import settings

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
