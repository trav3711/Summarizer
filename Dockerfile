FROM python:3.6.5-alpine

RUN pip install --upgrade pip && pip install --upgrade setuptools 
RUN apk update && apk upgrade
RUN apk add gcc && apk add python-dev && apk add build-base

RUN apk update && \
    apk add py-pip && \
    pip install --upgrade pip

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN python3 -m pip install -r requirements.txt

COPY . /app

EXPOSE 5050

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]
