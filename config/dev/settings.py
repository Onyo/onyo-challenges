import os

from config.base_settings import *
from config.ana.settings import *
from config.bob.settings import *

DEBUG = True

CURRENT_BOB_API_URL = 'http://localhost:8000/api/v0/bob/'

'''
Configuration needed to enable communication between APIs
in services during tests
'''

os.environ['DJANGO_LIVE_TEST_SERVER_ADDRESS'] = 'localhost:8000'
