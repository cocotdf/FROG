#pragma once

#include <cstdint>
#include <filesystem>
#include <optional>
#include <string>

#include "runtime.hpp"

namespace frog::runtime {

class BrowserUiRuntime {
public:
    BrowserUiRuntime(
        std::optional<std::filesystem::path> contract_path = std::nullopt,
        std::optional<std::filesystem::path> wfrog_path = std::nullopt);

    std::string render_html() const;
    void serve(const std::string& host = "127.0.0.1", std::uint16_t port = 0, bool open_browser = true);

    Slice05RuntimeCore core;
    std::optional<std::string> last_error;
};

} // namespace frog::runtime
