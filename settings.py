# Smarter settings working, based on work by Rob Golding
# http://www.robgolding.com/blog/2010/05/03/extending-settings-variables-with-local_settings-py-in-django/

try:
    from settings_local import *
except ImportError:
    from settings_default import *
