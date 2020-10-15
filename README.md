# turtle_move

## Overview

This package is used to move the turtlesim in a straight line, choosing the speed, distance and direction, with ROS2.

**Keywords:** move, line, turtle, ROS2.

### License

**Author: Mariana Mota<br />
Affiliation: Senai CIMATEC <br />
Maintainer: Mariana Mota, marivboas02@gmail.com**

The turtle_move package has been tested under [ROS2] Foxy on Ubuntu 20.04.

## Installation

### Building

To build from source, clone the latest version from this repository into your workspace and compile the package using

	cd <your_workspace>/src
	git clone "https://github.com/Marimvboas/turtle_move"
	cd ../
	rosdep install -i --from-path src --rosdistro <distro> -y
	colcon build

## Usage

Run the turtlesim node with

    source /opt/ros/<distro>/setup.bash
	ros2 run turtlesim turtlesim_node

In another shell, run the main node with

    cd <your_workspace>/
    source /opt/ros/<distro>/setup.bash
    . install/setup.bash
	ros2 run turtle_move moving

## Nodes

### turtle_move

The user inputs the speed, distance and direction (1 - forward and 0 - backward) for move the turtle.

#### Published Topics

* **`/turtle1/cmd_vel`** ([geometry_msgs/Twist])

	The velocity is send to move the turtle.

## Bugs & Feature Requests

Please report bugs and request features using the [Issue Tracker](https://github.com/Marimvboas/turtle_move/issues).


[ROS2]: https://index.ros.org/doc/ros2/
[geometry_msgs/Twist]: https://github.com/ros2/common_interfaces/blob/master/geometry_msgs/msg/Twist.msg