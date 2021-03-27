FROM alpine:3.7

RUN apk update && \
    apk add py-pip && \
    pip install --upgrade pip

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

EXPOSE 5050

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]
