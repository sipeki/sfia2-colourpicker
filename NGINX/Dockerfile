FROM nginx:latest

WORKDIR /etc/nginx/

RUN apt update -y

RUN rm conf.d/default.conf
RUN rm conf.d/reverse_proxy.conf
RUN COPY reverse_proxy.conf conf.d/