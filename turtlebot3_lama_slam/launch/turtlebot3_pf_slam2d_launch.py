import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
import launch
import launch.actions

def generate_launch_description():
    use_sim_time = launch.substitutions.LaunchConfiguration('use_sim_time', default='True')
    parameters_file_path= os.path.join(get_package_share_directory('turtlebot3_lama_slam'), 'config', 'live.yaml')
    rviz_config_dir = os.path.join(get_package_share_directory('turtlebot3_lama_slam'), 'rviz', 'turtlebot3_lama_slam.rviz')

    return LaunchDescription([
        launch.actions.DeclareLaunchArgument('use_sim_time', default_value='True',description='Use simulation (Gazebo) clock if True'),
        launch.actions.DeclareLaunchArgument('global_frame_id',  default_value="map", description='The frame attached to the map'),
        launch.actions.DeclareLaunchArgument('odom_frame_id',  default_value="odom", description='The frame attached to the odometry system'),
        launch.actions.DeclareLaunchArgument('base_frame_id',  default_value="base_footprint", description='The frame attached to the mobile base'),

        Node(
            package='iris_lama_ros2',
            node_namespace='iris_lama_ros2',
            node_executable='pf_slam2d_ros',
            node_name='pf_slam2d_ros',
            parameters=[parameters_file_path],
            output='screen',
        ),
        Node(
            package='rviz2',
            node_executable='rviz2',
            node_name='rviz2',
            arguments=['-d', rviz_config_dir],
            parameters=[{'use_sim_time': use_sim_time}],
            output='screen'),
    ])
