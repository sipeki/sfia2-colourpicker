#!/bin/bash

docker run -d -p 80:80 --name nginx nginx
sudo docker cp NGINX/reverse_proxy.conf nginx:/etc/nginx/conf.d/
sudo docker exec -it nginx /etc/init.d/nginx reload