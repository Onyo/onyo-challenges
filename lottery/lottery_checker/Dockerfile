FROM python:3.5

MAINTAINER Cássio Botaro <cassiobotaro@gmail.com>

RUN apt-get update
RUN apt-get install -y python python-dev python-pip
RUN pip2 install supervisor

ADD . /bob
ADD supervisord.conf /etc/supervisor/conf.d/bob.conf

WORKDIR /bob

RUN pip3 install -r requirements.txt
RUN ./manage.py migrate
RUN ./manage.py collectstatic --no-input

RUN mkdir logs
RUN touch logs/supervisor.log

EXPOSE 8001

CMD ["supervisord"]
