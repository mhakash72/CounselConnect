from .base import *  # noqa
from .base import env

# Debug settings
DEBUG = True
SECRET_KEY = env('DJANGO_SECRET_KEY', default='django-insecure-development-key-change-in-production')
ALLOWED_HOSTS = ['localhost', '0.0.0.0', '127.0.0.1']

# Email settings for development
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Django Debug Toolbar
INSTALLED_APPS += ['debug_toolbar']  # noqa F405
MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']  # noqa F405
DEBUG_TOOLBAR_CONFIG = {
    'DISABLE_PANELS': ['debug_toolbar.panels.redirects.RedirectsPanel'],
    'SHOW_TEMPLATE_CONTEXT': True,
}
INTERNAL_IPS = ['127.0.0.1', '10.0.2.2']

# Cache settings
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': '',
    }
}

# Django extensions for development tools
INSTALLED_APPS += ['django_extensions']  # noqa F405