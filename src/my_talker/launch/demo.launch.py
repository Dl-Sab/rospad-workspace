from launch import LaunchDescription            # container that groups launch actions
from launch_ros.actions import Node             # action that starts one ROS 2 node


def generate_launch_description():              # ros2 launch calls this function
    return LaunchDescription([
        Node(package='my_talker', executable='my_node', name='talker'),    # start the talker
        Node(package='my_talker', executable='listener', name='listener'),  # start the listener
    ])