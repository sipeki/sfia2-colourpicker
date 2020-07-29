#!/bin/bash

# Build service_1 iamge if does not exits localy
if [[ "$(docker images -q sipeki/service_1:latest 2> /dev/null)" == "" ]]; then
    docker build -t sipeki/service_1 ./Service_1
    docker push sipeki/service_1
else
    docker pull sipeki/service_1
fi

# Build service_2 iamge if does not exits localy
if [[ "$(docker images -q sipeki/service_2:latest 2> /dev/null)" == "" ]]; then
    docker build -t sipeki/service_2 ./Service_2
    docker push sipeki/service_2
else
    docker pull sipeki/service_2
fi

# Build service_3 iamge if does not exits localy
if [[ "$(docker images -q sipeki/service_3:latest 2> /dev/null)" == "" ]]; then
    docker build -t sipeki/service_3 ./Service_3
    docker push sipeki/service_3
else
    docker pull sipeki/service_3
fi

# Build service_4 iamge if does not exits localy
if [[ "$(docker images -q sipeki/service_4:latest 2> /dev/null)" == "" ]]; then
    docker build -t sipeki/service_4 ./Service_4
    docker push sipeki/service_4
else
    docker pull sipeki/service_4
fi
