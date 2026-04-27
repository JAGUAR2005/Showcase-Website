# Framer Web Design Guidelines & Best Practices

This document outlines the professional web design standards based on Framer's official principles, tailored for the **Car Resale Intelligence Platform**.

## 1. Design System Architecture

### Design Tokens
- **Color Styles**:
    - **Primary**: `#3b82f6` (Electric Blue) - Use for primary actions and system highlights.
    - **Background**: `#010a12` (Deep Navy) - Base for the dark mode persona.
    - **Surface**: `rgba(255, 255, 255, 0.03)` - For glass cards and panels.
- **Typography Scale**:
    - **H1**: Cinematic bold, `tracking-tight`, `leading-none`.
    - **Body**: Inter / System Sans, `leading-relaxed`, `text-slate-400`.
    - **Mono**: IBM Plex Mono for technical data points and neural audit nodes.

### Components & Patterns
- **Variants**: Ensure all interactive elements (buttons, nav items) have distinct Hover, Pressed, and Loading states.
- **Variables**: Use props for dynamic text (e.g., predicted values, currency symbols) to keep components reusable.

## 2. Layout & Responsiveness

- **Max Width**: Keep content constrained to **1200px - 1400px** for readability.
- **Stacks & Gaps**: Use flexbox/grid stacks with consistent gaps (`8px`, `16px`, `24px`, `32px`).
- **Fluid Sizing**: Prefer `fill` (100% width) or `relative` units over fixed pixel widths to prevent horizontal overflow on mobile.
- **Safe Areas**: Ensure fixed elements (tickers, headers) respect device safe area insets.

## 3. Typography & Readability

- **Line Length**: Limit body text to **50–75 characters** per line.
- **Hierarchy**: Use one `H1` per page. Use `H2` for variables and dashboard sections.
- **Balanced Text**: Avoid single-word orphans in headings.

## 4. Interaction & UX

- **Visual Hierarchy**: The "Execute Valuation" CTA must remain the highest contrast element.
- **Clickable Targets**: Minimum touch target size of **44x44px**.
- **Full Container Taps**: Ensure the entire card or input group is responsive to clicks, not just the text label.

## 5. Performance & Accessibility (WCAG)

- **Contrast**: Maintain a minimum **4.5:1 ratio** for text readability.
- **Alt Text**: All data visualization plots and the hero portrait must have descriptive labels for screen readers.
- **SEO**: Use semantic HTML tags (`main`, `section`, `header`, `footer`) as implemented in the React structure.

---
*Applied to: Car Resale Intelligence Platform v5.0*
