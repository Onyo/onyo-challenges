FROM python:3.5

MAINTAINER Cássio Botaro <cassiobotaro@gmail.com>

RUN apt-get update
RUN apt-get install -y python python-dev python-pip
RUN pip2 install supervisor

ADD . /ana
ADD supervisord.conf /etc/supervisor/conf.d/ana.conf

WORKDIR /ana

RUN pip3 install -r requirements.txt
RUN ./manage.py migrate
RUN ./manage.py collectstatic --no-input

RUN mkdir logs
RUN touch logs/supervisor.log

EXPOSE 8000

CMD ["supervisord"]
