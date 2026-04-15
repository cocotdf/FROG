cmake_minimum_required(VERSION 3.20)

project(frog_runtime_cpp_example05 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

add_executable(frog_runtime_cpp_example05
    src/main.cpp
)

target_include_directories(frog_runtime_cpp_example05
    PRIVATE
        ${CMAKE_CURRENT_SOURCE_DIR}/include
)

if(MSVC)
    target_compile_options(frog_runtime_cpp_example05 PRIVATE /W4)
else()
    target_compile_options(frog_runtime_cpp_example05 PRIVATE -Wall -Wextra -Wpedantic)
endif()
