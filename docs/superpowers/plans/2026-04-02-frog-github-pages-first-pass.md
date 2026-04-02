# FROG GitHub Pages First Pass Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a first-pass Docsify-based GitHub Pages shell to `Graiphic/FROG` so the existing documentation corpus becomes browsable and visually clean without renaming the existing `Readme.md` files.

**Architecture:** Add a lightweight root Pages shell (`index.html`, `404.html`, `.nojekyll`, `_sidebar.md`, `_navbar.md`) and a PowerShell smoke-check script. The Docsify bootstrap will explicitly use `Readme.md` entry points and rewrite same-repo markdown and asset paths at runtime so the existing repository structure remains stable during this first pass.

**Tech Stack:** Static HTML/CSS/JavaScript, Docsify via CDN, PowerShell verification script, GitHub Pages.

---

### Task 1: Define the expected GitHub Pages surface with a failing smoke-check

**Files:**
- Create: `C:/Users/PortableDEV/Desktop/FROG/scripts/verify-github-pages.ps1`

- [ ] **Step 1: Write the failing test**

```powershell
$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot

$requiredFiles = @(
    ".nojekyll",
    "index.html",
    "404.html",
    "_sidebar.md",
    "_navbar.md",
    "Readme.md"
)

$missing = @()

foreach ($relativePath in $requiredFiles) {
    $fullPath = Join-Path $repoRoot $relativePath
    if (-not (Test-Path -LiteralPath $fullPath)) {
        $missing += $relativePath
    }
}

if ($missing.Count -gt 0) {
    throw "Missing expected GitHub Pages files:`n - $($missing -join "`n - ")"
}
```

- [ ] **Step 2: Run test to verify it fails**

Run: `powershell -ExecutionPolicy Bypass -File C:/Users/PortableDEV/Desktop/FROG/scripts/verify-github-pages.ps1`
Expected: FAIL with missing `.nojekyll`, `index.html`, `404.html`, `_sidebar.md`, and `_navbar.md`.

- [ ] **Step 3: Expand the smoke-check to cover Docsify behavior**

```powershell
$indexHtml = Get-Content -LiteralPath (Join-Path $repoRoot "index.html") -Raw

foreach ($token in @(
    'homepage: "Readme.md"',
    'loadSidebar: true',
    'loadNavbar: true',
    'function resolveLocalAssetUrl',
    'function resolveLocalDocLink',
    'function resolveLocalAssetHref',
    'hook.beforeEach',
    'hook.doneEach'
)) {
    if ($indexHtml -notmatch [regex]::Escape($token)) {
        throw "index.html is missing expected token: $token"
    }
}
```

- [ ] **Step 4: Run test to verify it still fails for the right reason**

Run: `powershell -ExecutionPolicy Bypass -File C:/Users/PortableDEV/Desktop/FROG/scripts/verify-github-pages.ps1`
Expected: FAIL because the Pages shell is still absent, not because the script itself is invalid.

### Task 2: Add the root GitHub Pages shell

**Files:**
- Create: `C:/Users/PortableDEV/Desktop/FROG/index.html`
- Create: `C:/Users/PortableDEV/Desktop/FROG/404.html`
- Create: `C:/Users/PortableDEV/Desktop/FROG/.nojekyll`

- [ ] **Step 1: Write the minimal Pages shell implementation**

```html
<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>FROG Specification</title>
</head>
<body>
  <div id="app">Loading FROG documentation...</div>
</body>
</html>
```

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <meta http-equiv="refresh" content="0; url=./#/">
  <script>window.location.replace("./#/" + window.location.pathname.replace(/^\//, ""));</script>
</head>
<body></body>
</html>
```

```text

```

- [ ] **Step 2: Replace the minimal shell with the full Docsify implementation**

```javascript
window.$docsify = {
  name: "FROG",
  repo: "Graiphic/FROG",
  homepage: "Readme.md",
  loadSidebar: true,
  loadNavbar: true,
  auto2top: true,
  subMaxLevel: 2,
  maxLevel: 3
};
```

Add:
- dark-first documentation styling adapted from the GO Whitepapers shell
- a theme toggle
- markdown link rewriting for `Readme.md` entry points
- image and asset rewriting for relative `FROG logo.svg` and `frog-orville-chart.png` references

- [ ] **Step 3: Run the smoke-check to verify the shell now satisfies file-level expectations**

Run: `powershell -ExecutionPolicy Bypass -File C:/Users/PortableDEV/Desktop/FROG/scripts/verify-github-pages.ps1`
Expected: PASS file existence checks and any token checks covered by the current implementation.

### Task 3: Add focused navigation for the first-pass documentation map

**Files:**
- Create: `C:/Users/PortableDEV/Desktop/FROG/_sidebar.md`
- Create: `C:/Users/PortableDEV/Desktop/FROG/_navbar.md`

- [ ] **Step 1: Write the failing navigation expectations into the smoke-check**

```powershell
$sidebar = Get-Content -LiteralPath (Join-Path $repoRoot "_sidebar.md") -Raw
$navbar = Get-Content -LiteralPath (Join-Path $repoRoot "_navbar.md") -Raw

foreach ($token in @(
    '](#/Readme.md)',
    '](#/Expression/Readme.md)',
    '](#/Language/Readme.md)',
    '](#/IR/Readme.md)',
    '](#/Libraries/Readme.md)',
    '](#/Profiles/Readme.md)',
    '](#/IDE/Readme.md)',
    '](#/Examples/Readme.md)',
    '](#/Conformance/Readme.md)',
    '](#/Implementations/Reference/Readme.md)',
    '](#/Roadmap/Readme.md)',
    '](#/Strategy/Heilmeier/Readme.md)'
)) {
    if ($sidebar -notmatch [regex]::Escape($token)) {
        throw "_sidebar.md is missing expected navigation token: $token"
    }
}

foreach ($token in @(
    '](#/Readme.md)',
    '](#/Examples/Readme.md)',
    '](#/Conformance/Readme.md)',
    '](#/GOVERNANCE.md)',
    '](#/CONTRIBUTING.md)'
)) {
    if ($navbar -notmatch [regex]::Escape($token)) {
        throw "_navbar.md is missing expected navigation token: $token"
    }
}
```

- [ ] **Step 2: Run test to verify it fails**

Run: `powershell -ExecutionPolicy Bypass -File C:/Users/PortableDEV/Desktop/FROG/scripts/verify-github-pages.ps1`
Expected: FAIL with missing navigation tokens until `_sidebar.md` and `_navbar.md` are populated.

- [ ] **Step 3: Write the minimal navigation files**

```markdown
- [Home](#/Readme.md)
- [Expression](#/Expression/Readme.md)
- [Language](#/Language/Readme.md)
- [IR](#/IR/Readme.md)
- [Libraries](#/Libraries/Readme.md)
- [Profiles](#/Profiles/Readme.md)
- [IDE](#/IDE/Readme.md)
- [Examples](#/Examples/Readme.md)
- [Conformance](#/Conformance/Readme.md)
- [Reference Implementation](#/Implementations/Reference/Readme.md)
- [Roadmap](#/Roadmap/Readme.md)
- [Strategy](#/Strategy/Heilmeier/Readme.md)
```

```markdown
- [Overview](#/Readme.md)
- [Examples](#/Examples/Readme.md)
- [Conformance](#/Conformance/Readme.md)
- [Governance](#/GOVERNANCE.md)
- [Contributing](#/CONTRIBUTING.md)
```

- [ ] **Step 4: Run the smoke-check to verify navigation coverage**

Run: `powershell -ExecutionPolicy Bypass -File C:/Users/PortableDEV/Desktop/FROG/scripts/verify-github-pages.ps1`
Expected: PASS navigation token checks.

### Task 4: Polish verification and align the landing experience

**Files:**
- Modify: `C:/Users/PortableDEV/Desktop/FROG/Readme.md`
- Modify: `C:/Users/PortableDEV/Desktop/FROG/scripts/verify-github-pages.ps1`

- [ ] **Step 1: Add minimal landing-page polish only if needed for Docsify home readability**

```markdown
## Quick Navigation

- [Read the Expression layer](./Expression/Readme.md)
- [Read the Language layer](./Language/Readme.md)
- [Browse examples](./Examples/Readme.md)
- [Inspect conformance material](./Conformance/Readme.md)
```

Only keep this step if the existing landing page needs faster entry points once rendered inside Docsify.

- [ ] **Step 2: Finalize smoke-check coverage**

```powershell
foreach ($token in @(
    'theme-toggle',
    'function applyTheme',
    'function ensureThemeToggle',
    '.sidebar-nav a[href]',
    '.app-nav a[href]'
)) {
    if ($indexHtml -notmatch [regex]::Escape($token)) {
        throw "index.html is missing expected Pages UX token: $token"
    }
}

Write-Host "GitHub Pages smoke checks passed."
```

- [ ] **Step 3: Run final verification**

Run: `powershell -ExecutionPolicy Bypass -File C:/Users/PortableDEV/Desktop/FROG/scripts/verify-github-pages.ps1`
Expected: PASS with `GitHub Pages smoke checks passed.`

- [ ] **Step 4: Review the resulting diff**

Run: `git -C C:/Users/PortableDEV/Desktop/FROG status --short`
Expected: only the design/plan docs plus the new Pages shell files and any intentional root README adjustment.
