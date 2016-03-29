from base.settings import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(ss1^u3cy=4zj7us50^k^$j1t%$uc18h2bob@l&47=gaa1h98w'


INSTALLED_APPS += ["postman", "secretary"]	

ROOT_URLCONF = 'urls'

POSTMAN_SERVICE_URL = os.getenv("POSTMAN_SERVICE_URL", "http://localhost:8000/locations/")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'local.sqlite3'),
    }
}