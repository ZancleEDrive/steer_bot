cmake_minimum_required(VERSION 2.8.3)
project(steer_bot_gazebo)

find_package(catkin REQUIRED roslaunch)

catkin_package()

install(DIRECTORY launch
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

if (CATKIN_ENABLE_TESTING)
    roslaunch_add_file_check(launch)
endif()


## Mark executable scripts (Python etc.) for installation
## in contrast to setup.py, you can choose the destination
 catkin_install_python(PROGRAMS
   src/chronometer.py
   DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
 )
 catkin_install_python(PROGRAMS
   src/camera.py
   DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
 )