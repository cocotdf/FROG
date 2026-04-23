(function () {
  "use strict";

  var diagramReplacements = [
  {
    "path": "/Readme.md",
    "sectionId": "positioning",
    "kind": "image",
    "occurrence": 1,
    "count": 1,
    "image": "./assets/readme-positioning-map.png",
    "alt": "FROG positioning map: accessibility versus system-grade execution",
    "width": "760"
  },
  {
    "path": "/Readme.md",
    "sectionId": "dataflow-programming",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "./assets/readme-dataflow-execution.png",
    "alt": "Traditional execution compared with dataflow execution",
    "width": "760"
  },
  {
    "path": "/Readme.md",
    "sectionId": "repository-runtime-and-native-execution-direction",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "./assets/readme-runtime-native-execution-direction.png",
    "alt": "Runtime and native execution direction from canonical source to runtimes and optional LLVM-oriented native path",
    "width": "760"
  },
  {
    "path": "/Readme.md",
    "sectionId": "specification-architecture",
    "kind": "pre",
    "occurrence": 1,
    "count": 2,
    "image": "./assets/readme-specification-architecture.png",
    "alt": "FROG specification architecture layers",
    "width": "760"
  },
  {
    "path": "/Readme.md",
    "sectionId": "program-representation",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "./assets/readme-program-representation-pipeline.png",
    "alt": "FROG program representation pipeline from source to FIR and lowering",
    "width": "760"
  },
  {
    "path": "/Readme.md",
    "sectionId": "execution-architecture",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "./assets/readme-execution-architecture.png",
    "alt": "FROG execution architecture from IDE authoring to target execution and observability",
    "width": "760"
  },
  {
    "path": "/Readme.md",
    "sectionId": "recommended-reading-path",
    "kind": "pre",
    "occurrence": 2,
    "count": 1,
    "image": "assets/ascii-flow-diagrams/ascii-flow-23-readme.png",
    "alt": "ASCII flow diagram replacement for Readme.md section Recommended reading path",
    "width": "760"
  },
  {
    "path": "/Examples/Readme.md",
    "sectionId": "applicative-vertical-slice-anchor",
    "kind": "pre",
    "occurrence": 2,
    "count": 1,
    "image": "../assets/ascii-flow-diagrams/ascii-flow-08-examples-readme.png",
    "alt": "ASCII flow diagram replacement for Examples/Readme.md section 12. Applicative Vertical-Slice Anchor",
    "width": "760"
  },
  {
    "path": "/Expression/Cache.md",
    "sectionId": "cache-model",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../assets/ascii-flow-diagrams/ascii-flow-09-expression-cache.png",
    "alt": "ASCII flow diagram replacement for Expression/Cache.md section 8. Cache Model",
    "width": "760"
  },
  {
    "path": "/Expression/Icon.md",
    "sectionId": "coordinate-system-and-sizing",
    "kind": "pre",
    "occurrence": 2,
    "count": 1,
    "image": "../assets/ascii-flow-diagrams/ascii-flow-10-expression-icon.png",
    "alt": "ASCII flow diagram replacement for Expression/Icon.md section 9. Coordinate System and Sizing",
    "width": "760"
  },
  {
    "path": "/Expression/Type.md",
    "sectionId": "type-compatibility-model",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../assets/ascii-flow-diagrams/ascii-flow-11-expression-type.png",
    "alt": "ASCII flow diagram replacement for Expression/Type.md section 10. Type Compatibility Model",
    "width": "760"
  },
  {
    "path": "/Expression/Widget interaction.md",
    "sectionId": "diagram-representation",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../assets/ascii-flow-diagrams/ascii-flow-12-expression-widget-interaction.png",
    "alt": "ASCII flow diagram replacement for Expression/Widget interaction.md section 15. Diagram Representation",
    "width": "760"
  },
  {
    "path": "/IDE/Debugging.md",
    "sectionId": "relationship-with-probes-and-watches",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../assets/ascii-flow-diagrams/ascii-flow-13-ide-debugging.png",
    "alt": "ASCII flow diagram replacement for IDE/Debugging.md section 15. Relationship with Probes and Watches",
    "width": "760"
  },
  {
    "path": "/IDE/Observability.md",
    "sectionId": "high-level-observability-model",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../assets/ascii-flow-diagrams/ascii-flow-14-ide-observability.png",
    "alt": "ASCII flow diagram replacement for IDE/Observability.md section 6. High-Level Observability Model",
    "width": "760"
  },
  {
    "path": "/IDE/Probes.md",
    "sectionId": "overview",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../assets/ascii-flow-diagrams/ascii-flow-15-ide-probes.png",
    "alt": "ASCII flow diagram replacement for IDE/Probes.md section 1. Overview",
    "width": "760"
  },
  {
    "path": "/IDE/Readme.md",
    "sectionId": "high-level-architecture",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../assets/ascii-flow-diagrams/ascii-flow-16-ide-readme.png",
    "alt": "ASCII flow diagram replacement for IDE/Readme.md section 7. High-Level Architecture",
    "width": "760"
  },
  {
    "path": "/IDE/Snippet.md",
    "sectionId": "illustrative-examples",
    "kind": "pre",
    "occurrence": 5,
    "count": 1,
    "image": "../assets/ascii-flow-diagrams/ascii-flow-17-ide-snippet.png",
    "alt": "ASCII flow diagram replacement for IDE/Snippet.md section 20.5 Drag-and-drop behavior",
    "width": "760"
  },
  {
    "path": "/IR/Construction rules.md",
    "sectionId": "construction-result",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../assets/ascii-flow-diagrams/ascii-flow-20-ir-construction-rules.png",
    "alt": "ASCII flow diagram replacement for IR/Construction rules.md section 6. Construction Result",
    "width": "760"
  },
  {
    "path": "/IR/Readme.md",
    "sectionId": "position-in-the-representation-pipeline",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../assets/ascii-flow-diagrams/ascii-flow-21-ir-readme.png",
    "alt": "ASCII flow diagram replacement for IR/Readme.md section 5. Position in the Representation Pipeline",
    "width": "760"
  },
  {
    "path": "/Libraries/Readme.md",
    "sectionId": "libraries-vs-profiles",
    "kind": "pre",
    "occurrence": 2,
    "count": 1,
    "image": "../assets/ascii-flow-diagrams/ascii-flow-22-libraries-readme.png",
    "alt": "ASCII flow diagram replacement for Libraries/Readme.md section 8. Libraries vs Profiles",
    "width": "760"
  },
  {
    "path": "/Versioning/Readme.md",
    "sectionId": "repository-wide-versioning-diagram",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../assets/ascii-flow-diagrams/ascii-flow-25-versioning-readme.png",
    "alt": "ASCII flow diagram replacement for Versioning/Readme.md section 29. Repository-Wide Versioning Diagram",
    "width": "760"
  },
  {
    "path": "/Strategy/Heilmeier/Readme.md",
    "sectionId": "future-end-to-end-poc-direction",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../../assets/ascii-flow-diagrams/ascii-flow-24-strategy-heilmeier-readme.png",
    "alt": "ASCII flow diagram replacement for Strategy/Heilmeier/Readme.md section 14. Future End-to-End POC Direction",
    "width": "760"
  },
  {
    "path": "/Implementations/Reference/Readme.md",
    "sectionId": "architectural-position",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../../assets/ascii-flow-diagrams/ascii-flow-18-implementations-reference-readme.png",
    "alt": "ASCII flow diagram replacement for Implementations/Reference/Readme.md section 4. Architectural Position",
    "width": "760"
  },
  {
    "path": "/Implementations/Reference/Readme.md",
    "sectionId": "example-contract-runtime-reading",
    "kind": "pre",
    "occurrence": 3,
    "count": 1,
    "image": "../../assets/ascii-flow-diagrams/ascii-flow-19-implementations-reference-readme.png",
    "alt": "ASCII flow diagram replacement for Implementations/Reference/Readme.md section 8. Example -> Contract -> Runtime Reading",
    "width": "760"
  },
  {
    "path": "/Examples/04_stateful_feedback_delay/Readme.md",
    "sectionId": "source-shape",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../../assets/ascii-flow-diagrams/ascii-flow-07-examples-04-stateful-feedback-delay-readme.png",
    "alt": "ASCII flow diagram replacement for Examples/04_stateful_feedback_delay/Readme.md section 4. Source Shape",
    "width": "760"
  },
  {
    "path": "/Conformance/invalid/50_identity_loss_must_not_be_disguised_as_intentional_non_primary_correspondence.md",
    "sectionId": "intended-anti-pattern",
    "kind": "pre",
    "occurrence": 2,
    "count": 1,
    "image": "../../assets/ascii-flow-diagrams/ascii-flow-01-conformance-invalid-50-identity-loss-must-not-be-disguised-as-intentional-non-primary-corr.png",
    "alt": "ASCII flow diagram replacement for Conformance/invalid/50_identity_loss_must_not_be_disguised_as_intentional_non_primary_correspondence.md section 3. Intended Anti-Pattern",
    "width": "760"
  },
  {
    "path": "/Conformance/invalid/52_primary_execution_object_without_recoverable_source_anchor_is_invalid.md",
    "sectionId": "intended-anti-pattern",
    "kind": "pre",
    "occurrence": 2,
    "count": 1,
    "image": "../../assets/ascii-flow-diagrams/ascii-flow-02-conformance-invalid-52-primary-execution-object-without-recoverable-source-anchor-is-inval.png",
    "alt": "ASCII flow diagram replacement for Conformance/invalid/52_primary_execution_object_without_recoverable_source_anchor_is_invalid.md section 3. Intended Anti-Pattern",
    "width": "760"
  },
  {
    "path": "/Conformance/valid/05_public_interface_and_widget_participation_distinct.md",
    "sectionId": "overview",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../../assets/ascii-flow-diagrams/ascii-flow-03-conformance-valid-05-public-interface-and-widget-participation-distinct.png",
    "alt": "ASCII flow diagram replacement for Conformance/valid/05_public_interface_and_widget_participation_distinct.md section 1. Overview",
    "width": "760"
  },
  {
    "path": "/Conformance/valid/15_explicit_connectivity_remains_distinct_from_inferred_evaluation_order.md",
    "sectionId": "overview",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../../assets/ascii-flow-diagrams/ascii-flow-04-conformance-valid-15-explicit-connectivity-remains-distinct-from-inferred-evaluation-order.png",
    "alt": "ASCII flow diagram replacement for Conformance/valid/15_explicit_connectivity_remains_distinct_from_inferred_evaluation_order.md section 1. Overview",
    "width": "760"
  },
  {
    "path": "/Conformance/valid/21_explicit_structure_owned_state_remains_distinct_from_inferred_persistent_value_by_feedback_shape.md",
    "sectionId": "overview",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../../assets/ascii-flow-diagrams/ascii-flow-05-conformance-valid-21-explicit-structure-owned-state-remains-distinct-from-inferred-persist.png",
    "alt": "ASCII flow diagram replacement for Conformance/valid/21_explicit_structure_owned_state_remains_distinct_from_inferred_persistent_value_by_feedback_shape.md section 1. Overview",
    "width": "760"
  },
  {
    "path": "/Conformance/valid/53_schema_valid_canonical_ir_must_still_preserve_ir_architectural_distinctions.md",
    "sectionId": "boundary-being-exercised",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../../assets/ascii-flow-diagrams/ascii-flow-06-conformance-valid-53-schema-valid-canonical-ir-must-still-preserve-ir-architectural-distin.png",
    "alt": "ASCII flow diagram replacement for Conformance/valid/53_schema_valid_canonical_ir_must_still_preserve_ir_architectural_distinctions.md section 4. Boundary Being Exercised",
    "width": "760"
  }
];

  function normalizePath(path) {
    var normalized = String(path || "/Readme.md");
    if (normalized.charAt(0) !== "/") {
      normalized = "/" + normalized;
    }
    return normalized.replace(/\/+/g, "/").toLowerCase();
  }

  function escapeRegExp(value) {
    return String(value).replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
  }

  function escapeHtml(value) {
    return String(value || "")
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  function imageHtml(entry) {
    return [
      '<p align="center" class="frog-pages-diagram">',
      '  <img src="' + escapeHtml(entry.image) + '" alt="' + escapeHtml(entry.alt || "Generated diagram") + '" width="' + escapeHtml(entry.width || "760") + '" />',
      '</p>'
    ].join("\n");
  }

  function sectionRange(markdown, sectionId) {
    if (!sectionId) {
      return { start: 0, end: markdown.length };
    }

    var headingPattern = new RegExp("<h2\\s+id=[\"']" + escapeRegExp(sectionId) + "[\"'][^>]*>[\\s\\S]*?<\\/h2>", "i");
    var headingMatch = headingPattern.exec(markdown);
    if (!headingMatch) {
      return null;
    }

    var start = headingMatch.index + headingMatch[0].length;
    var remainder = markdown.slice(start);
    var nextHeadingIndex = remainder.search(/<h2\s+id=["'][^"']+["'][^>]*>/i);
    return {
      start: start,
      end: nextHeadingIndex === -1 ? markdown.length : start + nextHeadingIndex
    };
  }

  function replaceBlock(markdown, entry) {
    var range = sectionRange(markdown, entry.sectionId);
    if (!range) {
      return markdown;
    }

    var section = markdown.slice(range.start, range.end);
    var pattern = entry.kind === "image"
      ? /<p\s+align=["']center["']>\s*<img\b[\s\S]*?<\/p>/gi
      : /<pre\b[\s\S]*?<\/pre>/gi;
    var matches = [];
    var match;

    while ((match = pattern.exec(section)) !== null) {
      matches.push({ index: match.index, value: match[0] });
    }

    var occurrence = Math.max(1, Number(entry.occurrence || 1));
    var count = Math.max(1, Number(entry.count || 1));
    var first = matches[occurrence - 1];
    var last = matches[occurrence + count - 2];

    if (!first || !last) {
      return markdown;
    }

    var absoluteStart = range.start + first.index;
    var absoluteEnd = range.start + last.index + last.value.length;
    return markdown.slice(0, absoluteStart) + imageHtml(entry) + markdown.slice(absoluteEnd);
  }

  window.applyPagesDiagramReplacements = function (markdown, currentFile) {
    var normalizedCurrentFile = normalizePath(currentFile);
    return diagramReplacements.reduce(function (nextMarkdown, entry) {
      if (normalizePath(entry.path) !== normalizedCurrentFile) {
        return nextMarkdown;
      }
      return replaceBlock(nextMarkdown, entry);
    }, String(markdown || ""));
  };
}());
