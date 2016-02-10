from config.base_settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'default',
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASS'),
    }
}

INSTALLED_APPS += ['api.v0.ana', 'api.v0.bob']

CURRENT_BOB_API_URL = os.environ.get('CURRENT_BOB_API_URL')
