# Smarter settings working, based on work by Rob Golding
# http://www.robgolding.com/blog/2010/05/03/extending-settings-variables-with-local_settings-py-in-django/

import logging
logger = logging.getLogger('django-project-base')

try:
    from settings_local import *
except ImportError:
    logger.exception('Error importing settings_local')
    
    from settings_default import *
