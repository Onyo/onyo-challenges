FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /main_service
WORKDIR /main_service
ADD . /main_service
EXPOSE 8000
RUN python -m pip install --upgrade pip
RUN pip install pipenv
RUN pipenv install
RUN pipenv install --system --deploy --ignore-pipfile
RUN pipenv run python manage.py makemigrations users
RUN pipenv run python manage.py makemigrations api
RUN pipenv run python manage.py makemigrations
RUN chmod +X start.sh
RUN ls -la