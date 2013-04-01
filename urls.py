from django.conf.urls.defaults import *
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

# Sitemaps
from simplesite import sitemaps as simplesite_sitemaps

sitemaps = {
    'menu': simplesite_sitemaps.MenuSitemap,
    'submenu': simplesite_sitemaps.SubmenuSitemap,
    'pages': simplesite_sitemaps.PageSitemap
}


# Serve django-staticfiles (only works in DEBUG)
urlpatterns = staticfiles_urlpatterns()

# Serve media files (only works in DEBUG)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# 500 handler
handler500 = 'views.handler500'

urlpatterns += patterns('',
    #(r'^/', include('foo.urls')),
    # Sitemaps
    (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),

    # Django Admin, docs and password reset
    url(r'^admin/password_reset/$', 'django.contrib.auth.views.password_reset', name='admin_password_reset'),
    (r'^admin/password_reset/done/$', 'django.contrib.auth.views.password_reset_done'),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),

    # Password reset
    (r'^accounts/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm'),
    (r'^accounts/reset/done/$', 'django.contrib.auth.views.password_reset_complete')
)

