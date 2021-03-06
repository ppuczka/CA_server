FROM ubuntu:bionic
MAINTAINER P Puczka 'p.puczka@gmail.com'
ARG root_password
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
RUN apt-get install -y supervisor
RUN apt-get install -y supervisor openssh-server
RUN mkdir /run/sshd
RUN echo $root_password  | chpasswd
COPY . /app
COPY sshd_config /etc/ssh/
EXPOSE 80 2222 5555
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["/usr/bin/supervisord", "-c", "/app/supervisord.conf"]
