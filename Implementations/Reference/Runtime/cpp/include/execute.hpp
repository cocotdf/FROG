#pragma once

#include <cstdint>
#include <filesystem>
#include <optional>

#include "json.hpp"

namespace frog::runtime {

frog::json::Value execute_contract(
    std::uint16_t input_value,
    std::optional<std::filesystem::path> contract_path = std::nullopt,
    std::optional<std::filesystem::path> wfrog_path = std::nullopt);

} // namespace frog::runtime
