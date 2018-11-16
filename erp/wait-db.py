import socket
import sys

from decouple import config
from dj_database_url import parse as db_url

db_config = config(
    'DATABASE_URL', default='postgres://dev-cep-user:dev-cep-password@localhost:5432/dev-cep', cast=db_url
)
while True:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((db_config['HOST'], int(db_config['PORT'])))
    if result == 0:
        sys.exit(result)
