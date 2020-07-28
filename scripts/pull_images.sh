#!/bin/bash

# Pulls the the images built on Docker Hub
# Remember to connect Github with Docker Hub and setup build.

docker pull sipeki/service_1
docker pull sipeki/service_2
docker pull sipeki/service_3
docker pull sipeki/service_4

# Deletes orphaned images

docker rmi $(docker images -f "dangling=true" -q)