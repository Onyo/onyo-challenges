import dj_database_url

from config.ana.settings import *

# Update database configuration with $DATABASE_URL.
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['ana_db'].update(db_from_env)
DATABASES['default'].update(db_from_env)
