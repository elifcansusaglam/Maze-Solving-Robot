# generated from catkin/cmake/template/pkg.context.pc.in
CATKIN_PACKAGE_PREFIX = ""
PROJECT_PKG_CONFIG_INCLUDE_DIRS = "${prefix}/include;/usr/include/eigen3;/opt/ros/melodic/include".split(';') if "${prefix}/include;/usr/include/eigen3;/opt/ros/melodic/include" != "" else []
PROJECT_CATKIN_DEPENDS = "ecl_build;ecl_eigen;ecl_exceptions;ecl_formatters;ecl_math".replace(';', ' ')
PKG_CONFIG_LIBRARIES_WITH_PREFIX = "-lecl_linear_algebra".split(';') if "-lecl_linear_algebra" != "" else []
PROJECT_NAME = "ecl_linear_algebra"
PROJECT_SPACE_DIR = "/home/enes/gym-gazebo/gym_gazebo/envs/installation/catkin_ws/install"
PROJECT_VERSION = "0.62.2"
