from config.base_settings import *

INSTALLED_APPS += [
    'bob',
]

DATABASES['bob_db'] = {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': 'bob_db',
    'USER': os.environ.get('DB_USER'),
    'PASSWORD': os.environ.get('DB_PASS'),
}

DATABASE_ROUTERS += ['config.bob.db_router.BobDBRouter']
