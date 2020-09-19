# turtlebot3_lama_ros2

## Introduction
This is a package to use [iris_lama_ros](https://github.com/iris-ua/iris_lama_ros) with TurtleBot3(Gazebo).

## Requirements

- ROS 2 Dashing

## Preparation
```
$ sudo apt-get install ros-dashing-turtlebot3-bringup ros-dashing-turtlebot3-cartographer ros-dashing-turtlebot3-gazebo ros-dashing-turtlebot3-msgs ros-dashing-turtlebot3-navigation2 ros-dashing-turtlebot3-simulations ros-dashing-turtlebot3-teleop
```

And, please add the following description to `.bashrc`.

```
export TURTLEBOT3_MODEL=waffle
export GAZEBO_MODEL_PATH=$GAZEBO_MODEL_PATH:/opt/ros/dashing/share/turtlebot3_gazebo/models
```

## Build

```
$ mkdir -p ~/catkin_ws/src
$ cd ~/catkin_ws/src
$ git clone https://github.com/iris-ua/iris_lama.git
$ git clone https://github.com/iris-ua/iris_lama_ros.git -b dashing-devel
$ git clone https://github.com/atinfinity/turtlebot3_lama_ros2.git -b dashing-devel
```

And, I uncomment the following lines to avoid problem referencing [this comment](https://github.com/iris-ua/iris_lama_ros/blob/e4a229b637e0d9a13148680cfc8a9184d8994051/start.sh#L32-L34).  
<https://github.com/iris-ua/iris_lama_ros/blob/e4a229b637e0d9a13148680cfc8a9184d8994051/src/loc2d_ros.cpp#L328-L333>

```
$ cd ~/catkin_ws
$ colcon build
$ source install/setup.bash
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

## Localization
### Launch Gazebo

```
$ ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
```

### Launch LaMa ROS for Localization

```
$ ros2 launch turtlebot3_lama_localization turtlebot3_lama_loc2d_launch.py
```

### Launch Teleop

```
$ ros2 run turtlebot3_teleop teleop_keyboard
```

## Navigation
### Launch Gazebo

```
$ ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
```

### Launch LaMa ROS for Navigation

```
$ ros2 launch turtlebot3_lama_navigation turtlebot3_lama_navigation.py
```
