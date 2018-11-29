FROM python:2.7.12-alpine

ENV PYTHONUNBUFFERED 1

RUN mkdir /app

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r /app/requirements.txt

EXPOSE 8000
