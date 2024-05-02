from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os


def generate_launch_description():
    ld = LaunchDescription()

    # tag_pose_config_yaml_file = os.path.join(
    #     get_package_share_directory('localization_system_april'),
    #     'config',
    #     'tag_pose.yaml'
    # )

    # config = os.path.join(
    #     get_package_share_directory('localization_system_april'),
    #     'tag_pose.yaml'
    # )
    
    tag_pose = Node(
        package='localization_system_april',
        executable='static_tf_node',
        name='static_tf_node',
        output='screen',
        # parameters=[config]
    )

    ld.add_action(tag_pose)

    return ld
