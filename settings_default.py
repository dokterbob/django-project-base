from os import path

# Set PROJECT_ROOT to the dir of the current file
PROJECT_ROOT = path.dirname(__file__)

# DJANGO_PROJECT: the short project name
# (defaults to the basename of PROJECT_ROOT)
DJANGO_PROJECT = path.basename(PROJECT_ROOT.rstrip('/'))

FIXTURE_DIRS = (path.join(PROJECT_ROOT, 'fixtures'),)

DEBUG = True
TEMPLATE_DEBUG = DEBUG

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Amsterdam'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'nl'

gettext = lambda s: s

LANGUAGES = (
    ('nl', gettext('Dutch')),
    ('en', gettext('English')),
)

"""
django-staticfiles and media

For staticfiles and media, the following convention is used:

* '/static/media/': Application media default path
* '/static/global/': Global static media
* '/static/apps/<app_name>/': Static assets after running `collectstatic`

The respective URL's (available only when `DEBUG=True`) are in `urls.py`.

More information:
https://docs.djangoproject.com/en/1.4/ref/contrib/staticfiles/
"""

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = path.join(PROJECT_ROOT, 'static', 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/static/media/'

STATIC_ROOT = path.join(PROJECT_ROOT, 'static', 'apps')
STATIC_URL = '/static/apps/'
STATICFILES_DIRS = [
    ('global', path.join(PROJECT_ROOT, 'static', 'global')),
]

"""
These are basically the default values from the Django configuration, written
as a list for easy manipulation. This way one can:

1. Easily add, remove or replace elements in the list, ie. overriding.
2. Know what the defaults are, if you want to change them right here. This
   way you won't have to look them up everytime you want to change.
"""
MIDDLEWARE_CLASSES = [
    'raven.contrib.django.raven_compat.middleware.SentryResponseErrorIdMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'djangosecure.middleware.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

TEMPLATE_CONTEXT_PROCESSORS = [
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.core.context_processors.static',
    # 'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
]

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    path.join(PROJECT_ROOT, 'templates')
)

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.staticfiles',
    'django_extensions',
    'debug_toolbar',
    'raven.contrib.django.raven_compat',
    'south',
    'djangosecure',
]

# django-secure
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True

SECURE_SSL_REDIRECT = True

SECURE_CHECKS = [
    "djangosecure.check.csrf.check_csrf_middleware",
    "djangosecure.check.sessions.check_session_cookie_secure",
    "djangosecure.check.sessions.check_session_cookie_httponly",
    "djangosecure.check.djangosecure.check_security_middleware",
    # We are using Django's X_FRAME_OPTIONS
    # "djangosecure.check.djangosecure.check_frame_deny",
    "djangosecure.check.djangosecure.check_content_type_nosniff",
    "djangosecure.check.djangosecure.check_xss_filter",
    "djangosecure.check.djangosecure.check_ssl_redirect",
]

# Whether or not SSL is required for accessing this site
SSL_DEFAULT = False

if SSL_DEFAULT:
    SECURE_CHECKS.append("djangosecure.check.djangosecure.check_sts")

    # 12 months for HSTS
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True

    SESSION_COOKIE_SECURE = True
else:
    # If not SSL default, force at least SSL for admin and accounts by default
    SECURE_REDIRECT_EXEMPT = [
        '^(?!accounts/|admin/).*'
    ]

    SESSION_COOKIE_SECURE = False

# Don't expose session cookie to JS
SESSION_COOKIE_HTTPONLY = True
X_FRAME_OPTIONS = 'DENY'

# Default for Lighttpd
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
