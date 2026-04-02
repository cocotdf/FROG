# FROG GitHub Pages First Pass Design

**Date:** 2026-04-02

## Goal

Turn `Graiphic/FROG` into a clean GitHub Pages documentation experience modeled on the `GO_WhitePaper` setup, while preserving the existing repository structure and content during this first pass.

## Current State

- The repository already contains a substantial Markdown-based specification spread across architecture folders such as `Expression/`, `Language/`, `IR/`, `Libraries/`, `Profiles/`, and `IDE/`.
- The root landing document is `Readme.md`, not `README.md`.
- Many subdirectories also use `Readme.md`, which is valid in GitHub but brittle for Docsify defaults and path assumptions.
- The repository does not yet expose a GitHub Pages shell at the root.
- The repository has only a small number of shared root assets (`FROG logo.svg`, `frog-orville-chart.png`), while most content is Markdown.

## Desired Outcome

- A root GitHub Pages shell using Docsify.
- A branded landing page that presents FROG clearly and routes readers into the specification.
- A sidebar and top navigation that expose the main documentation families directly.
- Stable rendering of the existing Markdown corpus without a large rename sweep.
- Clean handling of local Markdown links and root-level assets on GitHub Pages.
- GitHub Pages compatibility through `.nojekyll` and `404.html`.

## Approach

Use the same overall pattern as `GO_WhitePaper`, adapted to the structure of `FROG`:

- Add a root `index.html` that boots Docsify and applies a clean Graiphic/FROG visual layer.
- Add `404.html` as the single-page-app fallback required by GitHub Pages.
- Add `.nojekyll` to avoid GitHub Pages filtering behavior.
- Add `_sidebar.md` and `_navbar.md` with explicit links to the root landing page and major top-level folders.
- Keep the repository landing content rooted in the existing `Readme.md` instead of renaming files in this first pass.
- Add client-side path rewriting so Docsify navigation resolves existing `Readme.md` files and local asset links correctly.

## Navigation Design

The first-pass navigation should stay focused on top-level discovery:

- Home
- Expression
- Language
- IR
- Libraries
- Profiles
- IDE
- Examples
- Conformance
- Implementations
- Roadmap
- Strategy
- Governance / Contributing references as utility links

This keeps the shell readable without trying to expose every nested specification page in the first iteration.

## Routing Strategy

Because the repository currently uses `Readme.md` widely, the Pages shell should not assume `README.md`:

- The Docsify homepage should point explicitly to `Readme.md`.
- Sidebar and navbar links should point explicitly to `.../Readme.md` for section entry points.
- Runtime link rewriting should normalize local Markdown links so directory links and same-repo file links stay navigable in GitHub Pages.
- Runtime asset rewriting should preserve correct loading for root SVG and PNG assets from nested pages.

## Visual Direction

The site should follow the same clean documentation shell principles as `GO_WhitePaper`, but tuned for FROG:

- GitHub-friendly dark-first documentation styling.
- Strong content readability for long-form architectural text.
- Light Graiphic branding rather than a heavy marketing landing page.
- Subtle hero treatment on the landing page, using the existing logo and positioning chart where useful.

## Non-Goals

- No mass rename of `Readme.md` to `README.md` in this first pass.
- No content rewrite of the FROG specification beyond minimal landing-page cleanup if needed for navigation.
- No build pipeline, bundler, or static-site generator beyond Docsify.
- No attempt to fully curate every nested document in the sidebar yet.

## Risks And Guardrails

- Docsify path assumptions can break mixed-case `Readme.md` navigation if links are not explicit.
- Large-scale renames would create noisy diffs and higher breakage risk, so they are deferred.
- The first pass should prioritize stable browsing and clean presentation over exhaustive information architecture.
