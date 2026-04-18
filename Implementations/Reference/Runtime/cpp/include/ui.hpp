#pragma once

#include "runtime.hpp"

#include <string>

namespace frog::runtime::cpp_ref {

std::string render_runtime_summary(const runtime_state& state);

} // namespace frog::runtime::cpp_ref
