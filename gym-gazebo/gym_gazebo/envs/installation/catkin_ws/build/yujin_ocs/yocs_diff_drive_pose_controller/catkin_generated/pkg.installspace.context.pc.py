# generated from catkin/cmake/template/pkg.context.pc.in
CATKIN_PACKAGE_PREFIX = ""
PROJECT_PKG_CONFIG_INCLUDE_DIRS = "${prefix}/include".split(';') if "${prefix}/include" != "" else []
PROJECT_CATKIN_DEPENDS = "ecl_threads;geometry_msgs;nodelet;pluginlib;roscpp;sensor_msgs;std_msgs;tf;yocs_controllers;yocs_math_toolkit".replace(';', ' ')
PKG_CONFIG_LIBRARIES_WITH_PREFIX = "-lyocs_diff_drive_pose_controller;-lyocs_diff_drive_pose_controller_nodelet".split(';') if "-lyocs_diff_drive_pose_controller;-lyocs_diff_drive_pose_controller_nodelet" != "" else []
PROJECT_NAME = "yocs_diff_drive_pose_controller"
PROJECT_SPACE_DIR = "/home/enes/gym-gazebo/gym_gazebo/envs/installation/catkin_ws/install"
PROJECT_VERSION = "0.8.2"
