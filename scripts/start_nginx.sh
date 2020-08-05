#!/bin/bash

docker build --no-cache -t sipeki/nginx ./NGINX
docker push sipeki/nginx:latest