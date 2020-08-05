#!/bin/bash

docker build --no-cache -t sipeki/nginx ./nginx
docker push sipeki/nginx:latest