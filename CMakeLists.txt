cmake_minimum_required(VERSION 3.10)
project(CoMusic)
  
find_package(pybind11 REQUIRED)
include_directories(${PYBIND11_INCLUDE_DIR})

set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${PROJECT_SOURCE_DIR})
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${PROJECT_SOURCE_DIR})

file(GLOB_RECURSE VideoList-src ${PROJECT_SOURCE_DIR}/VideoList/*)
pybind11_add_module(VideoList ${VideoList-src})
