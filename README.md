# turtlebot3_lama_ros2

## Build

```
$ mkdir -p ~/catkin_ws/src
$ cd ~/catkin_ws/src
$ git clone https://github.com/iris-ua/iris_lama
$ git clone https://github.com/iris-ua/iris_lama_ros -b dashing-devel
$ git clone https://github.com/atinfinity/turtlebot3_lama_ros2 -b dashing-devel
$ cd ..
$ colcon build
```

## Mapping
### Launch Gazebo

```
$ ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
```

### Launch LaMa ROS for Mapping

```
$ ros2 launch turtlebot3_lama_slam turtlebot3_pf_slam2d_launch.py
```

### Launch Teleop

```
$ ros2 run turtlebot3_teleop teleop_keyboard
```

### Save Map

```
$ mkdir ~/maps
$ ros2 run nav2_map_server map_saver -f ~/maps/world_map
```

