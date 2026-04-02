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
$navbar = Get-Content -LiteralPath (Join-Path $repoRoot "_navbar.md") -Raw
$notFound = Get-Content -LiteralPath (Join-Path $repoRoot "404.html") -Raw

foreach ($token in @(
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
    'function resolveLocalAssetUrl',
    'function resolveLocalDocLink',
    'function resolveLocalAssetHref',
    'hook.beforeEach',
    'hook.doneEach',
    '.sidebar-nav a[href]',
    '.app-nav a[href]',
    'theme-toggle',
    'function applyTheme',
    'function ensureThemeToggle',
    'repo: "Graiphic/FROG"',
    'Loading FROG documentation'
)) {
    if ($indexHtml -notmatch [regex]::Escape($token)) {
        throw "index.html is missing expected token: $token"
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
    '](/Language/Readme.md)',
    '](/IR/Readme.md)',
    '](/Libraries/Readme.md)',
    '](/Profiles/Readme.md)',
    '](/IDE/Readme.md)',
    '](/Examples/Readme.md)',
    '](/Conformance/Readme.md)',
    '](/Implementations/Reference/Readme.md)',
    '](/Roadmap/Readme.md)',
    '](/Strategy/Heilmeier/Readme.md)'
)) {
    if ($sidebar -notmatch [regex]::Escape($token)) {
        throw "_sidebar.md is missing expected navigation token: $token"
    }
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
