# Install script for directory: /home/enes/gym-gazebo/gym_gazebo/envs/installation/catkin_ws/src/ecl_core/ecl_exceptions

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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/enes/gym-gazebo/gym_gazebo/envs/installation/catkin_ws/build/ecl_core/ecl_exceptions/catkin_generated/installspace/ecl_exceptions.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/ecl_exceptions/cmake" TYPE FILE FILES
    "/home/enes/gym-gazebo/gym_gazebo/envs/installation/catkin_ws/build/ecl_core/ecl_exceptions/catkin_generated/installspace/ecl_exceptionsConfig.cmake"
    "/home/enes/gym-gazebo/gym_gazebo/envs/installation/catkin_ws/build/ecl_core/ecl_exceptions/catkin_generated/installspace/ecl_exceptionsConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/ecl_exceptions" TYPE FILE FILES "/home/enes/gym-gazebo/gym_gazebo/envs/installation/catkin_ws/src/ecl_core/ecl_exceptions/package.xml")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for each subdirectory.
  include("/home/enes/gym-gazebo/gym_gazebo/envs/installation/catkin_ws/build/ecl_core/ecl_exceptions/include/cmake_install.cmake")
  include("/home/enes/gym-gazebo/gym_gazebo/envs/installation/catkin_ws/build/ecl_core/ecl_exceptions/src/cmake_install.cmake")

endif()

