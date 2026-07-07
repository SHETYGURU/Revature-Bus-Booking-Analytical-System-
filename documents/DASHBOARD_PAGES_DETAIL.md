# Power BI Pages & Bookmark Filter Panel Setup Guide

This guide details the configurations for your overlay **Bookmark Filter Panel** (which slides open and close on command) and provides the step-by-step layout for the visualizations across all 7 dedicated report pages.

---

## Part 1: Bookmark-Driven Sliding Filter Panel

To create a clean overlay filter pane that appears when clicking the sidebar **Filters** button and closes when clicking a **Close (X)** button:

### Step 1: Create the Filter Panel Visual Group
On your canvas, build the filter container directly next to the sidebar:
1. **Background Panel**: Insert a **Rectangle Shape** (Insert > Shapes > Rectangle).
   - Coordinates: X = `180px` (directly adjacent to the sidebar), Y = `0px`, Width = `250px`, Height = `720px`.
   - Fill: Solid White (`#FFFFFF`). Border: Outline color Light Gray (`#E2E8F0`), Width: `1px`.
   - Shadow: Enable a soft shadow offset to the right.
2. **Close Button (X)**: Insert a **Blank Button** at the top right of the panel (X = `390px`, Y = `15px`, Width = `30px`, Height = `30px`).
   - Format Style: Under Text, toggle **On**, set value to `X`. Font: `Segoe UI Bold`, size `12pt`, color Slate Gray (`#64748B`).
3. **Place the Slicers**: Drag your 3 existing slicers into this panel:
   - **Date Range Slicer** (Y = `80px`)
   - **Source/Destination Slicer** (Y = `220px`)
   - **Bus Type Slicer** (Y = `420px`)
4. **Group the Elements**:
   - Go to the **View** ribbon > select and open the **Selection Pane**.
   - Select all 5 visual elements (the panel rectangle, the close button, and the 3 slicers) by holding `Ctrl`.
   - Right-click one of the selected items > select **Group** > rename this group to **`Filter Panel`**.

---

### Step 2: Create the Toggle Bookmarks
1. Go to the **View** ribbon > select and open the **Bookmarks Pane**.
2. **Configure "Show Filters" Bookmark**:
   - In the **Selection Pane**, click the eye icon next to **`Filter Panel`** to make it **Visible**.
   - In the **Bookmarks Pane**, click **Add** > rename the bookmark to **`Show Filters`**.
3. **Configure "Hide Filters" Bookmark**:
   - In the **Selection Pane**, click the eye icon next to **`Filter Panel`** to make it **Hidden**.
   - In the **Bookmarks Pane**, click **Add** > rename the bookmark to **`Hide Filters`**.
4. **CRITICAL STEP (Uncheck Data)**:
   - In the Bookmarks pane, click the three dots `...` next to both **`Show Filters`** and **`Hide Filters`** bookmarks.
   - **Uncheck "Data"** (ensure there is no checkmark next to *Data*).
   - *Why?* This ensures that opening or closing the filter panel only controls visual visibility and does *not* reset any active filter choices made by the user.

---

### Step 3: Assign Actions to Buttons
1. **Filters Sidebar Button** (On the main sidebar):
   - Select the `Filters` button.
   - In the Format pane, expand **Action** > toggle it **On**.
   - Set Type to **`Bookmark`**, and select Bookmark: **`Show Filters`**.
2. **Close Button (X)** (Inside the filter panel):
   - Select the `X` button.
   - In the Format pane, expand **Action** > toggle it **On**.
   - Set Type to **`Bookmark`**, and select Bookmark: **`Hide Filters`**.

Test it by holding `Ctrl` and clicking the buttons on your canvas!

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
       - *Customer Retention Rate*: `assets/Purple Bg Theme.jpg`
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
Focuses on tracking booking statuses, volume metrics, and capacity:

1. **Daily Bookings Volume (Area Chart)**:
   - **Visualization Pane**: Select **Area Chart** icon.
   - **Coordinates**: X = `200px`, Y = `85px`, Width = `650px`, Height = `280px`.
   - **Field Wells Configuration**:
     - Drag `Calendar[Date]` from the Data pane into the **X-axis** well.
     - Drag `_Measures[Total Bookings]` from the Data pane into the **Y-axis** well.
     - Leave **Legend** and **Small multiples** empty.
   - **Visual Formatting**: Go to the format paintbrush icon > expand **Lines**:
     - Set Stroke width to `3px`.
     - Set Color to Electric Blue (`#3B82F6`).
     - Expand **Shade area** > Turn **On** (Set transparency to `80%`, color `#D1E8FF`).

2. **Status Split (Clustered Column Chart)**:
   - **Visualization Pane**: Select **Clustered Column Chart** icon.
   - **Coordinates**: X = `870px`, Y = `85px`, Width = `380px`, Height = `280px`.
   - **Field Wells Configuration**:
     - Drag `bookings[Booking_Status]` into the **X-axis** well.
     - Drag `_Measures[Total Bookings]` into the **Y-axis** well.
   - **Visual Formatting**: Go to formatting paintbrush > expand **Columns** > **Colors** > select **Show all** to color each status:
     - `Confirmed` = Green (`#10B981`)
     - `Cancelled` = Red (`#EF4444`)
     - `Pending` = Orange (`#F59E0B`)

3. **Status vs Bus Type Matrix (Matrix Table)**:
   - **Visualization Pane**: Select **Matrix** icon.
   - **Coordinates**: X = `200px`, Y = `385px`, Width = `1050px`, Height = `310px`.
   - **Field Wells Configuration**:
     - Drag `buses[Bus_Type]` into the **Rows** well.
     - Drag `bookings[Booking_Status]` into the **Columns** well.
     - Drag `_Measures[Total Bookings]` into the **Values** well.
   - **Visual Formatting**:
     - Expand **Subtotals** > turn **On** for both rows and columns.
     - Select `[Total Bookings]` under Values in the build pane > click the down arrow > select **Conditional Formatting** > **Data Bars** > set positive bar color to light blue.

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
Analyzes which coach configurations perform best:

1. **Seat Occupancy Rate (Gauge Visual)**:
   - **Visualization Pane**: Select **Gauge** icon.
   - **Coordinates**: X = `200px`, Y = `85px`, Width = `380px`, Height = `280px`.
   - **Field Wells Configuration**:
     - Drag `_Measures[Occupancy Rate]` into the **Value** well.
     - Under the formatting pane (Visual > Gauge axis > Target), set the target value to `0.80` (80% load factor capacity target).

2. **Total Revenue by Coach Configuration (Pie Chart)**:
   - **Visualization Pane**: Select **Pie Chart** icon.
   - **Coordinates**: X = `600px`, Y = `85px`, Width = `650px`, Height = `280px`.
   - **Field Wells Configuration**:
     - Drag `buses[Bus_Type]` into the **Legend** well.
     - Drag `_Measures[Total Revenue]` into the **Values** well.

3. **Asset Yield Table (Table)**:
   - **Visualization Pane**: Select **Table** icon.
   - **Coordinates**: X = `200px`, Y = `385px`, Width = `1050px`, Height = `310px`.
   - **Field Wells Configuration**:
     - Drag these fields into the **Columns** well in this order:
       1. `buses[Bus_ID]`
       2. `buses[Bus_Number]`
       3. `buses[Bus_Type]`
       4. `buses[Capacity]`
       5. `_Measures[Total Bookings]`
       6. `_Measures[Total Revenue]`
       7. `_Measures[Occupancy Rate]`

---

### Page 6: Routes (Financial Yields per Sourced City)
Identifies the best-performing travel corridors:

1. **Route Performance Matrix (Matrix)**:
   - **Visualization Pane**: Select **Matrix** icon.
   - **Coordinates**: X = `200px`, Y = `85px`, Width = `1050px`, Height = `280px`.
   - **Field Wells Configuration**:
     - Drag `routes[Source]` and then `routes[Destination]` into the **Rows** well (in that order, to create a nestable hierarchy).
     - Drag `_Measures[Total Bookings]`, `_Measures[Total Revenue]`, and `_Measures[Occupancy Rate]` into the **Values** well.
   - **Formatting**: Expand **Row headers** in style options > Turn **On** the **Stepped layout** (this lets users click the `+` sign next to a source city to expand and view destinations).

2. **Top Corridors by Revenue (Horizontal Bar Chart)**:
   - **Visualization Pane**: Select **Clustered Bar Chart** (horizontal) icon.
   - **Coordinates**: X = `200px`, Y = `385px`, Width = `1050px`, Height = `310px`.
   - **Field Wells Configuration**:
     - Drag `routes[Route_ID]` (or corridor) into the **Y-axis** well.
     - Drag `_Measures[Total Revenue]` into the **X-axis** well.
     - Drag `routes[Source]` and `routes[Destination]` into the **Tooltips** well.
   - **Formatting**: Sort the visual descending: click `...` on the visual > Sort Axis > select `Total Revenue`.

---

### Page 7: Reports (Master Transaction Export Table)
Dedicated print-ready and exportable transaction ledger:

1. **Master Transaction Report (Table)**:
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

