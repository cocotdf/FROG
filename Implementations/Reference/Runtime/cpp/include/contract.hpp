#pragma once

#include <cstdint>
#include <optional>
#include <string>
#include <vector>

namespace frog::runtime::cpp_ref {

struct widget_binding {
    std::string widget_id;
    std::string role;
};

struct example05_contract {
    std::string backend_family;
    std::string example_id;
    std::uint16_t initial_state;
    std::uint16_t iterations;
    std::uint16_t input_value;
    std::uint16_t lower_bound;
    std::uint16_t upper_bound;
    std::vector<widget_binding> widgets;
};

struct expected_output {
    std::uint16_t final_state;
    std::uint16_t public_output;
    std::string property_member;
};

std::optional<example05_contract> build_example05_contract(std::uint16_t input_value);
std::optional<expected_output> build_expected_output(std::uint16_t input_value);

} // namespace frog::runtime::cpp_ref
