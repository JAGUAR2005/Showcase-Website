# Vertical Slicing UI Overhaul

## Objective
Transform the existing data dashboard into a surreal, monochromatic, movie-poster-style interface centered around the "Vertical Slicing" design concept. The UI will convey psychological tension and introspective duality through stark Black & White contrast, an unsettling fragmented aesthetic, and deliberate, calculated whitespace.

## Key Files & Context
- `frontend/src/App.css`: The primary target for the stylistic overhaul. All "luxury-gradient" and "glassmorphism" rules will be replaced with brutalist, high-contrast, stark B&W rules and the Vertical Slicing CSS effects.
- `frontend/src/App.tsx`: Structural changes to introduce the layered `div` elements required for the vertical slicing effect. Restyling the Recharts implementation to fit the new monochromatic color scheme.

## Implementation Steps

### 1. Color Palette & Typography Refactor (`App.css`)
- **Colors**: Implement a Stark B&W + Cobalt palette.
  - Background: Deep Charcoal/Black (`#0a0a0a`).
  - Surface: Stark White (`#ffffff`) or Off-White (`#f3f4f6`) for high contrast text/borders.
  - Accent: Muted Cobalt (`#3b5998` or `#4a69bd`) to fulfill the "cool bluish tones" requirement without breaking the grayscale dominance.
- **Typography**: Switch to a more cinematic, heavy, and stark font pairing if available, utilizing calculated kerning (tracking) to enhance the movie-poster feel.

### 2. The "Vertical Slicing" Hero Effect (`App.tsx` & `App.css`)
- Introduce a new hero section that acts as the focal point.
- **Technique**: Use CSS `mask-image` with repeating linear gradients or multiple absolutely positioned `div` layers containing the same background image (e.g., `assets/hero.png` or a placeholder portrait) but with slightly shifted `background-position` or `clip-path` polygons.
- **Filter**: Apply `filter: grayscale(100%) contrast(1.2) sepia(0.2) hue-rotate(180deg)` to give the image that unsettling, cool bluish tone natively in CSS.
- **Animation**: Add a subtle, slow CSS animation (e.g., oscillating the `clip-path` or background position slightly) to create an eerie, shifting illusion of duality.

### 3. Brutalist/Minimalist Form & Dashboard Refactor (`App.tsx` & `App.css`)
- Remove all rounded corners (`border-radius: 0`), drop shadows, and glassmorphism backdrops.
- Implement strict, calculated whitespace (e.g., massive padding, distinct grid gaps).
- Use stark borders (`border: 1px solid #333` or `#e5e5e5` depending on dark/light context) for inputs and panels.
- Buttons will be inverted blocks (e.g., white text on black background, turning cobalt on hover).

### 4. Data Visualization Integration (`App.tsx`)
- Update Recharts `<AreaChart>` and other metrics to use the stark monochromatic palette.
- Replace the purple gradient fill with a stark white or muted cobalt stroke, using no fill or a sheer gray fill to maintain the unsettling minimal aesthetic.
- The `plots/*.png` images from the backend are currently loaded directly. We will apply CSS filters (`filter: grayscale(100%) invert(1)`) to make them fit seamlessly into the dark, monochromatic theme.

## Verification & Testing
1. Verify the vertical slicing effect renders smoothly across common desktop widths without horizontal scrolling.
2. Confirm the stark B&W + Cobalt palette is consistently applied to all components (nav, forms, charts).
3. Ensure the CSS animations for the slicing effect do not cause performance jank (maintain 60fps).
4. Check that the extensive whitespace does not compromise readability but enhances the intended psychological tension.
