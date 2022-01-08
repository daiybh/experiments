cmake_minimum_required(VERSION 3.17)

set(CMAKE_DEBUG_POSTFIX d)
project(experiments)

set(CMAKE_CXX_STANDARD 20)
#find_package(xaaa REQUIRED)
add_executable(experiments main.cpp)

add_library(hello "hello.cpp")

install(TARGETS hello DESTINATION lib)
install(FILES hello.h DESTINATION include)

install(TARGETS hello
EXPORT hello-targets 
ARCHIVE DESTINATION lib
LIBRARY DESTINATION lib
RUNTIME DESTINATION bin
)
install(EXPORT hello-targets
FILE helloConfig.cmake
FILE hello-config.cmake
DESTINATION cmake
)