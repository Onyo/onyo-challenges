#!/bin/bash
python manage.py makemigrations users
python manage.py makemigrations api
python manage.py makemigrations
python manage.py migrate --run-syncdb
python manage.py createcachetable
python manage.py runserver 0.0.0.0:8000