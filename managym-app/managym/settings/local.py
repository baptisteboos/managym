from . import *

ALLOWED_HOSTS= ['127.0.0.1', 'localhost']

# Django debug toolbar
INSTALLED_APPS += ['debug_toolbar']
MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']
INTERNAL_IPS = ['127.0.0.1']