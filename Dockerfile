FROM ubuntu:latest
MAINTAINER P Puczka 'p.puczka@gmail.com'
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
RUN apk add openssh \ && echo "root:Docker!" | chpasswd
COPY sshd_config /etc/ssh/
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 80 2222
ENTRYPOINT ["python"]
CMD ["ca_server_app.py"]
