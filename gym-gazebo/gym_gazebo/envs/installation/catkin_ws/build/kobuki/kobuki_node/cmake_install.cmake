# Install script for directory: /home/enes/gym-gazebo/gym_gazebo/envs/installation/catkin_ws/src/kobuki/kobuki_node

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/enes/gym-gazebo/gym_gazebo/envs/installation/catkin_ws/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/enes/gym-gazebo/gym_gazebo/envs/installation/catkin_ws/build/kobuki/kobuki_node/catkin_generated/installspace/kobuki_node.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/kobuki_node/cmake" TYPE FILE FILES
    "/home/enes/gym-gazebo/gym_gazebo/envs/installation/catkin_ws/build/kobuki/kobuki_node/catkin_generated/installspace/kobuki_nodeConfig.cmake"
    "/home/enes/gym-gazebo/gym_gazebo/envs/installation/catkin_ws/build/kobuki/kobuki_node/catkin_generated/installspace/kobuki_nodeConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/kobuki_node" TYPE FILE FILES "/home/enes/gym-gazebo/gym_gazebo/envs/installation/catkin_ws/src/kobuki/kobuki_node/package.xml")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/kobuki_node" TYPE DIRECTORY FILES "/home/enes/gym-gazebo/gym_gazebo/envs/installation/catkin_ws/src/kobuki/kobuki_node/include/kobuki_node/")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/kobuki_node" TYPE DIRECTORY FILES "/home/enes/gym-gazebo/gym_gazebo/envs/installation/catkin_ws/src/kobuki/kobuki_node/plugins")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/kobuki_node" TYPE DIRECTORY FILES "/home/enes/gym-gazebo/gym_gazebo/envs/installation/catkin_ws/src/kobuki/kobuki_node/launch")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/kobuki_node" TYPE DIRECTORY FILES "/home/enes/gym-gazebo/gym_gazebo/envs/installation/catkin_ws/src/kobuki/kobuki_node/param")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/kobuki_node" TYPE DIRECTORY FILES "/home/enes/gym-gazebo/gym_gazebo/envs/installation/catkin_ws/src/kobuki/kobuki_node/image")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/kobuki_node" TYPE PROGRAM FILES
    "/home/enes/gym-gazebo/gym_gazebo/envs/installation/catkin_ws/src/kobuki/kobuki_node/scripts/getOdom2D.py"
    "/home/enes/gym-gazebo/gym_gazebo/envs/installation/catkin_ws/src/kobuki/kobuki_node/scripts/getYaw.py"
    )
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for each subdirectory.
  include("/home/enes/gym-gazebo/gym_gazebo/envs/installation/catkin_ws/build/kobuki/kobuki_node/src/cmake_install.cmake")

endif()

