#!/bin/bash


KOB_ROOT="$( cd "$( dirname "${BASH_SOURCE[0]}" )/.." && pwd )"

xhost +local:docker > /dev/null || true

docker run  -d -ti --rm \
            -e "DISPLAY" \
            -e "QT_X11_NO_MITSHM=1" \
            -e XAUTHORITY \
            -v /tmp/.X11-unix:/tmp/.X11-unix:rw \
            -v /etc/localtime:/etc/localtime:ro \
            -v ${KOB_ROOT}/workspace:/workspace \
            -v /dev:/dev \
            --net=host \
            --privileged \
            --name "kobuki_ros" kobuki_ros \
            > /dev/null
