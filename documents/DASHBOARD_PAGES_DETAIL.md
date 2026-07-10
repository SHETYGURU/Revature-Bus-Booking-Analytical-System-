# Power BI Pages & Bookmark Filter Panel Setup Guide

This guide details the configurations for your overlay **Bookmark Filter Panel** (which slides open and close on command), details page-specific filtering criteria, and provides the step-by-step layout for the visualizations across all 7 dedicated report pages.

---

## Part 1: Bookmark-Driven Sliding Filter Panel

To create a clean overlay filter pane that appears when clicking the sidebar **Filters** button and closes when clicking a **Close (X)** button:

### Step 1: Create the Filter Panel Visual Group (Duplicate per Page Tab)
Since each page tab has unique data, you will build a localized **`Filter Panel`** group on each page tab containing page-specific slicers.

**Background Panel**: Insert a **Rectangle Shape** (Insert > Shapes > Rectangle).
- Coordinates: X = `180px` (directly adjacent to the sidebar), Y = `0px`, Width = `250px`, Height = `720px`.
- Fill: Solid White (`#FFFFFF`). Border: Outline color Light Gray (`#E2E8F0`), Width: `1px`.
- Shadow: Enable a soft shadow offset to the right.

---

### Step 2: Configure the 3-State Close Button (X)
Instead of a simple text close button, use a **Blank Button** styled with the three newly generated transparent Close (X) icons to represent Default, Hover, and Pressed states:

1. Insert a **Blank Button** at the top right of the panel (X = `390px`, Y = `15px`, Width = `30px`, Height = `30px`).
2. Go to the **Format Pane > Button > Style**:
   - Set **State** to **`Default`**: 
     - Expand **Icon** > set type to **`Custom`** > Browse and upload **`assets/icon_close_slate.png`** (Sleek slate-gray outline).
   - Set **State** to **`On hover`**:
     - Expand **Icon** > set type to **`Custom`** > Browse and upload **`assets/icon_close_purple.png`** (White cross in a deep blue circle background for clear visual feedback).
   - Set **State** to **`On press`**:
     - Expand **Icon** > set type to **`Custom`** > Browse and upload **`assets/icon_close_white.png`** (Minimalist clean white cross).
3. Set **Image Fit** to **`Fit`** for all states.

---

### Step 3: Page-Specific Slicer Configurations (Inside the Overlay Panel)
Drag the appropriate slicers into the panel for each sheet:

| Page Tab | Slicer 1 (Y = `80px`) | Slicer 2 (Y = `220px`) | Slicer 3 (Y = `420px`) |
| :--- | :--- | :--- | :--- |
| **Page 1: Overview** | `Calendar[Date]` (Between Slider) | `routes[Source]` (Dropdown) | `buses[Bus_Type]` (Checkbox List) |
| **Page 2: Bookings** | `bookings[Booking_Status]` (Tile / Horizontal List) | `Calendar[Date]` (Between Slider) | `buses[Capacity]` (Numeric Range Slider) |
| **Page 3: Revenue** | `Calendar[Date]` (Between Slider) | `bookings[Fare_Amount]` (Numeric Range Slider) | `routes[Source]` (Dropdown) |
| **Page 4: Customers** | `customers[Gender]` (Tile) | `customers[Age_Group]` (Checkbox List) | `customers[Name]` (Searchable Dropdown) |
| **Page 5: Bus Types** | `buses[Bus_Type]` (Checkbox List) | `buses[Capacity]` (Numeric Range Slider) | *Leave Empty* |
| **Page 6: Routes** | `routes[Source]` (Dropdown) | `routes[Destination]` (Dropdown) | `routes[Distance]` (Numeric Range Slider) |
| **Page 7: Reports** | *No panel overlay (Uses Top Right Search Bar - See Page 7 visual guide)* | *None* | *None* |

---

### Step 4: Create local bookmarks (Selected Visuals scope)
To prevent bookmarks from affecting other pages:
1. In the **Selection Pane**, select the `Filter Panel` group you created on the active page.
2. In the **Bookmarks Pane**, click **Add** > rename to **`PageName_ShowFilters`** (e.g. `Overview_ShowFilters`).
3. Right-click the bookmark > check **Selected Visuals** (change it from *All Visuals*).
4. Uncheck **Data** on the bookmark.
5. Hide the `Filter Panel` group in the Selection Pane, add another bookmark, rename it to **`PageName_HideFilters`**, set to **Selected Visuals**, and uncheck **Data**.
6. Bind these bookmark actions to the page's sidebar **Filters** button and local **Close (X)** button.
7. Repeat this setup for Pages 1 through 6.

---

## Part 2: Page-by-Page Dedicated Visualizations

Here are the step-by-step layout grids and visual types for each page tab in your report:

### Page 1: Overview
Tracks high-level business performance, sales trends, and source yields:

1. **Top Row KPI Cards (Card (New) Visual)**:
   - **Visualization Pane**: Select **Card (new)** icon.
   - **Coordinates**: X = `100px`, Y = `85px`, Width = `1160px`, Height = `120px`.
   - **Field Wells Configuration**:
     - Drag `_Measures[Total Revenue]` into the Values box.
     - Drag `_Measures[Total Bookings]` into the Values box.
     - Drag `_Measures[Average Fare]` into the Values box.
     - Drag `_Measures[Customer Retention Rate]` into the Values box.
   - **Visual Layout & Formatting**:
     - Go to Layout > Orientation: **`Horizontal`**, Columns: **`4`**, Card spacing: `15px`, Vertical alignment: **`Middle`**.
     - Go to Callout values > Horizontal alignment: **`Left`**.
     - Go to Cards > Fill > select each series to upload background gradients:
       - *Total Revenue*: `assets/Bg Theme.jpg`
       - *Total Bookings*: `assets/Blue Bg Theme.png`
       - *Average Fare*: `assets/Peach Bg Image.jpg`
       - *Customer Retention Rate*: `assets/Blue Bg Theme.png`
     - Go to Cards > Image > select each series to upload 3D icons:
       - *Total Revenue*: `assets/icon_revenue.png` (Left-aligned, spacing `15px`, size `50px`).
       - *Total Bookings*: `assets/icon_bookings.png`.
       - *Average Fare*: `assets/icon_fare.png`.
       - *Customer Retention Rate*: `assets/icon_retention.png`.
     - Go to Reference labels > Add trend label measures as details, style backgrounds with `30%` transparency (capsule pill look), and set Alignment to **`Left`** (aligns under text).

2. **Total Bookings and Total Revenue (Dual Axis Line Chart)**:
   - **Visualization Pane**: Select **Line and Stacked Column Chart** or **Line and Clustered Column Chart** icon (or standard Line Chart with secondary Y-axis).
   - **Coordinates**: X = `100px`, Y = `220px`, Width = `570px`, Height = `240px`.
   - **Field Wells Configuration**:
     - Drag `Calendar[Date]` (or Calendar Date Hierarchy) into the **X-axis** well.
     - Drag `_Measures[Total Bookings]` into the primary **Y-axis** well.
     - Drag `_Measures[Total Revenue]` into the **Secondary Y-axis** well.
   - **Visual Formatting**:
     - Set `Total Bookings` line color to Electric Blue (`#3B82F6`), stroke width `3px`.
     - Set `Total Revenue` line color to Dark Blue (`#002D62`), stroke width `3px`.
     - Go to formatting pane > expand **Lines** > toggle **Smooth line** to **`On`**.

3. **Total Revenue by Bus_Type (Donut Chart)**:
   - **Visualization Pane**: Select **Donut Chart** icon.
   - **Coordinates**: X = `690px`, Y = `220px`, Width = `570px`, Height = `240px`.
   - **Field Wells Configuration**:
     - Drag `buses[Bus_Type]` into the **Legend** well.
     - Drag `_Measures[Total Revenue]` into the **Values** well.
   - **Visual Formatting**: Expand **Detail labels** > Label contents: select **Data value, percent of total** (displays values like `870.03K (59.01%)`).

4. **Total Revenue by Source (Horizontal Bar Chart)**:
   - **Visualization Pane**: Select **Clustered Bar Chart** (horizontal) icon.
   - **Coordinates**: X = `100px`, Y = `475px`, Width = `570px`, Height = `230px`.
   - **Field Wells Configuration**:
     - Drag `routes[Source]` into the **Y-axis** well.
     - Drag `_Measures[Total Revenue]` into the **X-axis** well.
   - **Visual Formatting**: Set bar color to Solid Blue (`#1E88E5`), enable **Data labels**.

5. **Booking Status Cards (Bottom Right Card (New) Visual)**:
   - **Visualization Pane**: Select **Card (new)** icon.
   - **Coordinates**: X = `690px`, Y = `475px`, Width = `570px`, Height = `230px`.
   - **Field Wells Configuration**:
     - Drag these custom status count measures into the Values box:
       1. Cancelled Bookings: `COUNTROWS(FILTER(bookings, bookings[Booking_Status] = "Cancelled"))`
       2. Confirmed Bookings: `COUNTROWS(FILTER(bookings, bookings[Booking_Status] = "Confirmed"))`
       3. Pending Bookings: `COUNTROWS(FILTER(bookings, bookings[Booking_Status] = "Pending"))`
   - **Visual Formatting**:
     - Align card values to the center.
     - Go to Cards > Image > upload corresponding outline icons (`icon_cancelled.png`, `icon_confirmed.png`, `icon_pending.png`). Set Image Fit to **`Fit`** and size to **`24px`**.

---

### Page 2: Bookings (Detailed Booking Status Analysis)
Focuses on tracking booking statuses, customer planning behavior, and traffic load distribution:

1. **Daily Bookings Volume (Area Chart)**:
   - **Visualization Pane**: Select **Area Chart** icon.
   - **Coordinates**: X = `15px`, Y = `85px`, Width = `560px`, Height = `280px`.
   - **Field Wells Configuration**:
     - Drag `Calendar[Date]` from the Data pane into the **X-axis** well.
     - Drag `_Measures[Total Bookings]` from the Data pane into the **Y-axis** well.
   - **Visual Formatting**: Go to the format paintbrush icon > expand **Lines**:
     - Set Stroke width to `3px`.
     - Set Color to Ocean Blue (`#054A75`).
     - Expand **Shade area** > Turn **On** (Set transparency to `85%`, color `#E0F2FE`).

2. **Planning Behavior (Donut Chart - NEW)**:
   - **Business Value**: Solves **"Do customers book last-minute or plan in advance?"** (helps adjust dynamic pricing and scheduling).
   - **Visualization Pane**: Select **Donut Chart** icon.
   - **Coordinates**: X = `590px`, Y = `85px`, Width = `310px`, Height = `280px`.
   - **Field Wells Configuration**:
     - Create a calculated column: `Lead Time Days = DATEDIFF(bookings[Booking_Date], bookings[Travel_Date], DAY)`.
     - Create a grouping column: `Lead Time Group = IF([Lead Time Days]=0, "Same Day", IF([Lead Time Days]<=3, "1-3 Days", IF([Lead Time Days]<=7, "4-7 Days", "8+ Days")))`.
     - Drag `Lead Time Group` into the **Legend** well.
     - Drag `_Measures[Total Bookings]` into the **Values** well.
   - **Visual Formatting**: Use light slate, ocean blue, and cyan colors for the segments.

3. **Status Split (Clustered Column Chart)**:
   - **Visualization Pane**: Select **Clustered Column Chart** icon.
   - **Coordinates**: X = `915px`, Y = `85px`, Width = `350px`, Height = `280px`.
   - **Field Wells Configuration**:
     - Drag `bookings[Booking_Status]` into the **X-axis** well.
     - Drag `_Measures[Total Bookings]` into the **Y-axis** well.
   - **Visual Formatting**: Go to formatting paintbrush > expand **Columns** > **Colors** > select **Show all** to color each status:
     - `Confirmed` = Teal (`#0D9488`)
     - `Cancelled` = Rose Red (`#EF4444`)
     - `Pending` = Amber / Orange (`#F59E0B`)

4. **Status vs Bus Type Matrix (Matrix Table)**:
   - **Visualization Pane**: Select **Matrix** icon.
   - **Coordinates**: X = `15px`, Y = `385px`, Width = `700px`, Height = `310px`.
   - **Field Wells Configuration**:
     - Drag `buses[Bus_Type]` into the **Rows** well.
     - Drag `_Measures[Confirmed Bookings]`, `_Measures[Cancelled Bookings]`, and `_Measures[Pending Bookings]` into the **Values** well.
   - **Visual Formatting**: Under formatting, select Cell Elements > enable Data Bars individually for each column using matching colors (Teal, Rose Red, Amber).

5. **Route Demands & Traffic Load (Horizontal Clustered Bar Chart - NEW)**:
   - **Business Value**: Solves **"Which routes have the highest passenger traffic?"** (helps dispatch more buses to high-demand routes).
   - **Visualization Pane**: Select **Clustered Bar Chart** (horizontal) icon.
   - **Coordinates**: X = `730px`, Y = `385px`, Width = `535px`, Height = `310px`.
   - **Field Wells Configuration**:
     - Drag a concatenated field `Routes[Source] & " → " & Routes[Destination]` into the **Y-axis** well.
     - Drag `_Measures[Total Bookings]` into the **X-axis** well.
   - **Visual Formatting**: Set bar color to Arctic Cyan (`#06B6D4`), enable **Data labels**.

---

### Page 3: Revenue (Yield & Yield Optimization)
Tracks cash flows, pricing trends, and revenue yields:

1. **Cumulative Revenue Trend (Line Chart)**:
   - **Visualization Pane**: Select **Line Chart** icon.
   - **Coordinates**: X = `200px`, Y = `85px`, Width = `650px`, Height = `280px`.
   - **Field Wells Configuration**:
     - Drag `Calendar[Year Month]` into the **X-axis** well.
     - Drag `_Measures[Total Revenue]` into the **Y-axis** well. 
     - *To show running cumulative total*: Click the down arrow next to `Total Revenue` inside the Y-axis well > hover over **Show value as** > select **Running total**.
   - **Visual Formatting**: Set Line stroke width to `3px`, Color to Indigo (`#4F46E5`), and turn **Data labels** to **`On`**.

2. **Average Fare by Bus Type (Horizontal Bar Chart)**:
   - **Visualization Pane**: Select **Clustered Bar Chart** (horizontal) icon.
   - **Coordinates**: X = `870px`, Y = `85px`, Width = `380px`, Height = `280px`.
   - **Field Wells Configuration**:
     - Drag `buses[Bus_Type]` into the **Y-axis** well.
     - Drag `_Measures[Average Fare]` into the **X-axis** well.
   - **Visual Formatting**: Set bar color to warm amber (`#F59E0B`), turn on **Data labels**.

3. **Revenue Yield per Distance Class (Clustered Column Chart)**:
   - **Visualization Pane**: Select **Clustered Column Chart** icon.
   - **Coordinates**: X = `200px`, Y = `385px`, Width = `1050px`, Height = `310px`.
   - **Field Wells Configuration**:
     - Drag `routes[Distance_km]` into the **X-axis** well.
     - Drag `_Measures[Total Revenue]` into the **Y-axis** well.
     - Drag `_Measures[Average Fare]` into the **Tooltips** well (so hover-overs show both revenue and average fare yield).

---

### Page 4: Customers (Demographics & Retention Profiles)
Analyzes user booking behaviors and repeat customer rates. 

*Before building, create an **Age Group** calculated column:*
- Select the `customers` table in the Data pane > click **New Column** in the Modeling ribbon:
  ```dax
  Age_Group = IF(customers[Age] < 25, "Under 25", IF(customers[Age] <= 45, "25-45", "45+"))
  ```

1. **Customer Bookings Leaderboard (Table)**:
   - **Visualization Pane**: Select **Table** icon.
   - **Coordinates**: X = `200px`, Y = `85px`, Width = `650px`, Height = `590px`.
   - **Field Wells Configuration**:
     - Drag these fields into the **Columns** well in this order:
       1. `customers[Name]`
       2. `customers[Gender]`
       3. `customers[Age_Group]`
       4. `_Measures[Total Bookings]`
       5. `_Measures[Total Revenue]`
     - *Sorting*: Click on the `Total Revenue` column header in the table visual once loaded to sort the list in descending order.

2. **Age Group Distribution (Clustered Column Chart)**:
   - **Visualization Pane**: Select **Clustered Column Chart** icon.
   - **Coordinates**: X = `870px`, Y = `85px`, Width = `380px`, Height = `280px`.
   - **Field Wells Configuration**:
     - Drag `customers[Age_Group]` into the **X-axis** well.
     - Drag `_Measures[Unique Customers]` into the **Y-axis** well.
   - **Visual Formatting**: Sort the X-axis chronologically: Click the `...` on the visual > Sort Axis > select `Age_Group`.

3. **Customer Retention Profile (Gauge Visual)**:
   - **Visualization Pane**: Select **Gauge** icon.
   - **Coordinates**: X = `870px`, Y = `385px`, Width = `380px`, Height = `280px`.
   - **Field Wells Configuration**:
     - Drag `_Measures[Customer Retention Rate]` into the **Value** well.
     - Under **Target value** in the formatting pane (Visual > Gauge axis > Target), set the static value to `0.80` (representing the 80% customer retention goal).

---

### Page 5: Bus Types (Asset Utilization & Seat Capacity)
Analyzes which coach configurations perform best and maps the fleet composition:

1. **Seat Occupancy Rate (Gauge Visual)**:
   - **Visualization Pane**: Select **Gauge** icon.
   - **Coordinates**: X = `15px`, Y = `85px`, Width = `350px`, Height = `280px`.
   - **Field Wells Configuration**:
     - Drag `_Measures[Occupancy Rate]` into the **Value** well.
     - Under the formatting pane (Visual > Gauge axis > Target), set the target value to `0.80` (80% load factor capacity target).
   - **Visual Formatting**: Color the active arc Deep Marine Blue (`#0F172A`).

2. **Fleet Composition (Pie Chart 1 - NEW)**:
   - **Business Value**: Solves **"What is the configuration split of our active fleet?"** (helps with resource and procurement planning).
   - **Visualization Pane**: Select **Pie Chart** icon.
   - **Coordinates**: X = `380px`, Y = `85px`, Width = `430px`, Height = `280px`.
   - **Field Wells Configuration**:
     - Drag `buses[Bus_Type]` into the **Legend** well.
     - Drag `buses[Bus_Number]` into the **Values** well (set aggregation type to **`Count (Distinct)`**).
   - **Visual Formatting**: Set slice colors to Deep Marine Blue (`#054A75`), Arctic Cyan (`#06B6D4`), and Slate Gray (`#64748B`).

3. **Bookings Demand by Coach (Donut Chart 2 - NEW)**:
   - **Business Value**: Solves **"Which bus types do customers choose the most?"** (directly guides purchase decisions for high-demand configurations).
   - **Visualization Pane**: Select **Donut Chart** icon.
   - **Coordinates**: X = `825px`, Y = `85px`, Width = `440px`, Height = `280px`.
   - **Field Wells Configuration**:
     - Drag `buses[Bus_Type]` into the **Legend** well.
     - Drag `_Measures[Total Bookings]` into the **Values** well.
   - **Visual Formatting**: Enable detail labels showing value and percentage. Color match slices to the fleet composition chart.

4. **Asset Yield Table (Table)**:
   - **Visualization Pane**: Select **Table** icon.
   - **Coordinates**: X = `15px`, Y = `385px`, Width = `1250px`, Height = `310px`.
   - **Field Wells Configuration**:
     - Drag these fields into the **Columns** well in this order:
       1. `buses[Bus_ID]`
       2. `buses[Bus_Number]`
       3. `buses[Bus_Type]`
       4. `buses[Capacity]`
       5. `_Measures[Total Bookings]`
       6. `_Measures[Total Revenue]`
       7. `_Measures[Occupancy Rate]`
   - **Visual Formatting**: Under style presets, select **Minimal** or **Alternating rows** (using Hex `#F8FAFC`). Color column headers Deep Marine Blue.

---

### Page 6: Routes (Financial Yields per Sourced City)
Identifies the best-performing travel corridors and correlates distance with revenue output:

1. **Route Performance Matrix (Matrix)**:
   - **Visualization Pane**: Select **Matrix** icon.
   - **Coordinates**: X = `15px`, Y = `85px`, Width = `780px`, Height = `280px`.
   - **Field Wells Configuration**:
     - Drag `routes[Source]` and then `routes[Destination]` into the **Rows** well (in that order, to create a nestable hierarchy).
     - Drag `_Measures[Total Bookings]`, `_Measures[Total Revenue]`, and `_Measures[Occupancy Rate]` into the **Values** well.
   - **Formatting**: Expand **Row headers** in style options > Turn **On** the **Stepped layout** (this lets users click the `+` sign next to a source city to expand and view destinations).

2. **Traffic Share by Source Hub (Donut Chart - NEW)**:
   - **Business Value**: Solves **"Which city hubs generate the highest volume of bookings?"** (essential for hub scheduling and fleet parking positioning).
   - **Visualization Pane**: Select **Donut Chart** icon.
   - **Coordinates**: X = `815px`, Y = `85px`, Width = `450px`, Height = `280px`.
   - **Field Wells Configuration**:
     - Drag `routes[Source]` into the **Legend** well.
     - Drag `_Measures[Total Bookings]` into the **Values** well.
   - **Visual Formatting**: Set slice colors to match the cool Nordic Ocean theme (Arctic Cyan, Ocean Blue, Slate Gray).

3. **Top Corridors by Revenue (Horizontal Bar Chart)**:
   - **Visualization Pane**: Select **Clustered Bar Chart** (horizontal) icon.
   - **Coordinates**: X = `15px`, Y = `385px`, Width = `780px`, Height = `310px`.
   - **Field Wells Configuration**:
     - Drag `routes[Route_ID]` (or corridor) into the **Y-axis** well.
     - Drag `_Measures[Total Revenue]` into the **X-axis** well.
     - Drag `routes[Source]` and `routes[Destination]` into the **Tooltips** well.
   - **Formatting**: Sort the visual descending: click `...` on the visual > Sort Axis > select `Total Revenue`. Set bar color to Ocean Blue (`#054A75`).

4. **Distance vs. Revenue Efficiency (Scatter Plot - NEW)**:
   - **Business Value**: Solves **"Do longer travel distances guarantee higher revenue, or are short corridors more profitable?"** (directly helps price route tickets).
   - **Visualization Pane**: Select **Scatter Chart** icon.
   - **Coordinates**: X = `815px`, Y = `385px`, Width = `450px`, Height = `310px`.
   - **Field Wells Configuration**:
     - Drag `routes[Distance]` into the **X-axis** well.
     - Drag `_Measures[Total Revenue]` into the **Y-axis** well.
     - Drag `routes[Route_ID]` (or the source-destination path) into the **Values / Details** well.
   - **Visual Formatting**: Enable gridlines, color plot markers Arctic Cyan (`#06B6D4`) with a dark blue outline, and enable zoom sliders.

---

### Page 7: Reports (Master Transaction Export Table)
Dedicated print-ready and exportable transaction ledger:

1. **Top Right Search Bar (Search Slicer)**:
   - **Visualization Pane**: Select **Slicer** icon.
   - **Coordinates**: X = `1000px`, Y = `25px`, Width = `250px`, Height = `50px`.
   - **Field Wells Configuration**:
     - Drag `customers[Name]` into the **Field** box.
   - **Visual Settings**:
     - Under Slicer Settings > Style: Select **`Dropdown`**.
     - Click the `...` (More options) on the visual header > Select **`Search`** (this adds a text entry field inside the dropdown, turning it into an interactive text search bar).
     - Selection Settings: Toggle **`Show "Select all"`** to **`On`**.

2. **Master Transaction Report (Table)**:
   - **Visualization Pane**: Select **Table** icon.
   - **Coordinates**: X = `200px`, Y = `85px`, Width = `1050px`, Height = `610px`.
   - **Field Wells Configuration**:
     - Drag these fields into the **Columns** well in this order:
       1. `bookings[Booking_ID]`
       2. `customers[Name]`
       3. `bookings[Booking_Date]`
       4. `routes[Source]`
       5. `routes[Destination]`
       6. `buses[Bus_Type]`
       7. `bookings[Fare_Amount]`
       8. `bookings[Booking_Status]`
   - **Formatting Settings**:
     - Go to Style presets > select **Alternating rows** (renders light gray alternating rows).
     - Go to Column headers > set font size to `10pt`, Bold.
     - Under **Visual Headers**, ensure **Export data** icon is checked **On** (enables users to export this table to a CSV/Excel file in the Power BI Service).

