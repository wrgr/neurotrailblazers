---
description: "Standing Rule: Mobile and Desktop Performance Optimization"
globs: "**/*"
---

# Standing Rule: Mobile & Desktop Performance Standard

All pages, interactive visualizations, and components across the NeuroTrailblazers site MUST adhere to the following performance and responsiveness standards:

## 1. Mobile Responsiveness & Touch Optimization
- **Viewport Adaptation**: All layouts MUST degrade gracefully to single-column layouts on viewports &le; 960px and &le; 640px.
- **Touch Targets**: All interactive buttons, lineage chips, tabs, and filters must maintain a minimum touch target area of &ge; 40–44px with active touch feedback.
- **Mobile Drawers & Sheets**: On screens &le; 768px, slide-out drawers must transition into bottom sheets (`bottom: 0; width: 100%; border-radius: 16px 16px 0 0`) with smooth scrolling to prevent overflowing off-screen.
- **Touch Gestures**: Canvas-based interactive graphs must support native single-finger panning and two-finger pinch-to-zoom alongside mouse drag/wheel interactions.

## 2. Desktop & Canvas Rendering Performance
- **On-Demand Rendering**: Canvas visualizations must only re-render when state changes (pan, zoom, node drag, filter change, hover) or during active momentum physics, pausing `requestAnimationFrame` loops when idle to prevent CPU/battery drain.
- **High-DPI Scaling**: Canvas elements must account for `window.devicePixelRatio` without rendering oversized uncompressed framebuffers.
- **Search & Filter Debouncing**: All live search, filter, and range sliders must use debouncing (150–250ms) to maintain 60 FPS without layout thrashing.
- **Large List Efficiency**: Long feeds (such as the 2,000-paper journal club list) must utilize CSS `content-visibility: auto`, `contain-intrinsic-size`, and lazy rendering.
