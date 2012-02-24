from os import path

# Set PROJECT_ROOT to the dir of the current file
PROJECT_ROOT = path.dirname(__file__)

# DJANGO_PROJECT: the short project name
# (defaults to the basename of PROJECT_ROOT)
DJANGO_PROJECT = path.basename(PROJECT_ROOT.rstrip('/'))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = path.join(PROJECT_ROOT, 'static', 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/static/media/'

# staticfiles
STATIC_ROOT = path.join(PROJECT_ROOT, 'static', 'apps')
STATIC_URL = '/static/apps/'
STATICFILES_DIRS = [
    ('global', path.join(PROJECT_ROOT, 'static', 'global')),
]

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

MIDDLEWARE_CLASSES = [
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    path.join(PROJECT_ROOT, 'templates')
)

# Log debug messages to standard output
if DEBUG:
    import logging
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(levelname)-8s %(message)s',
                        datefmt='[%d/%b/%Y %H:%M:%S]')
                        
    logging.getLogger('django.db.backends').setLevel(logging.WARNING)
    
    DEBUG_TOOLBAR_CONFIG = {
        'INTERCEPT_REDIRECTS' : False,
    }
    
    # Consider ourself as internal IP
    from socket import gethostname, gethostbyname
    try:
        hostname = gethostbyname(gethostname())
        INTERNAL_IPS = ('127.0.0.1', hostname)
    except:
        INTERNAL_IPS = ('127.0.0.1', )
    
    # Default to SQLite database for debugging
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': path.join(PROJECT_ROOT, 'database.sqlite')
        }
    }

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
    'raven.contrib.django',
]
