#!/usr/bin/env python3

import os
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch_ros.actions import Node
from ament_index_python import get_package_share_directory
from launch_ros.substitutions import FindPackageShare
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution

def generate_launch_description():
    ld = LaunchDescription()

    # Add launch arguments for your nodes
    headless = DeclareLaunchArgument('headless', default_value='0')
    gz_world = DeclareLaunchArgument('gz_world', default_value='tag')
    xpos = DeclareLaunchArgument('xpos', default_value='0.0')
    ypos = DeclareLaunchArgument('ypos', default_value='0.0')
    zpos = DeclareLaunchArgument('zpos', default_value='0.1')

    ld.add_action(headless)
    ld.add_action(gz_world)
    ld.add_action(xpos)
    ld.add_action(ypos)
    ld.add_action(zpos)

    # Node for Drone 1
    # Node for Drone 1
    gz_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                FindPackageShare('localization_system_april').find('localization_system_april'),
                'gz_loc.launch.py'
            )
        ),
        launch_arguments={
            'headless': headless,
            'gz_world': gz_world,
            'xpos': xpos,
            'ypos': ypos,
            'zpos': zpos
        }
    )



    ld.add_action(gz_launch)

    return ld
