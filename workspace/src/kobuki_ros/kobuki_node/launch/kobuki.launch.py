import os

import ament_index_python.packages
import launch
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

import yaml


def generate_launch_description():

    share_dir = ament_index_python.packages.get_package_share_directory('kobuki_node')
    params_file = os.path.join(share_dir, 'config', 'kobuki_node_params.yaml')
    with open(params_file, 'r') as f:
        params = yaml.safe_load(f)['kobuki_ros_node']['ros__parameters']

    kobuki_ros_node = Node(package='kobuki_node',
                           executable='kobuki_ros_node',
                           output='screen',
                           parameters=[params])
    
    base_footprint_transform = Node(
        package='tf2_ros',
        executable='static_transform_publisher',
        name='base_footprint_static_tf',
        arguments=[
            '0.0',
            '0.0',
            '0.0',
            '0.0',
            '0.0',
            '0.0',
            'base_link',
            'base_footprint'
        ]
    )

    laser_transform = Node(
        package='tf2_ros',
        executable='static_transform_publisher',
        name='laser_static_tf',
        arguments=[
            '--x', '0.0',
            '--y', '0.0',
            '--z', '0.2',
            '--roll', '0.0',
            '--pitch', '0.0',
            '--yaw', '0.0',
            '--frame-id', 'base_footprint',
            '--child-frame-id', 'laser'
        ]
    )

    lidar = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            [os.path.join(get_package_share_directory('urg_node2'), 'launch', 'urg_node2.launch.py')]
        ),
    )    

    wrapper = Node(
        package='cmd_vel_wrapper',
        executable='cmd_vel_wrapper',
        name='cmd_vel_wrapper',
    )

    return launch.LaunchDescription([kobuki_ros_node, base_footprint_transform, laser_transform, wrapper])
