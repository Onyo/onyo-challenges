from core.settings import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'jz_ixkqb)f*0fp6rgo*shujl%aw4()qdjlybl0i6rbv2(ruj@c'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

INSTALLED_APPS += [
    'bob',
]

ROOT_URLCONF = 'urls'

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'bob.sqlite3'),
    }
}

if os.getenv('DATABASE_URL', None):
    # Update database configuration with $DATABASE_URL.
    import dj_database_url
    db_from_env = dj_database_url.config()
    DATABASES['default'].update(db_from_env)