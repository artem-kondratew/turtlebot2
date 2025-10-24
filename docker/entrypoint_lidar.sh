#!/bin/bash
set -e

cd /workspace

source /opt/ros/$ROS_DISTRO/setup.bash

if [ -f "/workspace/install/setup.bash" ]; then
    source /workspace/install/setup.bash
    ros2 launch urg_node2 urg_node2.launch.py
fi

exec bash
