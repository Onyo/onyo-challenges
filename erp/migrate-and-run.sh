#!/bin/sh

set -e

python wait-db.py
python manage.py migrate
exec python manage.py runserver 0.0.0.0:$PORT
