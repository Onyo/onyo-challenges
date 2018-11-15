#!/bin/bash
python manage.py makemigrations sorteios
python manage.py makemigrations
python manage.py migrate --run-syncdb
python manage.py runserver 0.0.0.0:7000