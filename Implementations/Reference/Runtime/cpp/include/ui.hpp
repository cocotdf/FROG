#pragma once

#include "runtime.hpp"

#include <string>

namespace frog::runtime::cpp_ref {

void apply_indicator_foreground_color(runtime_state& state, const std::string& widget_id, const std::string& color);
std::string render_runtime_summary(const runtime_state& state);

} // namespace frog::runtime::cpp_ref
