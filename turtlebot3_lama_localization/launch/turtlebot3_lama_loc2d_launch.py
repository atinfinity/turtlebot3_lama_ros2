import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
import launch
import launch.actions

def generate_launch_description():
    use_sim_time = launch.substitutions.LaunchConfiguration('use_sim_time', default='True')
    parameters_file_path = os.path.join(get_package_share_directory('turtlebot3_lama_localization'), 'config', 'live.yaml')
    map_file_path = os.path.join(get_package_share_directory('turtlebot3_lama_localization'), 'maps', 'map.yaml')
    rviz_config_dir = os.path.join(get_package_share_directory('nav2_bringup'), 'launch', 'nav2_default_view.rviz')

    return LaunchDescription([
        launch.actions.DeclareLaunchArgument('use_sim_time', default_value='True', description='Use simulation (Gazebo) clock if True'),
        launch.actions.DeclareLaunchArgument('global_frame_id', default_value="map", description='The frame attached to the map'),
        launch.actions.DeclareLaunchArgument('odom_frame_id', default_value="odom", description='The frame attached to the odometry system'),
        launch.actions.DeclareLaunchArgument('base_frame_id', default_value="base_footprint", description='The frame attached to the mobile base'),
        launch.actions.DeclareLaunchArgument('scan_topic', default_value="scan", description='Laser scan topic to subscribe'),
        launch.actions.DeclareLaunchArgument('initial_pose_x', default_value="0.0", description='Initial x position'),
        launch.actions.DeclareLaunchArgument('initial_pose_y', default_value="0.0", description='Initial y position'),
        launch.actions.DeclareLaunchArgument('initial_pose_a', default_value="0.0", description='Initial rotation (or angle)'),

        Node(
            package='iris_lama_ros2',
            node_namespace='iris_lama_ros2',
            node_executable='loc2d_ros',
            node_name='loc2d_ros',
            parameters=[parameters_file_path],
            output='screen',
        ),
        Node(
            package='nav2_map_server',
            node_executable='map_server',
            node_name='map_server',
            parameters=[{'use_sim_time': use_sim_time}, 
                        {'yaml_filename': map_file_path}],
            output='screen',
        ),
        Node(
            package='nav2_lifecycle_manager',
            node_executable='lifecycle_manager',
            node_name='lifecycle_manager_localization',
            parameters=[{'use_sim_time': use_sim_time}, 
                        {'autostart': True},
                        {'node_names': ['map_server']}],
            output='screen',
        ),
        Node(
            package='rviz2',
            node_executable='rviz2',
            node_name='rviz2',
            arguments=['-d', rviz_config_dir],
            parameters=[{'use_sim_time': use_sim_time}],
            output='screen',
        ),
    ])
