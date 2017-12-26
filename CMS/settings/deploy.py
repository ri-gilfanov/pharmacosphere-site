from .common import *

# Импорт секретных настроек
# В честности, SECRET_KEY и DATABASES
from .secret import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
TEMPLATE_DEBUG = DEBUG
