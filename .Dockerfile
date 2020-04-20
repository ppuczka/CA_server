#for testing pupose only
FROM ubuntu:latest
MAINTAINER P Puczka 'p.puczka@gmail.com'
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app
EXPOSE 80 5000
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["ca_server_app.py"]