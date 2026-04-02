$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot

$requiredFiles = @(
    ".nojekyll",
    "index.html",
    "404.html",
    "_sidebar.md",
    "_navbar.md",
    "Readme.md",
    "assets/open-github-pages-banner.svg",
    "scripts/build-sidebar.ps1"
)

$requiredDocs = @(
    "Readme.md",
    "Expression/Readme.md",
    "Language/Readme.md",
    "IR/Readme.md",
    "Libraries/Readme.md",
    "Profiles/Readme.md",
    "IDE/Readme.md",
    "Examples/Readme.md",
    "Conformance/Readme.md",
    "Implementations/Reference/Readme.md",
    "Roadmap/Readme.md",
    "Strategy/Heilmeier/Readme.md",
    "GOVERNANCE.md",
    "CONTRIBUTING.md"
)

$missing = @()

foreach ($relativePath in $requiredFiles + $requiredDocs) {
    $fullPath = Join-Path $repoRoot $relativePath
    if (-not (Test-Path -LiteralPath $fullPath)) {
        $missing += $relativePath
    }
}

if ($missing.Count -gt 0) {
    throw "Missing expected GitHub Pages files:`n - $($missing -join "`n - ")"
}

$rootReadme = Get-Content -LiteralPath (Join-Path $repoRoot "Readme.md") -Raw
$indexHtml = Get-Content -LiteralPath (Join-Path $repoRoot "index.html") -Raw
$sidebar = Get-Content -LiteralPath (Join-Path $repoRoot "_sidebar.md") -Raw
$sidebarLines = Get-Content -LiteralPath (Join-Path $repoRoot "_sidebar.md")
$navbar = Get-Content -LiteralPath (Join-Path $repoRoot "_navbar.md") -Raw
$notFound = Get-Content -LiteralPath (Join-Path $repoRoot "404.html") -Raw

foreach ($token in @(
    '<div class="go-pages-link" data-render-target="github">',
    'https://graiphic.github.io/FROG/',
    './assets/open-github-pages-banner.svg',
    "FROG",
    "Free Open Graphical Language",
    "repository structure",
    "Conformance/",
    "Examples/"
)) {
    if ($rootReadme -notmatch [regex]::Escape($token)) {
        throw "Readme.md is missing expected content token: $token"
    }
}

foreach ($token in @(
    'homepage: "Readme.md"',
    'loadSidebar: true',
    'loadNavbar: true',
    '.markdown-section .go-pages-link',
    '.frog-nav-branch',
    '.frog-nav-toggle',
    '.frog-nav-entry',
    'function decorateSidebarWithToggles',
    'function readSidebarToggleState',
    'function writeSidebarToggleState',
    'function buildSidebarBranchKey',
    'function branchShouldBeOpen',
    'function resolveSamePageAnchorHref',
    'function resolveLocalAssetUrl',
    'function resolveLocalDocLink',
    'function resolveLocalAssetHref',
    'hook.beforeEach',
    'hook.doneEach',
    'decorateSidebarWithToggles()',
    '.sidebar-nav a[href]',
    '.app-nav a[href]',
    'theme-toggle',
    'function applyTheme',
    'function ensureThemeToggle',
    'repo: "Graiphic/FROG"',
    'Loading FROG documentation',
    'graiphic-frog-sidebar-state',
    'rawHref.startsWith("#")',
    '?id='
)) {
    if ($indexHtml -notmatch [regex]::Escape($token)) {
        throw "index.html is missing expected token: $token"
    }
}

foreach ($token in @(
    "#0d1117",
    "#161b22",
    "#30363d",
    "#e6edf3",
    "#8b949e",
    "#58a6ff",
    "#21262d",
    "rgba(88, 166, 255, 0.06)",
    "rgba(139, 148, 158, 0.04)"
)) {
    if ($indexHtml -notmatch [regex]::Escape($token)) {
        throw "index.html is missing expected GitHub dark theme token: $token"
    }
}

foreach ($token in @(
    '--nav-shift-left: 8.75rem;',
    '.markdown-section pre,',
    '.markdown-section pre > code,',
    '.markdown-section pre > code *',
    'color: var(--body-color) !important;'
)) {
    if ($indexHtml -notmatch [regex]::Escape($token)) {
        throw "index.html is missing expected readability/nav token: $token"
    }
}

foreach ($token in @(
    'window.location.replace',
    '#/'
)) {
    if ($notFound -notmatch [regex]::Escape($token)) {
        throw "404.html is missing expected SPA fallback token: $token"
    }
}

foreach ($token in @(
    '](/)',
    '](/Expression/Readme.md)',
    '](/Expression/Cache.md)',
    '](/Expression/Control%20structures.md)',
    '](/Examples/Readme.md)',
    '](/Examples/01_pure_addition/Readme.md)',
    '](/Language/Readme.md)',
    '](/Language/Execution%20model.md)',
    '](/IR/Readme.md)',
    '](/IR/Execution%20IR.md)',
    '](/Libraries/Readme.md)',
    '](/Libraries/UI.md)',
    '](/Profiles/Readme.md)',
    '](/IDE/Readme.md)',
    '](/Conformance/Readme.md)',
    '](/Conformance/valid/01_pure_addition.md)',
    '](/Conformance/invalid/06_widget_must_not_be_promoted_to_public_interface.md)',
    '](/Implementations/Reference/Readme.md)',
    '](/Implementations/Reference/CLI/frogc.md)',
    '](/Roadmap/Readme.md)',
    '](/Roadmap/Milestones.md)',
    '](/Strategy/Heilmeier/Readme.md)'
)) {
    if ($sidebar -notmatch [regex]::Escape($token)) {
        throw "_sidebar.md is missing expected navigation token: $token"
    }
}

$expectedSidebarOrder = @(
    "- [Home](/)",
    "- [Expression](/Expression/Readme.md)",
    "- [Examples](/Examples/Readme.md)",
    "- [Language](/Language/Readme.md)",
    "- [IR](/IR/Readme.md)",
    "- [Libraries](/Libraries/Readme.md)",
    "- [Profiles](/Profiles/Readme.md)",
    "- [IDE](/IDE/Readme.md)",
    "- [Conformance](/Conformance/Readme.md)",
    "- [Reference Implementation](/Implementations/Reference/Readme.md)",
    "- [Roadmap](/Roadmap/Readme.md)",
    "- [Strategy](/Strategy/Heilmeier/Readme.md)",
    "- [Governance](/GOVERNANCE.md)",
    "- [Contributing](/CONTRIBUTING.md)",
    "- [CLA](/CLA.md)"
)

$indexedSidebarLines = @{}
for ($index = 0; $index -lt $sidebarLines.Count; $index++) {
    $indexedSidebarLines[$sidebarLines[$index].Trim()] = $index
}

$lastIndex = -1
foreach ($line in $expectedSidebarOrder) {
    if (-not $indexedSidebarLines.ContainsKey($line)) {
        throw "_sidebar.md is missing ordered root navigation line: $line"
    }

    $lineIndex = $indexedSidebarLines[$line]
    if ($lineIndex -lt $lastIndex) {
        throw "_sidebar.md root navigation order is incorrect near: $line"
    }

    $lastIndex = $lineIndex
}

foreach ($token in @(
    '](/)',
    '](/Examples/Readme.md)',
    '](/Conformance/Readme.md)',
    '](/GOVERNANCE.md)',
    '](/CONTRIBUTING.md)'
)) {
    if ($navbar -notmatch [regex]::Escape($token)) {
        throw "_navbar.md is missing expected navigation token: $token"
    }
}

foreach ($token in @(
    '](#/',
    '#/?id='
)) {
    if ($sidebar -match [regex]::Escape($token)) {
        throw "_sidebar.md still contains legacy broken navigation syntax: $token"
    }

    if ($navbar -match [regex]::Escape($token)) {
        throw "_navbar.md still contains legacy broken navigation syntax: $token"
    }
}

Write-Host "GitHub Pages smoke checks passed."
