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
*This is the summary dashboard already built on page 1 of the guide, containing:*
- **KPI Row**: Total Revenue, Total Bookings, Average Fare, Customer Retention.
- **Middle Row**: Dual-Axis Line Chart (Booking Trends) & Donut Chart (Revenue by Bus Type).
- **Bottom Row**: Horizontal Bar Chart (Revenue by Source) & Slicer/Status cards.

---

### Page 2: Bookings (Detailed Booking Status Analysis)
Focuses on tracking booking statuses, volume metrics, and capacity:

1. **Daily Bookings Volume (Area Chart)**:
   - Coordinates: X = `200px`, Y = `85px`, Width = `650px`, Height = `280px`.
   - **X-axis**: `Calendar[Date]`
   - **Y-axis**: `[Total Bookings]`
   - *Formatting*: Set line stroke to Electric Blue (`#3B82F6`) with a soft light-blue filled area underneath.
2. **Status Split (Clustered Column Chart)**:
   - Coordinates: X = `870px`, Y = `85px`, Width = `380px`, Height = `280px`.
   - **X-axis**: `bookings[Booking_Status]` (Confirmed, Cancelled, Pending)
   - **Y-axis**: `[Total Bookings]`
   - *Colors*: Confirmed = Green (`#10B981`), Cancelled = Red (`#EF4444`), Pending = Orange (`#F59E0B`).
3. **Status vs Bus Type Matrix (Matrix Table)**:
   - Coordinates: X = `200px`, Y = `385px`, Width = `1050px`, Height = `310px`.
   - **Rows**: `buses[Bus_Type]`
   - **Columns**: `bookings[Booking_Status]`
   - **Values**: `[Total Bookings]` (Enable Row & Column Subtotals and Conditional Formatting Data Bars).

---

### Page 3: Revenue (Yield & Yield Optimization)
Tracks cash flows, pricing trends, and revenue yields:

1. **Cumulative Revenue Trend (Line Chart)**:
   - Coordinates: X = `200px`, Y = `85px`, Width = `650px`, Height = `280px`.
   - **X-axis**: `Calendar[Year Month]`
   - **Y-axis**: `[Total Revenue]` (Set to show **Running Total** using Quick Measures or custom DAX).
2. **Average Fare by Bus Type (Horizontal Bar Chart)**:
   - Coordinates: X = `870px`, Y = `85px`, Width = `380px`, Height = `280px`.
   - **Y-axis**: `buses[Bus_Type]`
   - **X-axis**: `[Average Fare]`
3. **Revenue Yield per Distance Class (Clustered Column Chart)**:
   - Coordinates: X = `200px`, Y = `385px`, Width = `1050px`, Height = `310px`.
   - **X-axis**: `routes[Distance_km]` (binned)
   - **Y-axis**: `[Total Revenue]` and `[Average Fare]` (Dual Axis).

---

### Page 4: Customers (Demographics & Retention Profiles)
Analyzes user booking behaviors and repeat customer rates:

1. **Customer Bookings Leaderboard (Table)**:
   - Coordinates: X = `200px`, Y = `85px`, Width = `650px`, Height = `590px` (tall listing).
   - **Columns**: `Customers[Name]`, `Customers[Gender]`, `Customers[Age]`, `[Total Bookings]`, `[Total Revenue]`.
   - *Formatting*: Sort descending by `[Total Revenue]`.
2. **Age Group Distribution (Clustered Column Chart)**:
   - Coordinates: X = `870px`, Y = `85px`, Width = `380px`, Height = `280px`.
   - **X-axis**: Age Groups (e.g. Under 25, 25-45, 45+)
   - **Y-axis**: `[Unique Customers]`
3. **Customer Retention Profile (Gauge Visual)**:
   - Coordinates: X = `870px`, Y = `385px`, Width = `380px`, Height = `280px`.
   - **Value**: `[Customer Retention Rate]`
   - **Target**: `0.80` (80% management target).

---

### Page 5: Bus Types (Asset Utilization & Seat Capacity)
Analyzes which coach configurations perform best:

1. **Seat Occupancy Rate (Gauge Visual)**:
   - Coordinates: X = `200px`, Y = `85px`, Width = `380px`, Height = `280px`.
   - **Value**: `[Occupancy Rate]`
   - **Target**: `0.80` (80% load factor).
2. **Total Revenue by Coach configuration (Pie Chart)**:
   - Coordinates: X = `600px`, Y = `85px`, Width = `650px`, Height = `280px`.
   - **Legend**: `buses[Bus_Type]`
   - **Values**: `[Total Revenue]`
3. **Asset Yield Matrix (Table)**:
   - Coordinates: X = `200px`, Y = `385px`, Width = `1050px`, Height = `310px`.
   - **Columns**: `buses[Bus_ID]`, `buses[Bus_Type]`, `buses[Capacity]`, `[Total Bookings]`, `[Total Revenue]`, `[Occupancy Rate]`.

---

### Page 6: Routes (Financial Yields per Sourced City)
Identifies the best-performing travel corridors:

1. **Route Performance Matrix (Matrix)**:
   - Coordinates: X = `200px`, Y = `85px`, Width = `1050px`, Height = `280px`.
   - **Rows**: `routes[Source]`, `routes[Destination]` (drill-down).
   - **Values**: `[Total Bookings]`, `[Total Revenue]`, `[Average Fare]`, `[Occupancy Rate]`.
2. **Top Corridors by Revenue (Horizontal Bar Chart)**:
   - Coordinates: X = `200px`, Y = `385px`, Width = `1050px`, Height = `310px`.
   - **Y-axis**: Route Corridor (concatenated `routes[Source]` & `routes[Destination]`).
   - **X-axis**: `[Total Revenue]`. Sort descending.

---

### Page 7: Reports (Master Transaction Export Table)
Dedicated print-ready and exportable transaction ledger:

1. **Master Transaction Report (Table)**:
   - Coordinates: X = `200px`, Y = `85px`, Width = `1050px`, Height = `610px`.
   - **Columns**: 
     - `bookings[Booking_ID]`
     - `Customers[Name]`
     - `bookings[Booking_Date]`
     - `routes[Source]`
     - `routes[Destination]`
     - `buses[Bus_Type]`
     - `bookings[Fare_Amount]`
     - `bookings[Booking_Status]`
   - *Formatting Settings*:
     - Grid style: **Minimal** or **Alternating Rows** (light gray `#F8FAFC`).
     - Enable **Visual Headers > Export Data** (allows users to extract the table to Excel with one click).
     - Column alignment: numbers right-aligned, text left-aligned.
