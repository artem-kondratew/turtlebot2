import os

import ament_index_python.packages
import launch
from launch_ros.actions import Node

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

    base_footprint_transform = Node(
        package='cmd_vel_wrapper',
        executable='cmd_vel_wrapper',
        name='cmd_vel_wrapper',
    )

    return launch.LaunchDescription([kobuki_ros_node, base_footprint_transform])
