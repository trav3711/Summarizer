FROM python:3.6.5-alpine

RUN pip install --upgrade pip && pip install --upgrade setuptools
RUN apk update && apk upgrade
RUN apk add gcc && apk add python-dev && apk add build-base

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN python3 -m pip install -r requirements.txt

COPY . /app

CMD gunicorn -w 4 -bind 0.0.0.0:8003 /app/wsgi --reload
