#include "execute.hpp"

#include "runtime.hpp"

namespace frog::runtime {

frog::json::Value execute_contract(
    std::uint16_t input_value,
    std::optional<std::filesystem::path> contract_path,
    std::optional<std::filesystem::path> wfrog_path) {
    Slice05RuntimeCore runtime(
        contract_path.value_or(default_contract_path()),
        wfrog_path.value_or(default_wfrog_path()));
    return runtime.execute(input_value);
}

} // namespace frog::runtime
