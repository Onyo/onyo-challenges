import os

from config.base_settings import *

INSTALLED_APPS += [
    'api.v0.ana',
]

DATABASES['ana_db'] = {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': 'ana_db',
    'USER': os.environ.get('DB_USER'),
    'PASSWORD': os.environ.get('DB_PASS'),
}

DATABASE_ROUTERS += ['config.ana.db_router.AnaDBRouter']


'''
Configuration needed to fully decouple APIs
'''

CURRENT_BOB_API_URL = os.environ.get('CURRENT_BOB_API_URL')
