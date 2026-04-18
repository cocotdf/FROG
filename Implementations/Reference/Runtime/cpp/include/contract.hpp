#pragma once

#include <cstdint>
#include <optional>
#include <string>
#include <vector>

namespace frog::runtime::cpp_ref {

struct widget_binding {
    std::string widget_id;
    std::string widget_class;
    std::string role;
};

struct property_write {
    std::string widget_id;
    std::string member;
    std::string value_type;
    std::string value_literal;
};

struct example05_contract {
    std::string backend_family;
    std::string example_id;
    std::string public_input_id;
    std::string public_output_id;
    std::uint16_t initial_state = 0;
    std::uint32_t iterations = 0;
    std::vector<widget_binding> widgets;
    std::vector<property_write> property_writes;
};

struct expected_output {
    std::uint16_t final_state = 0;
    std::uint16_t public_output = 0;
    std::string property_member;
};

std::string default_example05_contract_path();
std::optional<example05_contract> load_example05_contract_from_file(const std::string& path, std::string& error);
expected_output build_expected_output(std::uint16_t input_value);

} // namespace frog::runtime::cpp_ref
