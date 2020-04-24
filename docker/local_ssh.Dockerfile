FROM ubuntu:latest
MAINTAINER P Puczka 'p.puczka@gmail.com'
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
RUN apt-get update && apt-get install -y supervisor
RUN apt-get update && apt-get install -y supervisor openssh-server
RUN mkdir /run/sshd
RUN echo "root:Docker" | chpasswd
COPY . /app
COPY sshd_config /etc/ssh/
EXPOSE 2222 5555
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["/usr/bin/supervisord", "-c", "/app/supervisord.conf"]