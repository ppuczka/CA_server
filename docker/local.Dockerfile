FROM ubuntu:latest
MAINTAINER P Puczka 'p.puczka@gmail.com'
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
RUN apt-get update && apt-get install -y supervisor
RUN apt-get update && apt-get install -y supervisor openssh-client
COPY sshd_config /etc/ssh/
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["/usr/bin/supervisord", "-c", "/ca_server/supervisord.conf"]