from launch import LaunchDescriptioin
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescriptioin([
        Node(
            package='demo_nodes_py'
            executable='talker'
        )
    ])