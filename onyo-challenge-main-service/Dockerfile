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
RUN chmod +X start.sh
RUN ls -la