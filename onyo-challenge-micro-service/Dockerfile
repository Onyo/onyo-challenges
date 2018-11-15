FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /sorteios_microservice
WORKDIR /sorteios_microservice
ADD . /sorteios_microservice
EXPOSE 7000
RUN python -m pip install --upgrade pip
RUN pip install pipenv
RUN pipenv install
RUN pipenv install --system --deploy --ignore-pipfile
RUN chmod +X start.sh
RUN ls -la