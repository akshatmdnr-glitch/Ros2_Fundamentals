from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():

    return LaunchDescription([

        Node(
            package='parameter_demo',
            executable='parameter_node',
            name='parameter_node',
            output='screen',

            parameters=[
                {
                    'message': 'Started From Launch File'
                }
            ]
        ),

        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='turtle',
            output='screen'
        )

    ])