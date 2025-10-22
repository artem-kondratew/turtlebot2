ARG BASE_IMAGE=althack/ros2:humble-full
FROM ${BASE_IMAGE}

# workspace setup

ENV ROS_DISTRO=humble
ENV WS="/workspace"

RUN echo '\
if [ -f "/opt/ros/${ROS_DISTRO}/setup.bash" ]; then\n\
    source "/opt/ros/${ROS_DISTRO}/setup.bash"\n\
fi\n\
if [ -f "${WS}/install/setup.bash" ]; then\n\
    source "${WS}/install/setup.bash"\n\
    cd "${WS}"\n\
fi\n\
alias s=". ./install/setup.bash"\n\
alias l="clear"' >> /root/.bashrc

# Install ROS pkgs 

RUN DEBIAN_FRONTEND=noninteractive apt update -y

RUN DEBIAN_FRONTEND=noninteractive apt install -y iproute2 net-tools iputils-ping
RUN DEBIAN_FRONTEND=noninteractive apt install -y python3-pip python3-venv
RUN DEBIAN_FRONTEND=noninteractive apt install -y vim nano

RUN DEBIAN_FRONTEND=noninteractive apt install -y libgtk2.0-dev libgtk-3-dev

RUN python3 -m pip install setuptools==58.2.0

RUN DEBIAN_FRONTEND=noninteractive apt install -y python3-colcon-common-extensions
RUN DEBIAN_FRONTEND=noninteractive apt install -y ros-${ROS_DISTRO}-rmw-cyclonedds-cpp
RUN DEBIAN_FRONTEND=noninteractive apt install -y ros-${ROS_DISTRO}-ecl-*

#RUN DEBIAN_FRONTEND=noninteractive apt install -y ros-${ROS_DISTRO}-slam-toolbox
#RUN DEBIAN_FRONTEND=noninteractive apt install -y ros-${ROS_DISTRO}-navigation2 ros-${ROS_DISTRO}-nav2-bringup
#RUN DEBIAN_FRONTEND=noninteractive apt install -y ros-${ROS_DISTRO}-domain-bridge

#RUN DEBIAN_FRONTEND=noninteractive apt install -y ros-${ROS_DISTRO}-librealsense2*
#RUN DEBIAN_FRONTEND=noninteractive apt install -y ros-${ROS_DISTRO}-realsense2-*
