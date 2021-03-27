FROM python:alpine3.7
MAINTAINER Travis Welch "travi.cwelch@gmail.com"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5050
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]
