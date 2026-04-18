from __future__ import annotations

from Implementations.Reference.Runtime.reference_runtime import (
    ReferenceHostRuntime,
    create_runtime_for_family,
)


DEFAULT_RUNTIME_FAMILY = "reference_host_runtime_ui_binding"


def build_runtime_core() -> ReferenceHostRuntime:
    return create_runtime_for_family(DEFAULT_RUNTIME_FAMILY)
