cmake_minimum_required(VERSION 3.10)
project(CoMusic)

add_subdirectory(submod)

include_directories(${PYBIND11_INCLUDE_DIR})

set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${PROJECT_SOURCE_DIR})
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${PROJECT_SOURCE_DIR})
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${PROJECT_SOURCE_DIR})

file(GLOB_RECURSE VideoList-src ${PROJECT_SOURCE_DIR}/VideoList/*)
pybind11_add_module(VideoList ${VideoList-src})

if(WIN32)
	set(SRC ${PROJECT_SOURCE_DIR}/Debug)
	set(DEST ${PROJECT_SOURCE_DIR})
endif()
