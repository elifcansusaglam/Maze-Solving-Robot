# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.10

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/enes/gym-gazebo/gym_gazebo/envs/installation/catkin_ws/src

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/enes/gym-gazebo/gym_gazebo/envs/installation/catkin_ws/build

# Include any dependencies generated for this target.
include ecl_core/ecl_utilities/src/test/CMakeFiles/test_singleton.dir/depend.make

# Include the progress variables for this target.
include ecl_core/ecl_utilities/src/test/CMakeFiles/test_singleton.dir/progress.make

# Include the compile flags for this target's objects.
include ecl_core/ecl_utilities/src/test/CMakeFiles/test_singleton.dir/flags.make

ecl_core/ecl_utilities/src/test/CMakeFiles/test_singleton.dir/singleton.cpp.o: ecl_core/ecl_utilities/src/test/CMakeFiles/test_singleton.dir/flags.make
ecl_core/ecl_utilities/src/test/CMakeFiles/test_singleton.dir/singleton.cpp.o: /home/enes/gym-gazebo/gym_gazebo/envs/installation/catkin_ws/src/ecl_core/ecl_utilities/src/test/singleton.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/enes/gym-gazebo/gym_gazebo/envs/installation/catkin_ws/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object ecl_core/ecl_utilities/src/test/CMakeFiles/test_singleton.dir/singleton.cpp.o"
	cd /home/enes/gym-gazebo/gym_gazebo/envs/installation/catkin_ws/build/ecl_core/ecl_utilities/src/test && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/test_singleton.dir/singleton.cpp.o -c /home/enes/gym-gazebo/gym_gazebo/envs/installation/catkin_ws/src/ecl_core/ecl_utilities/src/test/singleton.cpp

ecl_core/ecl_utilities/src/test/CMakeFiles/test_singleton.dir/singleton.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/test_singleton.dir/singleton.cpp.i"
	cd /home/enes/gym-gazebo/gym_gazebo/envs/installation/catkin_ws/build/ecl_core/ecl_utilities/src/test && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/enes/gym-gazebo/gym_gazebo/envs/installation/catkin_ws/src/ecl_core/ecl_utilities/src/test/singleton.cpp > CMakeFiles/test_singleton.dir/singleton.cpp.i

ecl_core/ecl_utilities/src/test/CMakeFiles/test_singleton.dir/singleton.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/test_singleton.dir/singleton.cpp.s"
	cd /home/enes/gym-gazebo/gym_gazebo/envs/installation/catkin_ws/build/ecl_core/ecl_utilities/src/test && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/enes/gym-gazebo/gym_gazebo/envs/installation/catkin_ws/src/ecl_core/ecl_utilities/src/test/singleton.cpp -o CMakeFiles/test_singleton.dir/singleton.cpp.s

ecl_core/ecl_utilities/src/test/CMakeFiles/test_singleton.dir/singleton.cpp.o.requires:

.PHONY : ecl_core/ecl_utilities/src/test/CMakeFiles/test_singleton.dir/singleton.cpp.o.requires

ecl_core/ecl_utilities/src/test/CMakeFiles/test_singleton.dir/singleton.cpp.o.provides: ecl_core/ecl_utilities/src/test/CMakeFiles/test_singleton.dir/singleton.cpp.o.requires
	$(MAKE) -f ecl_core/ecl_utilities/src/test/CMakeFiles/test_singleton.dir/build.make ecl_core/ecl_utilities/src/test/CMakeFiles/test_singleton.dir/singleton.cpp.o.provides.build
.PHONY : ecl_core/ecl_utilities/src/test/CMakeFiles/test_singleton.dir/singleton.cpp.o.provides

ecl_core/ecl_utilities/src/test/CMakeFiles/test_singleton.dir/singleton.cpp.o.provides.build: ecl_core/ecl_utilities/src/test/CMakeFiles/test_singleton.dir/singleton.cpp.o


# Object files for target test_singleton
test_singleton_OBJECTS = \
"CMakeFiles/test_singleton.dir/singleton.cpp.o"

# External object files for target test_singleton
test_singleton_EXTERNAL_OBJECTS =

/home/enes/gym-gazebo/gym_gazebo/envs/installation/catkin_ws/devel/lib/ecl_utilities/test_singleton: ecl_core/ecl_utilities/src/test/CMakeFiles/test_singleton.dir/singleton.cpp.o
/home/enes/gym-gazebo/gym_gazebo/envs/installation/catkin_ws/devel/lib/ecl_utilities/test_singleton: ecl_core/ecl_utilities/src/test/CMakeFiles/test_singleton.dir/build.make
/home/enes/gym-gazebo/gym_gazebo/envs/installation/catkin_ws/devel/lib/ecl_utilities/test_singleton: gtest/googlemock/gtest/libgtest.so
/home/enes/gym-gazebo/gym_gazebo/envs/installation/catkin_ws/devel/lib/ecl_utilities/test_singleton: ecl_core/ecl_utilities/src/test/CMakeFiles/test_singleton.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/enes/gym-gazebo/gym_gazebo/envs/installation/catkin_ws/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable /home/enes/gym-gazebo/gym_gazebo/envs/installation/catkin_ws/devel/lib/ecl_utilities/test_singleton"
	cd /home/enes/gym-gazebo/gym_gazebo/envs/installation/catkin_ws/build/ecl_core/ecl_utilities/src/test && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/test_singleton.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
ecl_core/ecl_utilities/src/test/CMakeFiles/test_singleton.dir/build: /home/enes/gym-gazebo/gym_gazebo/envs/installation/catkin_ws/devel/lib/ecl_utilities/test_singleton

.PHONY : ecl_core/ecl_utilities/src/test/CMakeFiles/test_singleton.dir/build

ecl_core/ecl_utilities/src/test/CMakeFiles/test_singleton.dir/requires: ecl_core/ecl_utilities/src/test/CMakeFiles/test_singleton.dir/singleton.cpp.o.requires

.PHONY : ecl_core/ecl_utilities/src/test/CMakeFiles/test_singleton.dir/requires

ecl_core/ecl_utilities/src/test/CMakeFiles/test_singleton.dir/clean:
	cd /home/enes/gym-gazebo/gym_gazebo/envs/installation/catkin_ws/build/ecl_core/ecl_utilities/src/test && $(CMAKE_COMMAND) -P CMakeFiles/test_singleton.dir/cmake_clean.cmake
.PHONY : ecl_core/ecl_utilities/src/test/CMakeFiles/test_singleton.dir/clean

ecl_core/ecl_utilities/src/test/CMakeFiles/test_singleton.dir/depend:
	cd /home/enes/gym-gazebo/gym_gazebo/envs/installation/catkin_ws/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/enes/gym-gazebo/gym_gazebo/envs/installation/catkin_ws/src /home/enes/gym-gazebo/gym_gazebo/envs/installation/catkin_ws/src/ecl_core/ecl_utilities/src/test /home/enes/gym-gazebo/gym_gazebo/envs/installation/catkin_ws/build /home/enes/gym-gazebo/gym_gazebo/envs/installation/catkin_ws/build/ecl_core/ecl_utilities/src/test /home/enes/gym-gazebo/gym_gazebo/envs/installation/catkin_ws/build/ecl_core/ecl_utilities/src/test/CMakeFiles/test_singleton.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : ecl_core/ecl_utilities/src/test/CMakeFiles/test_singleton.dir/depend

