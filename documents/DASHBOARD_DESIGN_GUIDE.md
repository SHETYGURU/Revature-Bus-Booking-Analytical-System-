# Dashboard Layout, Sizing & Typography Design Guide

This design guide outlines the exact canvas settings, visual grids, sizing coordinates, and typography (font sizes) required to construct the single-page **Bus Booking Dashboard** so it fits the screen perfectly under the "Fit to Page" view.

---

## 1. Canvas & Slicer Sizing

To ensure the entire dashboard fits the screen cleanly without any scrollbars:

- **Canvas Ratio**: Go to the **Format Page** settings (canvas settings) > Select **16:9 (Widescreen)**.
- **Page View**: In the top ribbon, go to the **View** tab > Select **`Fit to Page`**.
- **Page Background**: Set background to a very light gray (Hex `#F8FAFC` or `#F1F5F9`) with `0%` transparency to make the cards pop.

---

## 2. Grid Coordinates & Positioning

Use the **Properties** pane (under *General > Properties*) to set the exact dimensions and positions for all visuals:

| Row / Visual | X (Left) | Y (Top) | Width | Height |
| :--- | :--- | :--- | :--- | :--- |
| **Title Header Bar** | `15px` | `15px` | `1250px` | `60px` |
| **Top Row KPI Cards** (4 columns side-by-side) | `15px` (offset by `312px` per card) | `85px` | `295px` | `120px` |
| **Middle Left Chart** (Line Chart) | `15px` | `215px` | `610px` | `245px` |
| **Middle Right Chart** (Donut Chart) | `645px` | `215px` | `620px` | `245px` |
| **Lower Left Chart** (Bar Chart) | `15px` | `475px` | `610px` | `230px` |
| **Lower Right Slicers/Status** (Grid) | `645px` (offset for slicer boxes) | `475px` | `620px` | `230px` |

---

## 3. Font Sizes and Typography (Segoe UI / Arial)

Use the following exact font sizes and styles to match the premium, clean look of the target dashboard:

### A. Title Header (Top Left)
- **Main Dashboard Title**: **`20pt` to `22pt`**, Bold (Color: `#0F172A` / Dark Slate).
- **Subtitle**: **`10pt`**, Regular (Color: `#64748B` / Slate Gray).

### B. KPI Cards (Top Row)
- **Callout Value** (e.g. `1.47M` / `2K`): **`24pt` to `28pt`**, Bold (Color: `#FFFFFF` / White).
- **Category Label** (e.g. `Total Revenue`): **`10pt`**, Semibold (Color: `#FFFFFF` at `80%` opacity).
- **Pill/Trend Text** (e.g. `↑ 12.5% vs Last Period`): **`9pt`**, Regular/Semibold.

### C. Chart Visuals (Line, Donut, and Bar Charts)
- **Visual Titles** (e.g. "Total Revenue by Bus_Type"): **`11pt` to `12pt`**, Semibold (Color: `#1E293B`).
- **Axis Text (X-axis & Y-axis)**: **`8pt` to `9pt`**, Regular (Color: `#64748B`).
- **Axis Titles**: **`9pt`**, Semibold.
- **Donut Chart Data Labels** (Percentages/Values): **`8.5pt`**, Regular.
- **Legends**: **`8.5pt`**, Regular.

### D. Slicer Controls (Lower Right)
- **Slicer Headers** (e.g. "Booking Date", "Bus_Type"): **`9pt`**, Semibold (Color: `#1E293B`).
- **Slicer Values/Items**: **`8.5pt`**, Regular.

### E. Booking Status Mini-Cards (Bottom Right)
- **Status Value** (e.g. `1,254`): **`14pt` to `16pt`**, Bold (Color: `#0F172A`).
- **Status Label** (e.g. `Confirmed`): **`8.5pt`**, Regular (Color: `#64748B`).

---

## 4. Cards & Effects Formatting

- **Visual Borders**: Set card borders **On** (Color: Light gray `#E2E8F0`, Rounded Corners: **`8px`**).
- **Subtle Drop Shadows**: Set shadows **On** (Offset: Bottom-Right, Color: `#000000` at `90%` transparency, Blur: `8px`).
- **Padding**: Ensure margin padding inside each chart visual is set to `10px` or `12px` to prevent elements from clipping the borders.

---

## 5. Color Palette & Theming (Nordic Ocean)

To maintain the premium, cool-analytical Nordic Ocean theme, apply the following color codes across all pages:

- **Canvas Background**: Hex `#F8FAFC` (Frost White)
- **Visual Cards Background**: Hex `#FFFFFF` (Pure White)
- **Visual Card Borders**: Hex `#E2E8F0` (Light Gray, `8px` rounded corners)
- **Sidebar Navigation Bar**: Hex `#FFFFFF` (Pure White) or `#F1F5F9` (Light Slate)
- **Title Text & Section Headers**: Hex `#0F172A` (Deep Marine Blue)
- **Primary Action Accent / Highlights**: Hex `#06B6D4` (Arctic Cyan)
- **Default/Unselected State**: Hex `#64748B` (Slate Gray)
- **KPI Background Fill / Trend Pill**: Hex `#E0F2FE` (Cool Ice Blue) or `Blue Bg Theme.png`
- **Status Indicators (Data Bars / Cards)**:
  - *Confirmed*: Hex `#0D9488` (Teal) or `#06B6D4` (Cyan)
  - *Pending*: Hex `#F59E0B` (Amber)
  - *Cancelled*: Hex `#EF4444` (Rose Red)
