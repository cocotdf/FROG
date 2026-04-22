#include <cassert>
#include <filesystem>
#include <iostream>
#include <stdexcept>
#include <string>

#include "contract.hpp"
#include "execute.hpp"
#include "json.hpp"
#include "ui.hpp"

namespace {

std::filesystem::path repo_root() {
    return frog::runtime::find_repo_root(std::filesystem::path(FROG_RUNTIME_CPP_SOURCE_DIR));
}

frog::json::Value load_json(const std::filesystem::path& path) {
    return frog::json::parse_file(path);
}

std::filesystem::path resolve_repo_path(const std::string& relative_path) {
    return repo_root() / relative_path;
}

std::string canonical_json(const frog::json::Value& value) {
    return frog::json::stringify(value, true, 2);
}

const frog::json::Object& acceptance_root() {
    static const frog::json::Value acceptance = load_json(
        repo_root() / "Implementations" / "Reference" / "Runtime" / "acceptance" / "example05_runtime_family.acceptance.json");
    return acceptance.as_object();
}

void test_headless_snapshot() {
    const auto& root = acceptance_root();
    const auto& refs = root.at("artifact_refs").as_object();
    const auto& headless = root.at("headless").as_object();
    const auto contract_path = resolve_repo_path(refs.at("contract_path").as_string());
    const auto wfrog_path = resolve_repo_path(refs.at("wfrog_path").as_string());
    const auto snapshot_path = resolve_repo_path(refs.at("snapshot_path").as_string());

    const auto expected = load_json(snapshot_path);
    const auto actual = frog::runtime::execute_contract(
        static_cast<std::uint16_t>(headless.at("input_value").as_i64()),
        contract_path,
        wfrog_path);

    assert(canonical_json(actual) == canonical_json(expected));
}

void test_overflow_rejection() {
    const auto& root = acceptance_root();
    const auto& refs = root.at("artifact_refs").as_object();
    const auto& overflow = root.at("overflow").as_object();
    const auto contract_path = resolve_repo_path(refs.at("contract_path").as_string());
    const auto wfrog_path = resolve_repo_path(refs.at("wfrog_path").as_string());

    bool rejected = false;
    try {
        static_cast<void>(frog::runtime::execute_contract(
            static_cast<std::uint16_t>(overflow.at("input_value").as_i64()),
            contract_path,
            wfrog_path));
    } catch (const std::exception& error) {
        rejected = true;
        assert(std::string(error.what()) == overflow.at("expected_error").as_string());
    }
    assert(rejected);
}

void test_ui_surface() {
    const auto& root = acceptance_root();
    const auto& refs = root.at("artifact_refs").as_object();
    const auto& routes = root.at("ui").as_object().at("expected_routes").as_array();
    const auto contract_path = resolve_repo_path(refs.at("contract_path").as_string());
    const auto wfrog_path = resolve_repo_path(refs.at("wfrog_path").as_string());
    const auto snapshot_path = resolve_repo_path(refs.at("snapshot_path").as_string());
    const auto expected = load_json(snapshot_path);

    frog::runtime::BrowserUiRuntime runtime(contract_path, wfrog_path);
    const std::string html = runtime.render_html();
    for (const auto& route_value : routes) {
        const auto route = route_value.as_string();
        if (route == "/") {
            continue;
        }
        assert(html.find(route) != std::string::npos);
    }

    runtime.core.execute(static_cast<std::uint16_t>(root.at("headless").as_object().at("input_value").as_i64()));
    assert(canonical_json(runtime.core.execution_artifact()) == canonical_json(expected));
    assert(std::filesystem::exists(runtime.core.asset_map.at("numeric_control_svg")));
    assert(std::filesystem::exists(runtime.core.asset_map.at("numeric_indicator_svg")));
}

} // namespace

int main() {
    test_headless_snapshot();
    test_overflow_rejection();
    test_ui_surface();
    std::cout << "slice05 runtime acceptance passed" << std::endl;
    return 0;
}
