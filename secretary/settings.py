from base.settings import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

SECRET_KEY = '(ss1^u3cy=4zj7us50^k^$j1t%$uc18h2bob@l&47=gaa1h98w'

# Application definition

INSTALLED_APPS += [
    'secretary'
]

ROOT_URLCONF = 'secretary.urls'

POSTMAN_SERVICE_URL = os.getenv("POSTMAN_SERVICE_URL", "http://localhost:8000/locations/")

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
if os.getenv("DATABASE_URL", None):
    import dj_database_url
    db_from_env = dj_database_url.config()
    DATABASES = {}
    DATABASES['default'] = db_from_env
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'secretary.sqlite3'),
        }
    }