#include "contract.hpp"
#include "execute.hpp"
#include "runtime.hpp"
#include "ui.hpp"

#include <cstdlib>
#include <iostream>
#include <sstream>
#include <stdexcept>

namespace frog::runtime::cpp_ref {
namespace {

std::uint16_t clamp_u16(std::uint32_t value, std::uint16_t low, std::uint16_t high) {
    if (value < low) {
        return low;
    }
    if (value > high) {
        return high;
    }
    return static_cast<std::uint16_t>(value);
}

std::uint16_t parse_input_value(int argc, char** argv) {
    if (argc < 2) {
        return 3;
    }

    const long parsed = std::strtol(argv[1], nullptr, 10);
    if (parsed < 0 || parsed > 65535) {
        throw std::runtime_error("input must be in the range [0, 65535]");
    }

    return static_cast<std::uint16_t>(parsed);
}

} // namespace

std::optional<example05_contract> build_example05_contract(std::uint16_t input_value) {
    example05_contract contract;
    contract.backend_family = "reference_host_runtime_ui_binding";
    contract.example_id = "05_bounded_ui_accumulator";
    contract.initial_state = 0;
    contract.iterations = 5;
    contract.input_value = input_value;
    contract.lower_bound = 0;
    contract.upper_bound = 65535;
    contract.widgets = {
        {"bounded_input", "control"},
        {"bounded_output", "indicator"}
    };
    return contract;
}

std::optional<expected_output> build_expected_output(std::uint16_t input_value) {
    expected_output out;
    out.final_state = static_cast<std::uint16_t>(input_value * 5);
    out.public_output = out.final_state;
    out.property_member = "foreground_color";
    return out;
}

runtime_state make_initial_runtime_state(const example05_contract& contract) {
    runtime_state state;
    state.loop_state = contract.initial_state;
    state.public_output = contract.initial_state;

    for (const auto& widget : contract.widgets) {
        widget_runtime_state widget_state;
        widget_state.widget_id = widget.widget_id;
        widget_state.role = widget.role;
        if (widget.role == "control") {
            widget_state.numeric_value = contract.input_value;
        }
        state.widgets.emplace(widget.widget_id, widget_state);
    }

    return state;
}

runtime_state execute_example05(const example05_contract& contract) {
    runtime_state state = make_initial_runtime_state(contract);

    for (std::uint16_t i = 0; i < contract.iterations; ++i) {
        const std::uint32_t candidate = static_cast<std::uint32_t>(state.loop_state) + contract.input_value;
        state.loop_state = clamp_u16(candidate, contract.lower_bound, contract.upper_bound);
    }

    state.public_output = state.loop_state;

    auto indicator_it = state.widgets.find("bounded_output");
    if (indicator_it != state.widgets.end()) {
        indicator_it->second.numeric_value = state.public_output;
        indicator_it->second.foreground_color = "green";
    }

    return state;
}

void apply_indicator_foreground_color(runtime_state& state, const std::string& widget_id, const std::string& color) {
    auto it = state.widgets.find(widget_id);
    if (it != state.widgets.end()) {
        it->second.foreground_color = color;
    }
}

std::string render_runtime_summary(const runtime_state& state) {
    std::ostringstream oss;
    oss << "runtime=cpp\n";
    oss << "loop_state=" << state.loop_state << "\n";
    oss << "public_output=" << state.public_output << "\n";
    for (const auto& [id, widget] : state.widgets) {
        oss << "widget=" << id
            << ";role=" << widget.role
            << ";value=" << widget.numeric_value
            << ";foreground_color=" << widget.foreground_color
            << "\n";
    }
    return oss.str();
}

} // namespace frog::runtime::cpp_ref

int main(int argc, char** argv) {
    using namespace frog::runtime::cpp_ref;

    try {
        const std::uint16_t input_value = parse_input_value(argc, argv);
        const auto contract = build_example05_contract(input_value);
        const auto expected = build_expected_output(input_value);

        if (!contract.has_value() || !expected.has_value()) {
            std::cerr << "failed to build example 05 contract" << std::endl;
            return 1;
        }

        if (contract->backend_family != "reference_host_runtime_ui_binding") {
            std::cerr << "unsupported backend family: " << contract->backend_family << std::endl;
            return 2;
        }

        runtime_state result = execute_example05(*contract);

        if (result.loop_state != expected->final_state || result.public_output != expected->public_output) {
            std::cerr << "example 05 parity failure" << std::endl;
            std::cerr << render_runtime_summary(result);
            return 3;
        }

        std::cout << render_runtime_summary(result);
        std::cout << "status=ok" << std::endl;
        return 0;
    } catch (const std::exception& e) {
        std::cerr << "error: " << e.what() << std::endl;
        return 10;
    }
}
