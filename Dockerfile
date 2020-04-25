FROM ubuntu:latest
MAINTAINER P Puczka 'p.puczka@gmail.com'
ARG root_password
RUN apt-get update
RUN apt-get install python3
RUN easy_install pip
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
