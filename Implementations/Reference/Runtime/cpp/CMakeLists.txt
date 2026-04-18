cmake_minimum_required(VERSION 3.20)

project(frog_runtime_cpp_example05 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

get_filename_component(FROG_REPO_ROOT "${CMAKE_CURRENT_SOURCE_DIR}/../../../.." ABSOLUTE)
set(FROG_EXAMPLE05_CONTRACT "${FROG_REPO_ROOT}/Implementations/Reference/ContractEmitter/examples/05_bounded_ui_accumulator.reference_host_runtime_ui_binding.contract.json")
string(REPLACE "\\" "\\\\" FROG_EXAMPLE05_CONTRACT_ESCAPED "${FROG_EXAMPLE05_CONTRACT}")

add_executable(frog_runtime_cpp_example05
    src/main.cpp
)

target_include_directories(frog_runtime_cpp_example05
    PRIVATE
        ${CMAKE_CURRENT_SOURCE_DIR}/include
)

target_compile_definitions(frog_runtime_cpp_example05
    PRIVATE
        FROG_EXAMPLE05_CONTRACT_PATH="${FROG_EXAMPLE05_CONTRACT_ESCAPED}"
)

if(MSVC)
    target_compile_options(frog_runtime_cpp_example05 PRIVATE /W4)
else()
    target_compile_options(frog_runtime_cpp_example05 PRIVATE -Wall -Wextra -Wpedantic)
endif()
