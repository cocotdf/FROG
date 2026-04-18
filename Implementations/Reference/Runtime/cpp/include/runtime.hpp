#pragma once

#include "contract.hpp"

#include <cstdint>
#include <map>
#include <string>

namespace frog::runtime::cpp_ref {

struct widget_runtime_state {
    std::string widget_id;
    std::string widget_class;
    std::string role;
    std::uint16_t numeric_value = 0;
    std::string foreground_color;
};

struct runtime_state {
    std::uint16_t loop_state = 0;
    std::uint16_t public_output = 0;
    std::map<std::string, widget_runtime_state> widgets;
};

runtime_state make_initial_runtime_state(const example05_contract& contract, std::uint16_t control_value);

} // namespace frog::runtime::cpp_ref
