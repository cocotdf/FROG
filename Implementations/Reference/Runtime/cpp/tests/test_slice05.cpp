#include <cassert>
#include <iostream>
#include <string>

#include "json.hpp"
#include "runtime.hpp"
#include "ui.hpp"

int main() {
    try {
        frog::runtime::Slice05RuntimeCore runtime;
        const auto artifact = runtime.execute(std::uint16_t{3});
        const auto& root = artifact.as_object();
        assert(root.at("artifact_kind").as_string() == "frog_runtime_execution_result");
        assert(root.at("status").as_string() == "ok");
        const auto& outputs = root.at("outputs").as_object();
        assert(outputs.at("public").as_object().at("result").as_i64() == 15);
        assert(outputs.at("ui").as_object().at("ind_result").as_i64() == 15);

        frog::runtime::BrowserUiRuntime ui_runtime;
        const std::string html = ui_runtime.render_html();
        assert(html.find("Run Example 05") != std::string::npos);
        assert(html.find("/asset/numeric_control_svg") != std::string::npos);
        assert(html.find("/asset/numeric_indicator_svg") != std::string::npos);

        std::cout << "C++ runtime tests passed." << std::endl;
        return 0;
    } catch (const std::exception& error) {
        std::cerr << error.what() << std::endl;
        return 1;
    }
}
