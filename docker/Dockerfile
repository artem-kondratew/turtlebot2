ARG base_img

FROM ${base_img}

# workspace setup

ENV WS /workspace

RUN echo "source ${WS}/install/setup.bash" >> ~/.bashrc
RUN echo "cd /workspace" >> ~/.bashrc
RUN echo "alias s=\". install/setup.bash\"" >> ~/.bashrc
RUN echo "alias l=clear" >> ~/.bashrc

# ROS setup

ENV ROS_DISTRO galactic

# Install ROS pkgs 

RUN DEBIAN_FRONTEND=noninteractive apt update -y

RUN DEBIAN_FRONTEND=noninteractive apt install -y htop vim python3-pip python3-venv nano

RUN DEBIAN_FRONTEND=noninteractive apt install -y libgtk2.0-dev libgtk-3-dev
RUN DEBIAN_FRONTEND=noninteractive apt install -y python3-colcon-common-extensions

RUN DEBIAN_FRONTEND=noninteractive apt install -y ros-${ROS_DISTRO}-slam-toolbox
RUN DEBIAN_FRONTEND=noninteractive apt install -y ros-${ROS_DISTRO}-navigation2 ros-${ROS_DISTRO}-nav2-bringup
RUN DEBIAN_FRONTEND=noninteractive apt install -y ros-${ROS_DISTRO}-domain-bridge

RUN DEBIAN_FRONTEND=noninteractive apt install -y ros-${ROS_DISTRO}-librealsense2*
RUN DEBIAN_FRONTEND=noninteractive apt install -y ros-${ROS_DISTRO}-realsense2-*
