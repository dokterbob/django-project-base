from os import path

# Set PROJECT_ROOT to the dir of the current file
PROJECT_ROOT = path.dirname(__file__)

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

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/static/global/admin/'

# staticfiles
STATIC_ROOT = path.join(PROJECT_ROOT, 'static', 'global')
STATIC_URL = '/static/global/'

MIDDLEWARE_CLASSES = [
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
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
    INTERNAL_IPS = ( '127.0.0.1', 
                     gethostbyname(gethostname()),)
    
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
    'django_extensions',
    'debug_toolbar',
    'sentry.client',
    'django.contrib.staticfiles',
]
