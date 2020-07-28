# Created the micro service stack if no sfia2 service stack exists
if [[ "$(docker stack services sfia2 2> /dev/null)" == "" ]]; then
    docker stack deploy --compose-file docker-compose.yml sfia2

fi