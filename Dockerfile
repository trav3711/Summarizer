FROM ubuntu:16.04

RUN apt-get update -y && apt-get install apt-file -y && apt-file update -y && apt-get install -y python3-dev build-essential

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 5050

COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]
