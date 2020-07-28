#!/bin/bash


# Created the micro service stack if no sfia2 service stack exists
if [[ "$(docker stack services sfia2 2> /dev/null)" == "" ]]; then
    docker stack deploy --compose-file docker-compose.yml sfia2
else

    if [[ "$(docker stack services sfia2 -q --filter name=sfia2_Service_1 2> /dev/null)" == "" ]]; then
        docker service update --image sipeki/service_1:latest sfia2_Service_1
    fi

    if [[ "$(docker stack services sfia2 -q --filter name=sfia2_Service_2 2> /dev/null)" == "" ]]; then
        docker service update --image sipeki/service_2:latest sfia2_Service_2
    fi

    if [[ "$(docker stack services sfia2 -q --filter name=sfia2_Service_3 2> /dev/null)" == "" ]]; then
        docker service update --image sipeki/sfia2_Service_3:latest sfia2_Service_3
    fi

    if [[ "$(docker stack services sfia2 -q --filter name=sfia2_Service_4 2> /dev/null)" == "" ]]; then
        docker service update --image sipeki/sfia2_Service_4:latest sfia2_Service_4
    fi

fi

if [[ "$(docker stack services sfia2 -q --filter name=sfia2_Service_1 2> /dev/null)" == "" ]]; then
    docker service update --image sipeki/sfia2_Service_1:latest sfia2_Service_1
fi
