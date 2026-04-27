# Global Car Resale Intelligence: Frontend Technical Audit

## 1. Core Architecture
- **Framework**: React 19 (TypeScript)
- **Build Tool**: Vite (Ultra-fast HMR)
- **State Management**: React Hooks (`useState`, `useEffect`, `useRef`)
- **Data Fetching**: Axios with 3-second polling for real-time metric synchronization.
- **Styling**: Vanilla CSS with a centralized Variable System for "Vertical Slicing" and "Glassmorphism" aesthetics.

## 2. Visual Persona: "Vertical Slicing"
The UI follows a cinematic, high-fidelity aesthetic inspired by modern movie posters and "Awwwards" winning data dashboards.
- **Glassmorphism**: Background blurs (`backdrop-filter: blur(20px)`) and sheer border treatments simulate a multi-layered neural glass interface.
- **Typography**: Dual-layer system using **Press Start 2P** for low-level system logs and **Inter** for high-level data interpretation.
- **Color Palette**: Deep Charcoal (`#0a0a0f`) baseline with Electric Cobalt (`#3b82f6`) accents.

## 3. Animation Engine (Framer Motion)
The system uses a physics-based animation engine to provide psychological weight to data transitions.

### A. Narrative Text Animations
- **Letter-by-Letter Stagger**: Hero titles (`RESALE INTELLIGENCE`) utilize a 3D rotate-X and opacity stagger. Each character enters with a unique delay (`index * 0.04s`) for a "digital reconstruction" feel.
- **Reveal Sections**: The `RevealSection` wrapper uses `useInView` to trigger smooth Y-axis translations and opacity fades only when the user scrolls the component into the viewport.

### B. Computational Feedback
- **Animated Counters**: Numbers (R² Accuracy, FX Rates) don't jump; they "count up" using a cubic-bezier ease-out function over 1500ms, simulating a calculation in progress.
- **Status Ticker**: Fixed-position ticker simulating a live neural engine heartbeat.

## 4. The "Neural Audit" (Fracture Graphs)
The visualizations are built using **Recharts** but heavily extended with custom SVG logic and Framer Motion hooks.

### Fracture 01: Neural Heatmap (Confusion Matrix)
- **Logic**: Dynamic CSS Grid where cell background intensity is mapped to the model's classification confidence (0% to 100%).
- **Animation**: Staggered scale-in effect as the matrix enters view.

### Fracture 02: Error Stability (Residual Plot)
- **Twinkling Datapoints**: A custom `TwinklingDot` shape is applied to the Scatter Plot. Each dot pulses with a randomized duration (`1.5s - 3.5s`) and scale offset, creating a "living" data cloud.
- **Precision Zones**: Real-time rendering of the MAE (Mean Absolute Error) as reference lines to visually validate prediction clusters.
- **Live Stream**: Backend serves actual residuals from `sample_residuals.json` to ensure visual truth.

### Fracture 03: Valuation Drivers (Feature Hierarchy)
- **Gradient Spread**: Bars feature an internal `linearGradient` with a `motion.stop` animation. The gradient center oscillates back and forth, creating a liquid shimmer effect.
- **Neural Scan**: A high-contrast SVG line traverses the width of each bar on a loop, simulating the engine's "active scanning" of features like Car Age and Mileage.
- **Tip Pulse**: Rhythmic pulse at the terminal point of each bar indicating the specific "driver strength."

## 5. Live Systems
- **Dynamic FX Engine**: Integrated with `open.er-api.com`. The frontend dynamically updates the **Live FX Baseline** metric based on the user's selected market (INR for India, EUR for Europe, GBP for UK).
- **Cascading Configuration**: The form is fully reactive. Selecting a Market region reconfigures the Manufacturer list, which in turn reconfigures the specific Model list via the `models_registry.json` served by the FastAPI backend.

---
*Generated for: Global Car Resale Intelligence Platform v6.0*
