#include "contract.hpp"
#include "execute.hpp"
#include "runtime.hpp"
#include "ui.hpp"

#include <cstdint>
#include <cstdlib>
#include <filesystem>
#include <fstream>
#include <iostream>
#include <map>
#include <optional>
#include <regex>
#include <sstream>
#include <stdexcept>
#include <string>
#include <vector>

namespace frog::runtime::cpp_ref {
namespace {

std::string read_text_file(const std::string& path) {
    std::ifstream input(path, std::ios::in | std::ios::binary);
    if (!input) {
        throw std::runtime_error("unable to open contract file: " + path);
    }
    std::ostringstream buffer;
    buffer << input.rdbuf();
    return buffer.str();
}

std::string normalize_json(std::string text) {
    for (char& ch : text) {
        if (ch == '\n' || ch == '\r' || ch == '\t') {
            ch = ' ';
        }
    }
    return text;
}

std::string extract_first_string(const std::string& text, const std::string& key) {
    const std::regex pattern("\\\"" + key + "\\\"\\s*:\\s*\\\"([^\\\"]+)\\\"");
    std::smatch match;
    if (!std::regex_search(text, match, pattern)) {
        throw std::runtime_error("missing string field: " + key);
    }
    return match[1].str();
}

std::uint32_t extract_first_uint(const std::string& text, const std::string& key) {
    const std::regex pattern("\\\"" + key + "\\\"\\s*:\\s*([0-9]+)");
    std::smatch match;
    if (!std::regex_search(text, match, pattern)) {
        throw std::runtime_error("missing integer field: " + key);
    }
    return static_cast<std::uint32_t>(std::stoul(match[1].str()));
}

bool has_widget_binding(
    const std::string& text,
    const std::string& widget_id,
    const std::string& widget_class,
    const std::string& role,
    const std::string& public_port_id,
    const std::string& binding_key) {
    const std::regex pattern(
        "\\{\\s*\\\"widget_id\\\"\\s*:\\s*\\\"" + widget_id +
        "\\\".*?\\\"widget_class\\\"\\s*:\\s*\\\"" + widget_class +
        "\\\".*?\\\"role\\\"\\s*:\\s*\\\"" + role +
        "\\\".*?\\\"binding\\\"\\s*:\\s*\\{.*?\\\"mode\\\"\\s*:\\s*\\\"widget_value\\\".*?\\\"" +
        binding_key + "\\\"\\s*:\\s*\\\"" + public_port_id + "\\\".*?\\}.*?\\}");
    return std::regex_search(text, pattern);
}

std::string extract_property_write_color(const std::string& text, const std::string& widget_id) {
    const std::regex pattern(
        "\\{.*?\\\"operation\\\"\\s*:\\s*\\\"frog\\.ui\\.property_write\\\".*?"
        "\\\"widget_id\\\"\\s*:\\s*\\\"" + widget_id +
        "\\\".*?\\\"member\\\"\\s*:\\s*\\\"foreground_color\\\".*?"
        "\\\"value\\\"\\s*:\\s*\\{.*?\\\"type\\\"\\s*:\\s*\\\"frog\\.color\\.rgba8\\\".*?"
        "\\\"value\\\"\\s*:\\s*\\\"([^\\\"]+)\\\".*?\\}.*?\\}");
    std::smatch match;
    if (!std::regex_search(text, match, pattern)) {
        throw std::runtime_error("missing foreground_color property write for widget: " + widget_id);
    }
    return match[1].str();
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

std::string parse_contract_path(int argc, char** argv) {
    if (argc >= 3) {
        return argv[2];
    }
    return default_example05_contract_path();
}

std::uint16_t checked_u16(std::uint32_t value, const std::string& label) {
    if (value > 65535u) {
        throw std::runtime_error(label + " exceeds the u16 domain");
    }
    return static_cast<std::uint16_t>(value);
}

} // namespace

std::string default_example05_contract_path() {
#ifdef FROG_EXAMPLE05_CONTRACT_PATH
    return std::string(FROG_EXAMPLE05_CONTRACT_PATH);
#else
    return "Implementations/Reference/ContractEmitter/examples/05_bounded_ui_accumulator.reference_host_runtime_ui_binding.contract.json";
#endif
}

std::optional<example05_contract> load_example05_contract_from_file(const std::string& path, std::string& error) {
    try {
        const std::string text = normalize_json(read_text_file(path));

        example05_contract contract;
        contract.backend_family = extract_first_string(text, "backend_family");
        contract.example_id = extract_first_string(text, "example_id");
        contract.public_input_id = extract_first_string(text, "public_input_id");
        contract.public_output_id = extract_first_string(text, "public_output_id");
        contract.initial_state = checked_u16(extract_first_uint(text, "initial_value"), "initial_value");
        contract.iterations = extract_first_uint(text, "iteration_count");

        if (contract.backend_family != "reference_host_runtime_ui_binding") {
            throw std::runtime_error("unsupported backend family: " + contract.backend_family);
        }
        if (contract.example_id != "05_bounded_ui_accumulator") {
            throw std::runtime_error("unexpected example id: " + contract.example_id);
        }
        if (contract.public_input_id != "input_value") {
            throw std::runtime_error("expected public input id input_value");
        }
        if (contract.public_output_id != "result") {
            throw std::runtime_error("expected public output id result");
        }
        if (contract.iterations != 5) {
            throw std::runtime_error("this minimal runtime only supports 5 iterations for Example 05");
        }

        if (!has_widget_binding(text, "ctrl_input", "frog.widgets.numeric_control", "control", "input_value", "public_input_id")) {
            throw std::runtime_error("missing or invalid ctrl_input widget binding");
        }
        if (!has_widget_binding(text, "ind_result", "frog.widgets.numeric_indicator", "indicator", "result", "public_output_id")) {
            throw std::runtime_error("missing or invalid ind_result widget binding");
        }

        contract.widgets = {
            {"ctrl_input", "frog.widgets.numeric_control", "control"},
            {"ind_result", "frog.widgets.numeric_indicator", "indicator"},
        };
        contract.property_writes = {
            {"ctrl_input", "foreground_color", "frog.color.rgba8", extract_property_write_color(text, "ctrl_input")},
            {"ind_result", "foreground_color", "frog.color.rgba8", extract_property_write_color(text, "ind_result")},
        };

        return contract;
    } catch (const std::exception& ex) {
        error = ex.what();
        return std::nullopt;
    }
}

expected_output build_expected_output(std::uint16_t input_value) {
    expected_output out;
    out.final_state = checked_u16(static_cast<std::uint32_t>(input_value) * 5u, "expected final state");
    out.public_output = out.final_state;
    out.property_member = "foreground_color";
    return out;
}

runtime_state make_initial_runtime_state(const example05_contract& contract, std::uint16_t control_value) {
    runtime_state state;
    state.loop_state = contract.initial_state;
    state.public_output = contract.initial_state;

    std::map<std::string, std::string> colors;
    for (const auto& write : contract.property_writes) {
        colors.emplace(write.widget_id, write.value_literal);
    }

    for (const auto& widget : contract.widgets) {
        widget_runtime_state widget_state;
        widget_state.widget_id = widget.widget_id;
        widget_state.widget_class = widget.widget_class;
        widget_state.role = widget.role;
        widget_state.foreground_color = colors[widget.widget_id];
        if (widget.role == "control") {
            widget_state.numeric_value = control_value;
        }
        state.widgets.emplace(widget.widget_id, widget_state);
    }

    return state;
}

runtime_state execute_example05(const example05_contract& contract, std::uint16_t control_value) {
    runtime_state state = make_initial_runtime_state(contract, control_value);

    for (std::uint32_t i = 0; i < contract.iterations; ++i) {
        const std::uint32_t candidate = static_cast<std::uint32_t>(state.loop_state) + control_value;
        if (candidate > 65535u) {
            throw std::runtime_error("u16 overflow during bounded accumulation");
        }
        state.loop_state = static_cast<std::uint16_t>(candidate);
    }

    state.public_output = state.loop_state;
    state.widgets["ctrl_input"].numeric_value = control_value;
    state.widgets["ind_result"].numeric_value = state.public_output;
    return state;
}

std::string render_runtime_summary(const runtime_state& state) {
    std::ostringstream oss;
    oss << "runtime=cpp\n";
    oss << "loop_state=" << state.loop_state << "\n";
    oss << "public_output=" << state.public_output << "\n";
    for (const auto& [id, widget] : state.widgets) {
        oss << "widget=" << id
            << ";class=" << widget.widget_class
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
        const std::string contract_path = parse_contract_path(argc, argv);
        std::string error;
        const auto contract = load_example05_contract_from_file(contract_path, error);
        if (!contract.has_value()) {
            std::cerr << "error: " << error << std::endl;
            return 1;
        }

        const expected_output expected = build_expected_output(input_value);
        const runtime_state result = execute_example05(*contract, input_value);

        if (result.loop_state != expected.final_state || result.public_output != expected.public_output) {
            std::cerr << "example 05 parity failure" << std::endl;
            std::cerr << render_runtime_summary(result);
            return 2;
        }

        const auto ctrl_it = result.widgets.find("ctrl_input");
        const auto ind_it = result.widgets.find("ind_result");
        if (ctrl_it == result.widgets.end() || ind_it == result.widgets.end()) {
            std::cerr << "example 05 runtime state is missing required widgets" << std::endl;
            return 3;
        }
        if (ctrl_it->second.foreground_color != "#5B9BD5" || ind_it->second.foreground_color != "#70AD47") {
            std::cerr << "example 05 property write parity failure" << std::endl;
            std::cerr << render_runtime_summary(result);
            return 4;
        }

        std::cout << "contract_path=" << contract_path << "\n";
        std::cout << render_runtime_summary(result);
        std::cout << "status=ok" << std::endl;
        return 0;
    } catch (const std::exception& e) {
        std::cerr << "error: " << e.what() << std::endl;
        return 10;
    }
}
