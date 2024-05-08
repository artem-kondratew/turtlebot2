#!/usr/bin/env bash


KOB_ROOT="$( cd "$( dirname "${BASH_SOURCE[0]}" )/.." && pwd )"

BASE_IMG="nickodema/hsl_2022_kobuki"

docker build -t "kobuki_ros" \
             -f $KOB_ROOT/docker/Dockerfile $KOB_ROOT \
            --network=host \
            --build-arg base_img=${BASE_IMG} \
            --build-arg workspace=${KOB_ROOT}/workspace
