# Tableau Dashboards Worksheet-by-Worksheet Construction Manual

This document details the step-by-step configurations for all **Worksheets (Sheets)** in Tableau, followed by instructions on how to combine them into each of the 3 consolidated **Dashboards**.

---

## Global Sheet Setup Warning
Before building any dashboard, you must create all the individual worksheet tabs listed under each dashboard section below. For every worksheet, ensure:
1. **Background Shading**: Right-click the worksheet canvas > select **Format...** > under the Shading tab (paint bucket icon), set **Worksheet Background** to pure White (`#FFFFFF`) (except sparkline sheets which should be transparent or `#F8FAFC`).
2. **Font Formatting**: Set sheet titles to Tableau Semibold (`#1E293B`, `10pt`). Set labels and axes to Tableau Book (`#64748B`, `8.5pt`).

---

## Dashboard 1: Overview

### Part A: Individual Worksheets to Build First

#### 1. Sheet: `Overview - KPI Total Revenue`
*   **Fields**: Drag `[Total Revenue]` to **Text** and `[Revenue MoM %]` to **Detail**.
*   **Formatting**: Callout text is `24pt`, Bold, Color: Deep Slate (`#0F172A`). Label it: `"Total Revenue"` (`9pt`, Slate Gray `#64748B`) directly below.

#### 2. Sheet: `Overview - Revenue Sparkline Background`
*   **Columns**: Continuous `[Booking Date]` (Day level).
*   **Rows**: `[Total Revenue]`.
*   **Marks Card (Type)**: **Area Chart**. Color: Light Cyan (`#E0F2FE`), opacity: `30%`.
*   **Formatting**: Uncheck **Show Header** for both axes. Set Grid Lines, Zero Lines, and Dividers to **None**.

#### 3. Sheet: `Overview - KPI Total Bookings`
*   **Fields**: Drag `[Total Bookings]` to **Text** and `[Bookings MoM %]` to **Detail**.
*   **Formatting**: Callout text is `24pt`, Bold, Color: `#0F172A`.

#### 4. Sheet: `Overview - Bookings Sparkline Background`
*   **Columns**: Continuous `[Booking Date]` (Day level).
*   **Rows**: `[Total Bookings]`.
*   **Marks Card**: Area Chart, Color: `#E0F2FE` at `30%` opacity. Hide axes, borders, and lines.

#### 5. Sheet: `Overview - KPI Average Fare`
*   **Fields**: Drag `[Average Fare]` to **Text** and `[Average Fare MoM %]` to **Detail**.
*   **Formatting**: Callout text is `24pt`, Bold, Color: `#0F172A`.

#### 6. Sheet: `Overview - Average Fare Sparkline Background`
*   **Columns**: Continuous `[Booking Date]` (Day level).
*   **Rows**: `[Average Fare]`.
*   **Marks Card**: Area Chart, Color: `#E0F2FE` at `30%` opacity. Hide axes, borders, and lines.

#### 7. Sheet: `Overview - KPI Customer Retention`
*   **Fields**: Drag `[Customer Retention Rate]` to **Text** and `[Retention MoM %]` to **Detail**.
*   **Formatting**: Callout text is `24pt`, Bold, Color: `#0F172A`.

#### 8. Sheet: `Overview - Customer Retention Sparkline Background`
*   **Columns**: Continuous `[Booking Date]` (Day level).
*   **Rows**: `[Customer Retention Rate]`.
*   **Marks Card**: Area Chart, Color: `#E0F2FE` at `30%` opacity. Hide axes, borders, and lines.

#### 9. Sheet: `Overview - Total Bookings and Total Revenue by Month` (Dual-Axis Chart)
*   **Columns**: Continuous `[Booking Date]` (Month level).
*   **Rows**: Drag `[Total Bookings]` and `[Total Revenue]` side-by-side. Set `Total Revenue` to **Dual Axis**.
*   **Marks Card**: 
    - `Total Bookings` card: Set mark type to **Line** (smooth), Color: Ocean Blue (`#054A75`).
    - `Total Revenue` card: Set mark type to **Line** (smooth), Color: Arctic Cyan (`#06B6D4`).
*   **Title**: "Total Bookings and Total Revenue by Month".

#### 10. Sheet: `Overview - Total Revenue by Bus_Type` (Donut Chart)
*   **Angle**: `[Total Revenue]`.
*   **Color**: `[Bus Type]`. (Colors: Non-AC Sleeper `#06B6D4`, AC Sleeper `#054A75`, AC Seater `#64748B`).
*   **Cutout**: Drag double `MIN(1.0)` to Rows. Set dual axis. Change the second Marks card to Circle, color to White (`#FFFFFF`), shrink size, and add total value text.

#### 11. Sheet: `Overview - Total Revenue by Source` (Horizontal Bar Chart)
*   **Columns**: `[Total Revenue]`.
*   **Rows**: `[Source]` (sorted descending by `Total Revenue`).
*   **Color**: Solid Ocean Blue (`#054A75`). Enable data labels.

#### 12. Sheets: `Overview - Booking Status Confirmed`, `Cancelled`, & `Pending` (Icons & Text Cards)
*   **Icon Shapes Method**:
    - Copy icons (`icon_confirmed.png`, `icon_cancelled.png`, `icon_pending.png`) to `My Tableau Repository\Shapes\Custom\`.
    - Change Mark Type to **Shape**. Drag dummy field `[Status Type Label]` to Shape and Color shelves.
    - Drag corresponding measure (`[Successful Transactions]`, `[Cancelled Bookings]`, or `[Pending Bookings]`) to the Label card.
    - Assign shapes from the reloadable `Custom` palette.

#### 13. Sheet: `Overview - Occupancy Rate Semicircle Gauge` (Semicircle Gauge - **NEW**)
*   **Angle**: Drag measures `[Occupancy Rate] * 180`, `(1.0 - [Occupancy Rate]) * 180`, and bottom spacer segment `180` to Angle.
*   **Color**: Set Occupied to Ocean Blue (`#054A75`), Unoccupied to Light Gray (`#E2E8F0`), and Spacer to White (`#FFFFFF`).
*   **Rotation**: Set Pie starting angle to **`-90` degrees** under formatting.
*   **Cutout**: Drag double `AVG(0)` to Rows, make dual axis. Set second Marks card to a smaller white Circle and add the center callout label displaying `0.51` occupancy rate.

#### 14. Sheet: `Overview - Bookings by Lead Time Group Donut Chart` (Donut - **NEW**)
*   **Angle**: `[Total Bookings]`.
*   **Color**: `[Lead Time Group]` (1-3 Days, 4-7 Days, 8+ Days, Same Day).
*   **Colors**: 1-3 Days (`#054A75`), 4-7 Days (`#06B6D4`), 8+ Days (`#64748B`), Same Day (`#E0F2FE`).
*   **Cutout**: Dual axis dummy `AVG(0)` setup with a white center circle cutout.

---

### Part B: Dashboard Assembly (Overview Dashboard)
1. **Create Dashboard**: Click New Dashboard tab, set size to **Fixed size: 1280 x 1000** (height extended to fit the new row of charts).
2. **Top Navigation**: Drag a Horizontal Layout Container (`Y = 0`, Height = `60px`). Drop logo, brand texts, and 3 Nav buttons (`Overview` set as active blue, `Operations & Assets`, `Finance & Customers` as inactive slate).
3. **KPI Sparkline Row (Row 1)**: Horizontal Layout Container (`Y = 75`, Height = `100px`). Nest 4 vertical containers (White background, `#E2E8F0` border, `8px` padding). Drop text sheets, and overlay floating transparent background sparklines sent to back.
4. **Middle Upper Row (Row 2)**: Horizontal Layout Container (`Y = 190`, Height = `270px`). 
   - Left: `Overview - Total Bookings and Total Revenue by Month` (Width = `780px`, white background, card border).
   - Right: `Overview - Total Revenue by Bus_Type` donut (Width = `440px`, white background, card border).
5. **Middle Lower Row (Row 3 - NEW)**: Horizontal Layout Container (`Y = 475`, Height = `250px`).
   - Left: `Overview - Bookings by Lead Time Group Donut Chart` (Width = `620px`, white background, card border, outer padding `8px`).
   - Right: `Overview - Occupancy Rate Semicircle Gauge` (Width = `620px`, white background, card border, outer padding `8px`).
6. **Bottom Row (Row 4)**: Horizontal Layout Container (`Y = 740`, Height = `245px`).
   - Left: `Overview - Total Revenue by Source` (Width = `700px`, white background, card border).
   - Right: Horizontal Layout Container (White background, card border, `8px` padding). Nest the three status cards (`Confirmed`, `Cancelled`, `Pending`) side-by-side. Select container dropdown and check **Distribute Contents Evenly**.

---

## Dashboard 2: Operations & Assets

This dashboard consolidates operational details, assets capacity, and route metrics.

### Part A: Individual Worksheets to Build First

#### 1. Sheet: `Ops - KPI Total Bookings`
*   **Marks Card (Text)**: Drag `[Total Bookings]` to Text. Format to `24pt`, Bold, Color: `#0F172A`.

#### 2. Sheet: `Ops - KPI Occupancy Rate`
*   **Marks Card (Text)**: Drag `[Occupancy Rate]` to Text (formatted to `51%`).

#### 3. Sheet: `Ops - KPI Total Buses`
*   **Marks Card (Text)**: Drag `[Total Buses]` to Text (displays `11`).

#### 4. Sheet: `Ops - KPI Active Route Footprint`
*   **Marks Card (Text)**: Drag `[Active Route Footprint]` to Text (displays `11`).

#### 5. Sheet: `Ops - KPI Average Lead Time` (KPI Card - **NEW**)
*   **Marks Card (Text)**: Drag `[Average Lead Time]` (or `AVG([Lead Time Days])`) to Text. Format to `24pt`, Bold, Color: `#0F172A`. Label it `"Avg Lead Time"` (`9pt`, `#64748B`) directly below.

#### 6. Sheet: `Ops - Total Bookings by Booking Status` (Column Chart)
*   **Columns**: `[Booking Status]`.
*   **Rows**: `[Total Bookings]`.
*   **Color**: `[Booking Status]` (Confirmed = Teal `#0D9488`, Pending = Amber `#F59E0B`, Cancelled = Rose `#EF4444`).

#### 7. Sheet: `Ops - Total Seating Capacity and Occupied Seats by Bus Type` (Clustered Column)
*   **Columns**: `[Bus Type]` and `[Measure Names]`.
*   **Rows**: `[Measure Values]` (containing `[Total Seating Capacity]` and `[Occupied Seats]`).
*   **Color**: `[Measure Names]` (Capacity = Ocean Blue `#054A75`, Occupied = Arctic Cyan `#06B6D4`).

#### 8. Sheet: `Ops - Bookings by Lead Time Group` (Donut Chart)
*   **Angle**: `[Total Bookings]`.
*   **Color**: `[Lead Time Group]`. (Colors: Slate, Cyan, Dark Blue, Light Blue).

#### 9. Sheet: `Ops - Occupancy Rate by Distance` (Column Chart)
*   **Columns**: `[Distance]` (dimension).
*   **Rows**: `[Occupancy Rate]`.
*   **Color**: Solid Ocean Blue (`#054A75`). Enable data labels.

#### 10. Sheet: `Ops - Total Bookings by Source` (Donut Chart)
*   **Angle**: `[Total Bookings]`.
*   **Color**: `[Source]`.

#### 11. Sheet: `Ops - Asset Performance & Yield Table` (Table)
*   **Rows**: `[Bus ID]`, `[Bus Number]`, `[Bus Type]`, `[Capacity]`.
*   **Measures**: `[Total Bookings]`, `[Total Revenue]`, `[Occupancy Rate]`. Enable Row Totals.

#### 12. Sheet: `Ops - Route Performance Matrix Table` (Table)
*   **Rows**: `[Source]`, `[Destination]`, `[Route ID]`, `[Distance]`.
*   **Measures**: `[Total Bookings]`, `[Total Revenue]`, `[Occupancy Rate]`. Enable Row Totals.

---

### Part B: Dashboard Assembly (Operations & Assets Dashboard)
1. **Create Dashboard**: Click New Dashboard tab, set size to **Fixed size: 1280 x 1200** (extended vertical scrolling canvas).
2. **Top Navigation**: Drag a Horizontal Layout Container (`Y = 0`, Height = `60px`). Highlight the "Operations & Assets" button.
3. **KPI Row (Row 1)**: Horizontal Layout Container (`Y = 75`, Height = `100px`). Nest **5 vertical containers** side-by-side with white background, borders, and `8px` padding. Drop the corresponding KPI text sheets: `Total Bookings`, `Occupancy Rate`, `Total Buses`, `Active Route Footprint`, and `Average Lead Time`. Select the row container dropdown and click **Distribute Contents Evenly** for perfect spacing.
4. **Upper Row (Row 2)**: Horizontal Layout Container (`Y = 190`, Height = `280px`).
   - Left: `Ops - Total Bookings by Booking Status` (Width = `600px`, white background, border, outer padding `8px`).
   - Right: `Ops - Total Seating Capacity and Occupied Seats by Bus Type` (Width = `600px`, white background, border, outer padding `8px`).
5. **Middle Row (Row 3)**: Horizontal Layout Container (`Y = 485`, Height = `260px`).
   - Left: `Ops - Bookings by Lead Time Group` donut (Width = `390px`, white card format).
   - Center: `Ops - Occupancy Rate by Distance` column (Width = `420px`, white card format).
   - Right: `Ops - Total Bookings by Source` donut (Width = `390px`, white card format).
6. **Lower Row (Row 4)**: Horizontal Layout Container (`Y = 760`, Height = `420px`).
   - Left: `Ops - Asset Performance & Yield Table` (Width = `620px`, white card format).
   - Right: `Ops - Route Performance Matrix Table` (Width = `580px`, white card format).

---

## Dashboard 3: Finance & Customers

This dashboard consolidates revenue streams, customer metrics, and master audits.

### Part A: Individual Worksheets to Build First

#### 1. Sheet: `Finance - KPI Total Revenue`
*   **Marks Card (Text)**: Drag `[Total Revenue]` to Text. Format to `$1.24M` style.

#### 2. Sheet: `Finance - KPI Average Fare`
*   **Marks Card (Text)**: Drag `[Average Fare]` to Text (displays `$68.04` style).

#### 3. Sheet: `Finance - KPI Unique Customers`
*   **Marks Card (Text)**: Drag `[Unique Customers]` to Text (displays `288`).

#### 4. Sheet: `Finance - KPI Customer Retention Rate`
*   **Marks Card (Text)**: Drag `[Customer Retention Rate]` to Text (displays `42%`).

#### 5. Sheet: `Finance - Total Revenue by Year Month` (Area Chart)
*   **Columns**: Continuous `[Booking Date]` (Month level).
*   **Rows**: `[Total Revenue]`.
*   **Marks Card**: Area Chart, Color: `#054A75` at `15%` opacity.

#### 6. Sheet: `Finance - Average Seat Fare by Bus Type` (Horizontal Bar Chart)
*   **Columns**: `[Average Fare]`.
*   **Rows**: `[Bus Type]`.
*   **Color**: `[Bus Type]` (Slate `#64748B`, Dark Blue `#054A75`, Cyan `#06B6D4`).

#### 7. Sheet: `Finance - Customer Bookings Leaderboard Table` (Table)
*   **Rows**: `[Name]`, `[Gender]`, `[Age Group]`.
*   **Measures**: `[Total Bookings]`, `[Total Revenue]`. Sort descending by Total Revenue.

#### 8. Sheet: `Finance - Customer Retention Rate Semicircle Gauge` (Semicircle Gauge)
*   **Angle**: `[Customer Retention Rate] * 180`, `(1.0 - [Customer Retention Rate]) * 180`, and bottom spacer segment `180`.
*   **Rotation**: Starting angle set to `-90` degrees. Spacer colored to white.
*   **Cutout**: Dual axis dummy `AVG(0)` setup with center label text showing `0.42` retention rate.

#### 9. Sheet: `Finance - Unique Customers by Age Group` (Column Chart)
*   **Columns**: `[Age Group]` (45+, 25-45, Under 25).
*   **Rows**: `[Unique Customers]`.
*   **Color**: Solid Ocean Blue (`#054A75`).

#### 10. Sheet: `Finance - Master Transaction Report Table` (Table)
*   **Rows**: Drag `[Booking ID]`, `[Name]`, `[Booking Date]`, `[Source]`, `[Destination]`, `[Bus Type]`, `[Fare Amount]`, `[Booking Status]` to Rows.
*   **Formatting**: Enable row banding (white and light gray).

---

### Part B: Dashboard Assembly (Finance & Customers Dashboard)
1. **Create Dashboard**: Click New Dashboard tab, set size to **Fixed size: 1280 x 1200** (extended vertical scrolling canvas).
2. **Top Navigation**: Drag a Horizontal Layout Container (`Y = 0`, Height = `60px`). Highlight the "Finance & Customers" navigation button.
3. **KPI Row (Row 1)**: Horizontal Layout Container (`Y = 75`, Height = `100px`). Nest 4 vertical containers with white background, borders, and `8px` padding. Drop the corresponding KPI text sheets.
4. **Upper Row (Row 2)**: Horizontal Layout Container (`Y = 190`, Height = `280px`).
   - Left: `Finance - Total Revenue by Year Month` (Width = `780px`, white card format).
   - Right: `Finance - Average Seat Fare by Bus Type` (Width = `440px`, white card format).
5. **Middle Row (Row 3)**: Horizontal Layout Container (`Y = 485`, Height = `280px`).
   - Left: `Finance - Customer Bookings Leaderboard Table` (Width = `520px`, white card format).
   - Center: `Finance - Customer Retention Rate Semicircle Gauge` (Width = `380px`, white card format).
   - Right: `Finance - Unique Customers by Age Group` (Width = `340px`, white card format).
6. **Lower Row (Row 4)**: Vertical Layout Container (`Y = 780`, Height = `400px`). Set container background to White, borders to thin light gray, and outer padding to `8px`.
   - Drop the worksheet `Finance - Master Transaction Report Table` inside.
   - Click the table, go to the top-right caret dropdown > select **Filters** > click **Name**.
   - Change the filter type by clicking the filter care dropdown > select **Wildcard Match** and drag this search field to sit at the top-right header of the table container.
