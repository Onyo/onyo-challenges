#!/bin/sh

set -ex

while ! nc -z ${DEFAULT_DATABASE_HOST} ${DEFAULT_DATABASE_PORT}; do
  sleep 0.1 # wait for 1/10 of the second before check again
done

python manage.py migrate
exec python manage.py runserver 0.0.0.0:8000
