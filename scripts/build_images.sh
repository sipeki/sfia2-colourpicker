#!/bin/bash
    
    # List the current images before building
    echo $(docker images)
    
    # Build service_1 image then push to docker hub
    docker build --no-cache -t sipeki/service_1 ./Service_1
    docker push sipeki/service_1:latest

    # Build service_2 image then push to docker hub
    docker build --no-cache -t sipeki/service_2 ./Service_2
    docker push sipeki/service_2:latest

    # Build service_3 image then push to docker hub
    docker build --no-cache  -t sipeki/service_3 ./Service_3
    docker push sipeki/service_3:latest


    # Build service_4 image then push to docker hub
    docker build --no-cache  -t sipeki/service_4 ./Service_4
    docker push sipeki/service_4:latest

    # List images after building
    echo $(docker images)
