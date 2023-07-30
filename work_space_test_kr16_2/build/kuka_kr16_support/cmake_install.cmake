# Install script for directory: /home/vayne/Documents/Curso_Robotica_ROS/work_space_test_kr16_2/src/kuka_kr16_support

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/vayne/Documents/Curso_Robotica_ROS/work_space_test_kr16_2/install")
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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/vayne/Documents/Curso_Robotica_ROS/work_space_test_kr16_2/build/kuka_kr16_support/catkin_generated/installspace/kuka_kr16_support.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/kuka_kr16_support/cmake" TYPE FILE FILES
    "/home/vayne/Documents/Curso_Robotica_ROS/work_space_test_kr16_2/build/kuka_kr16_support/catkin_generated/installspace/kuka_kr16_supportConfig.cmake"
    "/home/vayne/Documents/Curso_Robotica_ROS/work_space_test_kr16_2/build/kuka_kr16_support/catkin_generated/installspace/kuka_kr16_supportConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/kuka_kr16_support" TYPE FILE FILES "/home/vayne/Documents/Curso_Robotica_ROS/work_space_test_kr16_2/src/kuka_kr16_support/package.xml")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/kuka_kr16_support" TYPE DIRECTORY FILES
    "/home/vayne/Documents/Curso_Robotica_ROS/work_space_test_kr16_2/src/kuka_kr16_support/config"
    "/home/vayne/Documents/Curso_Robotica_ROS/work_space_test_kr16_2/src/kuka_kr16_support/launch"
    "/home/vayne/Documents/Curso_Robotica_ROS/work_space_test_kr16_2/src/kuka_kr16_support/meshes"
    "/home/vayne/Documents/Curso_Robotica_ROS/work_space_test_kr16_2/src/kuka_kr16_support/urdf"
    )
endif()

