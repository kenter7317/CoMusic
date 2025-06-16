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
 	configure_file(${PROJECT_SOURCE_DIR}/a.ps1.in ${PROJECT_SOURCE_DIR}/a.ps1)
 
	add_custom_command(
		TARGET VideoList 
		POST_BUILD
		COMMAND powershell -File ${PROJECT_SOURCE_DIR}/a.ps1
  		COMMAND rm "./a.ps1"
		WORKING_DIRECTORY ${CMAKE_LIBRARY_OUTPUT_DIRECTORY}
	)
endif()
