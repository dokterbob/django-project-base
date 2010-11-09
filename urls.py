from django.conf.urls.defaults import *
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    
    urlpatterns = staticfiles_urlpatterns()
    
    from os import path
    urlpatterns += patterns('django.views', (r'^%s(?P<path>.*)$' % settings.MEDIA_URL,
                                              'static.serve', 
                                             {'document_root': settings.MEDIA_ROOT }))
    
else:
    urlpatterns = patterns('')

urlpatterns += patterns('',
    #(r'^/', include('foo.urls')),

    # Django Admin
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
)
