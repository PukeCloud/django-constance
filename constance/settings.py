import os
from .utils import import_module_attr

settings = import_module_attr(
    os.getenv('CONSTANCE_SETTINGS_MODULE', 'django.conf.settings')
)

REDIS_PREFIX = getattr(settings, 'CONSTANCE_REDIS_PREFIX',
               getattr(settings, 'CONSTANCE_PREFIX', 'constance:'))

BACKEND = getattr(settings, 'CONSTANCE_BACKEND',
                  'constance.backends.redisd.RedisBackend')

CONFIG = getattr(settings, 'CONSTANCE_CONFIG', {})

CONNECTION_CLASS = getattr(settings, 'CONSTANCE_REDIS_CONNECTION_CLASS',
                   getattr(settings, 'CONSTANCE_CONNECTION_CLASS', None))

REDIS_CONNECTION = getattr(settings, 'CONSTANCE_REDIS_CONNECTION',
                   getattr(settings, 'CONSTANCE_CONNECTION', {}))

DATABASE_CACHE_BACKEND = getattr(settings, 'CONSTANCE_DATABASE_CACHE_BACKEND',
                                 None)

DATABASE_CACHE_AUTOFILL_TIMEOUT = getattr(settings,
                                          'CONSTANCE_DATABASE_CACHE_AUTOFILL_TIMEOUT',
                                          60 * 60 * 24)

DATABASE_PREFIX = getattr(settings, 'CONSTANCE_DATABASE_PREFIX', '')

SUPERUSER_ONLY = getattr(settings, 'CONSTANCE_SUPERUSER_ONLY', True)
