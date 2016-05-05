from core.settings import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'jz_ixkqb)f*0fp6rgo*shujl%aw4()qdjlybl0i6rbv2(ruj@c'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

INSTALLED_APPS += [
    'bob',
    'ana',
]

ROOT_URLCONF = 'core.urls'

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


