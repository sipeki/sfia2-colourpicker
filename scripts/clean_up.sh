#!/bin/bash

    # remove orphaned containers and services

    docker system prune -f

    
# Deletes orphaned images

docker rmi $(docker images -f "dangling=true" -q)