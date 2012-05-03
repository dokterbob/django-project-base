from django.conf.urls.defaults import *
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static


# Serve django-staticfiles (only works in DEBUG)
urlpatterns = staticfiles_urlpatterns()

# Serve media files (only works in DEBUG)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler500 = 'views.handler500'

urlpatterns += patterns('',
    #(r'^/', include('foo.urls')),

    # Django Admin, docs and password reset
    url(r'^admin/password_reset/$', 'django.contrib.auth.views.password_reset', name='admin_password_reset'),
    url(r'^admin/password_reset/done/$', 'django.contrib.auth.views.password_reset_done'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # Admin tools
    url(r'^admin_tools/', include('admin_tools.urls')),

    # Password reset
    url(r'^accounts/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm'),
    url(r'^accounts/reset/done/$', 'django.contrib.auth.views.password_reset_complete')
)

