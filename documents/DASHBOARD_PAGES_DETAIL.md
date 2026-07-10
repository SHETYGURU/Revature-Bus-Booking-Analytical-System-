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

Here are the step-by-step layout grids, visual types, and business rationale for each page tab in your report:

### Page 1: Overview
Tracks high-level business performance, sales trends, and source yields:

1. **Top Row KPI Cards (Card (New) Visual)**:
   - **Business Value**: Solves **"What is the overall financial and volume health of our business today?"** (tracks core executive indicators at a glance).
   - **Visualization Pane**: Select **Card (new)** icon.
   - **Coordinates**: X = `15px`, Y = `85px`, Width = `1250px`, Height = `120px`.
   - **Field Wells Configuration**:
     - Drag `_Measures[Total Revenue]`, `_Measures[Total Bookings]`, `_Measures[Average Fare]`, and `_Measures[Customer Retention Rate]` into the Values box.
   - **Visual Layout & Formatting**:
     - Orientation: **`Horizontal`**, Columns: **`4`**, Card spacing: `15px`, Vertical alignment: **`Middle`**.
     - Go to Cards > Fill > upload gradients matching theme: `Bg Theme.jpg` (Revenue), `Blue Bg Theme.png` (Bookings/Retention), `Peach Bg Image.jpg` (Fare).
     - Go to Cards > Image > upload matching 3D icons (`icon_revenue.png`, `icon_bookings.png`, `icon_fare.png`, `icon_retention.png`). Set Image Fit to **`Fit`** and size to **`50px`**.
     - Go to Reference labels > Add trend labels, style backgrounds with `30%` transparency (capsule pill look).

2. **Total Bookings and Total Revenue (Dual Axis Line Chart)**:
   - **Business Value**: Solves **"Are revenue trends matching booking volume trends over the months?"** (identifies price performance alignment and booking peaks).
   - **Visualization Pane**: Select **Line Chart** icon (with secondary Y-axis).
   - **Coordinates**: X = `15px`, Y = `220px`, Width = `610px`, Height = `240px`.
   - **Field Wells Configuration**:
     - Drag `Calendar[Date]` (or Hierarchy) into the **X-axis** well.
     - Drag `_Measures[Total Bookings]` into the primary **Y-axis** well.
     - Drag `_Measures[Total Revenue]` into the **Secondary Y-axis** well.
   - **Visual Formatting**: Set `Total Bookings` line to Ocean Blue (`#054A75`), `Total Revenue` line to Arctic Cyan (`#06B6D4`), stroke width `3px`, enable **Smooth line**.

3. **Total Revenue by Bus Type (Donut Chart)**:
   - **Business Value**: Solves **"Which coach types are our main profit drivers?"** (identifies if premium sleeper vs. seater coaches generate more cash).
   - **Visualization Pane**: Select **Donut Chart** icon.
   - **Coordinates**: X = `645px`, Y = `220px`, Width = `620px`, Height = `240px`.
   - **Field Wells Configuration**:
     - Drag `buses[Bus_Type]` into the **Legend** well.
     - Drag `_Measures[Total Revenue]` into the **Values** well.
   - **Visual Formatting**: Set colors to Deep Marine Blue, Arctic Cyan, and Slate Gray. Set detail labels to **Data value, percent of total**.

4. **Total Revenue by Source (Horizontal Bar Chart)**:
   - **Business Value**: Solves **"Which starting hubs yield the highest revenue return?"** (assists with marketing campaigns and routing priority).
   - **Visualization Pane**: Select **Clustered Bar Chart** (horizontal) icon.
   - **Coordinates**: X = `15px`, Y = `475px`, Width = `610px`, Height = `230px`.
   - **Field Wells Configuration**:
     - Drag `routes[Source]` into the **Y-axis** well.
     - Drag `_Measures[Total Revenue]` into the **X-axis** well.
   - **Visual Formatting**: Set bar color to Arctic Cyan (`#06B6D4`), enable **Data labels**.

5. **Booking Status Cards (Bottom Right Card (New) Visual)**:
   - **Business Value**: Solves **"What is the status split of our bookings at this moment?"** (directly highlights cancellation volumes and pending ticket issues).
   - **Visualization Pane**: Select **Card (new)** icon.
   - **Coordinates**: X = `645px`, Y = `475px`, Width = `620px`, Height = `230px`.
   - **Field Wells Configuration**:
     - Drag custom count measures: `_Measures[Confirmed Bookings]`, `_Measures[Cancelled Bookings]`, and `_Measures[Pending Bookings]` into the Values box.
   - **Visual Formatting**: Align text to center, set border shapes. Upload outline icons (`icon_confirmed.png`, `icon_cancelled.png`, `icon_pending.png`) with size `24px`. Color borders based on status: Confirmed (Teal `#0D9488`), Cancelled (Rose Red `#EF4444`), Pending (Amber `#F59E0B`).

---

### Page 2: Bookings (Detailed Booking Status Analysis)
Focuses on tracking booking statuses, customer planning behavior, and traffic load distribution:

1. **Top Row KPI Cards (Card (New) Visual - NEW)**:
   - **Business Value**: Solves **"How healthy are our passenger booking workflows, planning lead times, and financial cancellation impacts?"** (tracks user behavior efficiency, transaction attrition, and lost sales value instead of simple volume aggregates).
   - **Visualization Pane**: Select **Card (new)** icon.
   - **Coordinates**: X = `15px`, Y = `85px`, Width = `1250px`, Height = `120px`.
   - **Field Wells Configuration**:
     - Drag `_Measures[Average Lead Time]`, `_Measures[Cancellation Rate]`, `_Measures[Revenue Leakage]`, and `_Measures[Active Route Footprint]` into the Values box.
   - **Visual Layout & Formatting**:
     - Orientation: **`Horizontal`**, Columns: **`4`**, Card spacing: `15px`, Vertical alignment: **`Middle`**.
     - Go to Cards > Fill > upload gradients matching theme: `Blue Bg Theme.png` (Lead Time / Routes), `Peach Bg Image.jpg` (Cancellation Rate), `Purple Bg Theme.jpg` (Revenue Leakage).
     - Go to Cards > Image > upload matching 3D icons (`icon_fare.png` for lead time, `icon_cancelled.png` for cancellation rate, `icon_revenue.png` for leakage, `icon_confirmed.png` for routes). Set size to **`50px`**.
     - Go to Reference labels > Add trend labels, style backgrounds with `30%` transparency (capsule pill look).

2. **Daily Bookings Volume (Area Chart)**:
   - **Business Value**: Solves **"What are our daily booking volumes and seasonal spikes?"** (helps with staffing and server infrastructure management).
   - **Visualization Pane**: Select **Area Chart** icon.
   - **Coordinates**: X = `15px`, Y = `220px`, Width = `560px`, Height = `240px`.
   - **Field Wells Configuration**:
     - Drag `Calendar[Date]` from the Data pane into the **X-axis** well.
     - Drag `_Measures[Total Bookings]` from the Data pane into the **Y-axis** well.
   - **Visual Formatting**: Set Stroke width to `3px`, Color to Ocean Blue (`#054A75`), expand **Shade area** > Turn **On** (Set transparency to `85%`, color `#E0F2FE`).

3. **Planning Behavior (Donut Chart)**:
   - **Business Value**: Solves **"Do customers book last-minute or plan in advance?"** (helps adjust dynamic pricing models and booking policies).
   - **Visualization Pane**: Select **Donut Chart** icon.
   - **Coordinates**: X = `590px`, Y = `220px`, Width = `310px`, Height = `240px`.
   - **Field Wells Configuration**:
     - Create a calculated column: `Lead Time Days = DATEDIFF(bookings[Booking_Date], bookings[Travel_Date], DAY)`.
     - Create a grouping column: `Lead Time Group = IF([Lead Time Days]=0, "Same Day", IF([Lead Time Days]<=3, "1-3 Days", IF([Lead Time Days]<=7, "4-7 Days", "8+ Days")))`.
     - Drag `Lead Time Group` into the **Legend** well.
     - Drag `_Measures[Total Bookings]` into the **Values** well.
   - **Visual Formatting**: Use light slate, ocean blue, and cyan colors for the segments.

4. **Status Split (Clustered Column Chart)**:
   - **Business Value**: Solves **"Is our cancellation volume within acceptable boundaries?"** (helps operations identify booking leakage).
   - **Visualization Pane**: Select **Clustered Column Chart** icon.
   - **Coordinates**: X = `915px`, Y = `220px`, Width = `350px`, Height = `240px`.
   - **Field Wells Configuration**:
     - Drag `bookings[Booking_Status]` into the **X-axis** well.
     - Drag `_Measures[Total Bookings]` into the **Y-axis** well.
   - **Visual Formatting**: Color columns: Confirmed = Teal (`#0D9488`), Cancelled = Rose Red (`#EF4444`), Pending = Amber / Orange (`#F59E0B`).

5. **Status vs Bus Type Matrix (Matrix Table)**:
   - **Business Value**: Solves **"Are cancellations concentrated on specific bus configurations?"** (identifies if seater or sleeper configurations experience more booking changes).
   - **Visualization Pane**: Select **Matrix** icon.
   - **Coordinates**: X = `15px`, Y = `475px`, Width = `700px`, Height = `230px`.
   - **Field Wells Configuration**:
     - Drag `buses[Bus_Type]` into the **Rows** well.
     - Drag `_Measures[Confirmed Bookings]`, `_Measures[Cancelled Bookings]`, and `_Measures[Pending Bookings]` into the **Values** well.
   - **Visual Formatting**: Cell Elements > enable Data Bars individually for each column using matching status colors.

6. **Route Demands & Traffic Load (Horizontal Clustered Bar Chart)**:
   - **Business Value**: Solves **"Which routes have the highest passenger traffic?"** (guides fleet allocation managers to dispatch extra buses to high-demand corridors).
   - **Visualization Pane**: Select **Clustered Bar Chart** (horizontal) icon.
   - **Coordinates**: X = `730px`, Y = `475px`, Width = `535px`, Height = `230px`.
   - **Field Wells Configuration**:
     - Drag `Routes[Source] & " → " & Routes[Destination]` into the **Y-axis** well.
     - Drag `_Measures[Total Bookings]` into the **X-axis** well.
   - **Visual Formatting**: Set bar color to Arctic Cyan (`#06B6D4`), enable **Data labels**.

---

### Page 3: Revenue (Yield & Yield Optimization)
Tracks cash flows, pricing trends, and revenue yields:

1. **Cumulative Revenue Trend (Line Chart)**:
   - **Business Value**: Solves **"Is our business on track to hit its total revenue goals over time?"** (tracks running cumulative totals to forecast quarterly sales).
   - **Visualization Pane**: Select **Line Chart** icon.
   - **Coordinates**: X = `15px`, Y = `85px`, Width = `610px`, Height = `280px`.
   - **Field Wells Configuration**:
     - Drag `Calendar[Year Month]` into the **X-axis** well.
     - Drag `_Measures[Total Revenue]` into the **Y-axis** well. Click down arrow > Show value as > select **Running total**.
   - **Visual Formatting**: Set Line color to Ocean Blue (`#054A75`), stroke width `3px`, turn on **Data labels**.

2. **Revenue Share by Coach Type (Donut Chart)**:
   - **Business Value**: Solves **"Which coach configuration yields the highest financial return share?"** (tells procurement if they should invest in Seaters or Sleepers).
   - **Visualization Pane**: Select **Donut Chart** icon.
   - **Coordinates**: X = `645px`, Y = `85px`, Width = `620px`, Height = `280px`.
   - **Field Wells Configuration**:
     - Drag `buses[Bus_Type]` into the **Legend** well.
     - Drag `_Measures[Total Revenue]` into the **Values** well.
   - **Visual Formatting**: Set slice colors to match theme. Enable detail labels showing values and percentages.

3. **Average Fare by Bus Type (Horizontal Bar Chart)**:
   - **Business Value**: Solves **"What is the average pricing yield for each seat configuration?"** (helps pricing teams verify that sleepers are priced sufficiently higher than seaters).
   - **Visualization Pane**: Select **Clustered Bar Chart** (horizontal) icon.
   - **Coordinates**: X = `15px`, Y = `385px`, Width = `610px`, Height = `310px`.
   - **Field Wells Configuration**:
     - Drag `buses[Bus_Type]` into the **Y-axis** well.
     - Drag `_Measures[Average Fare]` into the **X-axis** well.
   - **Visual Formatting**: Set bar color to Arctic Cyan (`#06B6D4`), turn on **Data labels**.

4. **Revenue Yield per Distance Class (Clustered Column Chart)**:
   - **Business Value**: Solves **"Are longer routes generating proportionate revenue relative to their operating distance?"** (identifies if pricing models reflect journey distance fairly).
   - **Visualization Pane**: Select **Clustered Column Chart** icon.
   - **Coordinates**: X = `645px`, Y = `385px`, Width = `620px`, Height = `310px`.
   - **Field Wells Configuration**:
     - Drag `routes[Distance]` into the **X-axis** well.
     - Drag `_Measures[Total Revenue]` into the **Y-axis** well.
     - Drag `_Measures[Average Fare]` into the **Tooltips** well.
   - **Visual Formatting**: Set column colors to Deep Marine Blue (`#0F172A`).

---

### Page 4: Customers (Demographics & Retention Profiles)
Analyzes user booking behaviors and repeat customer rates:

1. **Age Group Distribution (Clustered Column Chart)**:
   - **Business Value**: Solves **"Which age demographic is our primary customer base?"** (allows marketing to refine digital ad campaign age targets).
   - **Visualization Pane**: Select **Clustered Column Chart** icon.
   - **Coordinates**: X = `15px`, Y = `85px`, Width = `610px`, Height = `280px`.
   - **Field Wells Configuration**:
     - Drag `customers[Age_Group]` (calculated column) into the **X-axis** well.
     - Drag `_Measures[Unique Customers]` into the **Y-axis** well.
   - **Visual Formatting**: Set color to Arctic Cyan (`#06B6D4`), sort the X-axis chronologically.

2. **Customer Retention Profile (Gauge Visual)**:
   - **Business Value**: Solves **"Are we retaining customers month-over-month, or relying entirely on new acquisitions?"** (tracks customer loyalty against a high-performance 80% target).
   - **Visualization Pane**: Select **Gauge** icon.
   - **Coordinates**: X = `645px`, Y = `85px`, Width = `620px`, Height = `280px`.
   - **Field Wells Configuration**:
     - Drag `_Measures[Customer Retention Rate]` into the **Value** well.
     - Under Gauge axis > Target, set target to `0.80`.
   - **Visual Formatting**: Color active gauge area Ocean Blue (`#054A75`).

3. **Customer Bookings Leaderboard (Table)**:
   - **Business Value**: Solves **"Who are our top-value customers?"** (enables the CRM/loyalty team to distribute targeted rewards or premium memberships).
   - **Visualization Pane**: Select **Table** icon.
   - **Coordinates**: X = `15px`, Y = `385px`, Width = `1250px`, Height = `310px`.
   - **Field Wells Configuration**:
     - Drag `customers[Name]`, `customers[Gender]`, `customers[Age_Group]`, `_Measures[Total Bookings]`, and `_Measures[Total Revenue]` into the Columns well.
     - Click `Total Revenue` column header to sort descending.
   - **Visual Formatting**: Apply **Alternating rows** styling with light blue/slate accents.

---

### Page 5: Bus Types (Asset Utilization & Seat Capacity)
Analyzes which coach configurations perform best and maps the fleet composition:

1. **Seat Occupancy Rate (Gauge Visual)**:
   - **Business Value**: Solves **"Are our buses running mostly full or empty?"** (essential for capacity utilization planning).
   - **Visualization Pane**: Select **Gauge** icon.
   - **Coordinates**: X = `15px`, Y = `85px`, Width = `350px`, Height = `280px`.
   - **Field Wells Configuration**:
     - Drag `_Measures[Occupancy Rate]` into the **Value** well.
     - Under Gauge axis > Target, set target to `0.80`.
   - **Visual Formatting**: Color the active arc Deep Marine Blue (`#0F172A`).

2. **Fleet Composition (Pie Chart)**:
   - **Business Value**: Solves **"What is the configuration split of our active fleet?"** (guides procurement planning for new coaches).
   - **Visualization Pane**: Select **Pie Chart** icon.
   - **Coordinates**: X = `380px`, Y = `85px`, Width = `430px`, Height = `280px`.
   - **Field Wells Configuration**:
     - Drag `buses[Bus_Type]` into the **Legend** well.
     - Drag `buses[Bus_Number]` into the **Values** well (set aggregation type to **`Count (Distinct)`**).
   - **Visual Formatting**: Set slice colors to Deep Marine Blue (`#054A75`), Arctic Cyan (`#06B6D4`), and Slate Gray (`#64748B`).

3. **Bookings Demand by Coach (Donut Chart)**:
   - **Business Value**: Solves **"Which bus types do customers choose the most?"** (identifies if fleet composition matches consumer demand).
   - **Visualization Pane**: Select **Donut Chart** icon.
   - **Coordinates**: X = `825px`, Y = `85px`, Width = `440px`, Height = `280px`.
   - **Field Wells Configuration**:
     - Drag `buses[Bus_Type]` into the **Legend** well.
     - Drag `_Measures[Total Bookings]` into the **Values** well.
   - **Visual Formatting**: Enable detail labels showing value and percentage.

4. **Asset Yield Table (Table)**:
   - **Business Value**: Solves **"How much revenue and bookings does each specific bus number bring in?"** (helps trace mechanical maintenance schedules vs. profitability).
   - **Visualization Pane**: Select **Table** icon.
   - **Coordinates**: X = `15px`, Y = `385px`, Width = `1250px`, Height = `310px`.
   - **Field Wells Configuration**:
     - Columns: `buses[Bus_ID]`, `buses[Bus_Number]`, `buses[Bus_Type]`, `buses[Capacity]`, `_Measures[Total Bookings]`, `_Measures[Total Revenue]`, `_Measures[Occupancy Rate]`.
   - **Visual Formatting**: Alternating rows style, set headers to Deep Marine Blue.

---

### Page 6: Routes (Financial Yields per Sourced City)
Identifies the best-performing travel corridors and correlates distance with revenue output:

1. **Route Performance Matrix (Matrix)**:
   - **Business Value**: Solves **"What is the nested yield breakdown from each source city to its destinations?"** (allows route planners to check passenger volumes and seat utilization).
   - **Visualization Pane**: Select **Matrix** icon.
   - **Coordinates**: X = `15px`, Y = `85px`, Width = `780px`, Height = `280px`.
   - **Field Wells Configuration**:
     - Rows: `routes[Source]` then `routes[Destination]`.
     - Values: `_Measures[Total Bookings]`, `_Measures[Total Revenue]`, and `_Measures[Occupancy Rate]`.
   - **Formatting**: Enable **Stepped layout** for drill-down functionality.

2. **Traffic Share by Source Hub (Donut Chart)**:
   - **Business Value**: Solves **"Which city hubs generate the highest volume of bookings?"** (essential for hub scheduling and fleet parking positioning).
   - **Visualization Pane**: Select **Donut Chart** icon.
   - **Coordinates**: X = `815px`, Y = `85px`, Width = `450px`, Height = `280px`.
   - **Field Wells Configuration**:
     - Drag `routes[Source]` into the **Legend** well.
     - Drag `_Measures[Total Bookings]` into the **Values** well.
   - **Visual Formatting**: Set slice colors to Arctic Cyan, Ocean Blue, and Slate Gray.

3. **Top Corridors by Revenue (Horizontal Bar Chart)**:
   - **Business Value**: Solves **"What are our top revenue-producing corridors?"** (identifies main commercial corridors to safeguard and optimize).
   - **Visualization Pane**: Select **Clustered Bar Chart** (horizontal) icon.
   - **Coordinates**: X = `15px`, Y = `385px`, Width = `780px`, Height = `310px`.
   - **Field Wells Configuration**:
     - Drag `routes[Route_ID]` into the Y-axis. Drag `_Measures[Total Revenue]` into the X-axis. Drag `routes[Source]` and `routes[Destination]` into tooltips.
   - **Formatting**: Sort descending by `Total Revenue`. Set bar color to Ocean Blue (`#054A75`).

4. **Distance vs. Revenue Efficiency (Scatter Plot)**:
   - **Business Value**: Solves **"Do longer travel distances guarantee higher revenue, or are short corridors more profitable?"** (directly helps price route tickets).
   - **Visualization Pane**: Select **Scatter Chart** icon.
   - **Coordinates**: X = `815px`, Y = `385px`, Width = `450px`, Height = `310px`.
   - **Field Wells Configuration**:
     - X-axis: `routes[Distance]`, Y-axis: `_Measures[Total Revenue]`, Details: `routes[Route_ID]`.
   - **Visual Formatting**: Color plot markers Arctic Cyan (`#06B6D4`) with a dark blue outline.

---

### Page 7: Reports (Master Transaction Export Table)
Dedicated print-ready and exportable transaction ledger:

1. **Top Right Search Bar (Search Slicer)**:
   - **Business Value**: Solves **"How can customer service agents search and locate a passenger's transaction ledger by name?"**
   - **Visualization Pane**: Select **Slicer** icon.
   - **Coordinates**: X = `1000px`, Y = `15px`, Width = `250px`, Height = `50px`.
   - **Field Wells Configuration**:
     - Drag `customers[Name]` into the Field box.
   - **Visual Settings**: Style: **`Dropdown`**, click `...` visual header > select **`Search`** to enable text search, toggle **`Show "Select all"`** to **`On`**.

2. **Master Transaction Report (Table)**:
   - **Business Value**: Solves **"How can accounting/audit teams review and export our entire transaction ledger to CSV/Excel?"**
   - **Visualization Pane**: Select **Table** icon.
   - **Coordinates**: X = `15px`, Y = `85px`, Width = `1250px`, Height = `610px`.
   - **Field Wells Configuration**:
     - Drag fields in order: `bookings[Booking_ID]`, `customers[Name]`, `bookings[Booking_Date]`, `routes[Source]`, `routes[Destination]`, `buses[Bus_Type]`, `bookings[Fare_Amount]`, `bookings[Booking_Status]`.
   - **Formatting Settings**: Alternating rows style, set headers to Deep Marine Blue, verify **Export data** icon is checked **On** under visual header settings.
