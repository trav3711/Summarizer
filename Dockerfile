FROM python:alpine3.7
MAINTAINER Travis Welch "travi.cwelch@gmail.com"

RUN apt-get update -y && apt-get install apt-file -y && apt-file update -y && apt-get install -y python3-dev build-essential

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5050
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]
