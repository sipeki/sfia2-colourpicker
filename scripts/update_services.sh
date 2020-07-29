#!/bin/bash    
    
    # Update images in the stack

    docker service update --image sipeki/service_1:latest --force sfia2_Service_1
    docker service update --image sipeki/service_2:latest --force sfia2_Service_2
    docker service update --image sipeki/service_3:latest --force sfia2_Service_3
    docker service update --image sipeki/service_4:latest --force sfia2_Service_4
    
    # remove orphaned containers and services

    docker system prune -f
