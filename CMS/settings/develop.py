from .common import *


ALLOWED_HOSTS = ['localhost', '127.0.0.1',]


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = DEBUG

# Secret key for development
SECRET_KEY = 'secret_key'



# подключение debug_toolbar
INTERNAL_IPS = ['localhost', '127.0.0.1']
INSTALLED_APPS.append('debug_toolbar')
MIDDLEWARE.append('debug_toolbar.middleware.DebugToolbarMiddleware')
