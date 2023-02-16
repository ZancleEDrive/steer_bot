# Steer Bot

Simulate a simple Ackermann steering vehicle in Gazebo using `ros_control`
the `ackermann_steering_controller` and `steer_bot_hardware_gazebo`.

This was tested by the ZED team at UniMe on a Ubuntu 20.04 with ROS Noetic (installed with the one line installer).

## Installation

```bash
# Create a workspace folder
mkdir -p <catkin_ws>/src

# Clone the repo
cd <catkin_ws>/src
git clone https://github.com/ZancleEDrive/steer_bot

# Checkout a version of `steer_drive_ros` patched for ROS Melodic (but it also works for Noetic)
git clone https://github.com/ZancleEDrive/steer_drive_ros.git
cd steer_drive_ros
git checkout melodic-devel

#Install rosdep if not present
sudo apt install python3-rosdep

# Check dependencies
rosdep check --from-paths src --ignore-src --rosdistro noetic

# Install dependencies
rosdep install --from-paths src --ignore-src --rosdistro noetic -y

# Build
cd <catkin_ws>
catkin_make
```

## Run

Start the Gazebo simulation:

```bash
cd <catkin_ws>
source devel/setup.bash
roslaunch steer_bot_gazebo steer_bot_sim.launch
```

Start `rviz`:

```bash
roslaunch steer_bot_viz view_steer_bot_robot.launch
```

If all is working well you should see the robot in Gazebo and be able to
command it using `rqt_robot_steering`:

![steer_gazebo rviz](https://raw.githubusercontent.com/wiki/srmainwaring/steer_bot/images/steer_bot_gazebo.png)

The robot model and odometry can be monitored in `rviz`: 

![steer_bot rviz](https://raw.githubusercontent.com/wiki/srmainwaring/steer_bot/images/steer_bot_rviz.png)

## License

This software is licensed under the BSD-3-Clause license found in the
LICENSE file in the root directory of this source tree.
