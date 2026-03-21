from __future__ import annotations

from pathlib import Path

from Implementations.Reference.common import DEMO_ARTIFACT_VERSION, LoadedSource, load_json_file, sha256_text


def load_source(file_path: str) -> LoadedSource:
    path = Path(file_path)
    text, document = load_json_file(path)

    artifact = {
        "artifact_kind": "frog_loaded_source",
        "artifact_version": DEMO_ARTIFACT_VERSION,
        "source": {
            "path": str(path).replace("\\", "/"),
            "content_hash": sha256_text(text),
            "spec_version": document.get("spec_version"),
        },
        "document": document,
        "diagnostics": [],
    }
    return LoadedSource(artifact=artifact)
