# Tableau Step-by-Step Dashboard Setup Guide (From Scratch)

This comprehensive tutorial guides you through building the **Bus Booking Dashboard** in Tableau, including database connection, logical data modeling, calculated fields, dashboard container structures, and creating the vertical navigation sidebar with show/hide filter overlays.

---

## Phase 1: Database Connection

To load your cleansed data from the local MySQL database into Tableau Desktop:

1. Open **Tableau Desktop**.
2. Under the **Connect** pane on the left, click **To a Server** > select **MySQL**.
   *(Note: If you don't see MySQL, click "More..." or install the MySQL ODBC driver from Tableau's driver page).*
3. In the Connection Dialog, enter:
   - **Server**: `localhost`
   - **Port**: `3306`
   - **Username**: `root`
   - **Password**: `root`
4. Click **Sign In**.
5. In the Data Source workspace, select the database **`bus_booking_tableau`** from the Database dropdown.

---

## Phase 2: Data Modeling (Logical Relationships)

Establish relationships between the tables using Tableau's logical relationship canvas (the "noodle" layer):

1. Double-click or drag **`bookings`** onto the main canvas. This will be your fact table.
2. Drag **`customers`** to the canvas and drop it next to `bookings`.
   - Set the relationship join clause: `[bookings].[Customer_ID] = [customers].[Customer_ID]`.
3. Drag **`buses`** to the canvas and drop it next to `bookings`.
   - Set the relationship join clause: `[bookings].[Bus_ID] = [buses].[Bus_ID]`.
4. Drag **`routes`** to the canvas and drop it next to `bookings`.
   - Set the relationship join clause: `[bookings].[Route_ID] = [routes].[Route_ID]`.
5. Switch to a sheet (e.g., `Sheet 1`) to begin creating worksheets.

---

## Phase 3: Calculations & Calculated Fields

Create calculated fields to match the Power BI metrics. To create a calculation, right-click anywhere in the **Data Pane** on the left and select **Create Calculated Field**.

### 1. Main Indicators

#### Total Revenue
```sql
// Name: Total Revenue
SUM([Fare Amount])
```

#### Total Bookings
```sql
// Name: Total Bookings
COUNT([Booking ID])
```

#### Average Fare
```sql
// Name: Average Fare
SUM([Fare Amount]) / COUNT([Booking ID])
```

#### Unique Customers
```sql
// Name: Unique Customers
COUNTD([Customer ID])
```

#### Lead Time Days
```sql
// Name: Lead Time Days
DATEDIFF('day', [Booking Date], [Travel Date])
```

#### Average Lead Time
```sql
// Name: Average Lead Time
AVG([Lead Time Days])
```

#### Lead Time Group
Segments bookings based on how many days in advance they were booked.
```sql
// Name: Lead Time Group
IF [Lead Time Days] = 0 THEN "Same Day"
ELSEIF [Lead Time Days] >= 1 AND [Lead Time Days] <= 3 THEN "1-3 Days"
ELSEIF [Lead Time Days] >= 4 AND [Lead Time Days] <= 7 THEN "4-7 Days"
ELSE "8+ Days"
END
```

#### Customer Retention Rate
Tracks what proportion of customers have booked more than once.
```sql
// Name: Customer Retention Rate
COUNTD(IF { FIXED [Customer ID] : COUNT([Booking ID]) } > 1 THEN [Customer ID] END) 
/ 
COUNTD([Customer ID])
```

#### Occupancy Rate
Evaluates seat fill rate. A run is defined by a unique combination of `Travel Date` and `Bus ID`.
```sql
// Name: Occupancy Rate
COUNT(IF [Booking Status] <> 'Cancelled' THEN [Booking ID] END)
/
SUM({ FIXED [Travel Date], [Bus ID] : MAX([Capacity]) })
```

#### Cancellation Rate
```sql
// Name: Cancellation Rate
COUNT(IF [Booking Status] = 'Cancelled' THEN [Booking ID] END) / COUNT([Booking ID])
```

#### Revenue Leakage
```sql
// Name: Revenue Leakage
SUM(IF [Booking Status] = 'Cancelled' THEN [Fare Amount] END)
```

#### Active Route Footprint
```sql
// Name: Active Route Footprint
COUNTD([Route ID])
```

#### Total Buses
```sql
// Name: Total Buses
COUNTD([Bus ID])
```

#### Total Seating Capacity
```sql
// Name: Total Seating Capacity
SUM([Capacity])
```

#### Occupied Seats
```sql
// Name: Occupied Seats
COUNT(IF [Booking Status] <> 'Cancelled' THEN [Booking ID] END)
```

#### Average Bus Capacity
```sql
// Name: Average Bus Capacity
AVG([Capacity])
```

#### Net Realized Revenue
```sql
// Name: Net Realized Revenue
SUM(IF [Booking Status] <> 'Cancelled' THEN [Fare Amount] END)
```

#### Avg Bookings per Customer
```sql
// Name: Avg Bookings per Customer
COUNT([Booking ID]) / COUNTD([Customer ID])
```

#### Avg Spend per Customer
```sql
// Name: Avg Spend per Customer
SUM([Fare Amount]) / COUNTD([Customer ID])
```

#### Total Distance Covered
```sql
// Name: Total Distance Covered
SUM([Distance])
```

#### Average Route Distance
```sql
// Name: Average Route Distance
AVG([Distance])
```

#### Revenue per KM
```sql
// Name: Revenue per KM
SUM([Fare Amount]) / SUM([Distance])
```

#### Successful Transactions
```sql
// Name: Successful Transactions
COUNT(IF [Booking Status] = 'Confirmed' THEN [Booking ID] END)
```

#### Avg Route Yield
```sql
// Name: Avg Route Yield
SUM([Fare Amount]) / COUNTD([Route ID])
```

#### Avg Revenue per Day
```sql
// Name: Avg Revenue per Day
SUM([Fare Amount]) / COUNTD([Booking Date])
```

#### Loyal Customers (2+ Bookings)
```sql
// Name: Loyal Customers
COUNTD(IF { FIXED [Customer ID] : COUNT([Booking ID]) } >= 2 THEN [Customer ID] END)
```

#### Average Confirmed Transaction Value
```sql
// Name: Average Confirmed Transaction Value
SUM(IF [Booking Status] <> 'Cancelled' THEN [Fare Amount] END) / COUNT(IF [Booking Status] = 'Confirmed' THEN [Booking ID] END)
```

#### Confirmation Rate
```sql
// Name: Confirmation Rate
COUNT(IF [Booking Status] = 'Confirmed' THEN [Booking ID] END) / COUNT([Booking ID])
```

#### Pending Rate
```sql
// Name: Pending Rate
COUNT(IF [Booking Status] = 'Pending' THEN [Booking ID] END) / COUNT([Booking ID])
```

---

## Phase 4: Time Intelligence (Month-over-Month)

In Tableau, Month-over-Month (MoM) comparisons can be achieved using two main methods depending on the visual context.

### Method 1: Using Table Calculations (For Trend Charts)
If you are showing month-by-month values in a chart:
1. **Previous Month Revenue**: 
   `LOOKUP(SUM([Fare Amount]), -1)`
2. **Revenue MoM %**:
   `(SUM([Fare Amount]) - LOOKUP(SUM([Fare Amount]), -1)) / LOOKUP(SUM([Fare Amount]), -1)`
   *(Right-click calculation > Default Properties > Number Format > Percentage, 1 decimal place).*

### Method 2: Using Parameters and LOD Expressions (For Single KPI Cards)

For cards that dynamically display statistics for a selected month vs. the prior month:

1. Create a date parameter **`[Select Month]`** (DataType: Date, values loaded from `Booking Date` truncated to months).
2. **Revenue MoM Calculations**:
   - **`Current Month Revenue`**:
     ```sql
     { FIXED : SUM(IF DATETRUNC('month', [Booking Date]) = [Select Month] THEN [Fare Amount] END) }
     ```
   - **`Previous Month Revenue`**:
     ```sql
     { FIXED : SUM(IF DATETRUNC('month', [Booking Date]) = DATEADD('month', -1, [Select Month]) THEN [Fare Amount] END) }
     ```
   - **`Revenue MoM %`**:
     ```sql
     ([Current Month Revenue] - [Previous Month Revenue]) / [Previous Month Revenue]
     ```
3. **Bookings MoM Calculations**:
   - **`Current Month Bookings`**:
     ```sql
     { FIXED : COUNT(IF DATETRUNC('month', [Booking Date]) = [Select Month] THEN [Booking ID] END) }
     ```
   - **`Previous Month Bookings`**:
     ```sql
     { FIXED : COUNT(IF DATETRUNC('month', [Booking Date]) = DATEADD('month', -1, [Select Month]) THEN [Booking ID] END) }
     ```
   - **`Bookings MoM %`**:
     ```sql
     ([Current Month Bookings] - [Previous Month Bookings]) / [Previous Month Bookings]
     ```
4. **Average Fare MoM Calculations**:
   - **`Current Month Average Fare`**:
     ```sql
     { FIXED : SUM(IF DATETRUNC('month', [Booking Date]) = [Select Month] THEN [Fare Amount] END) 
     / 
     COUNT(IF DATETRUNC('month', [Booking Date]) = [Select Month] THEN [Booking ID] END) }
     ```
   - **`Previous Month Average Fare`**:
     ```sql
     { FIXED : SUM(IF DATETRUNC('month', [Booking Date]) = DATEADD('month', -1, [Select Month]) THEN [Fare Amount] END) 
     / 
     COUNT(IF DATETRUNC('month', [Booking Date]) = DATEADD('month', -1, [Select Month]) THEN [Booking ID] END) }
     ```
   - **`Average Fare MoM %`**:
     ```sql
     ([Current Month Average Fare] - [Previous Month Average Fare]) / [Previous Month Average Fare]
     ```
5. **Customer Retention MoM Calculations**:
   - **`Current Month Retention Rate`**:
     ```sql
     { FIXED : COUNTD(IF { FIXED [Customer ID] : COUNT(IF DATETRUNC('month', [Booking Date]) = [Select Month] THEN [Booking ID] END) } > 1 THEN [Customer ID] END) 
     / 
     COUNTD(IF DATETRUNC('month', [Booking Date]) = [Select Month] THEN [Customer ID] END) }
     ```
   - **`Previous Month Retention Rate`**:
     ```sql
     { FIXED : COUNTD(IF { FIXED [Customer ID] : COUNT(IF DATETRUNC('month', [Booking Date]) = DATEADD('month', -1, [Select Month]) THEN [Booking ID] END) } > 1 THEN [Customer ID] END) 
     / 
     COUNTD(IF DATETRUNC('month', [Booking Date]) = DATEADD('month', -1, [Select Month]) THEN [Customer ID] END) }
     ```
   - **`Retention MoM %`**:
     ```sql
     ([Current Month Retention Rate] - [Previous Month Retention Rate]) / [Previous Month Retention Rate]
     ```

*(For all MoM % calculations, right-click the field > Default Properties > Number Format > select Percentage with 1 or 2 decimal places).*

---

## Phase 5: Creating the Worksheets (Sheet-First Workflow)

> [!IMPORTANT]
> In Tableau, you **cannot** construct charts directly inside a Dashboard canvas. You must build each visual card as an individual **Worksheet (Sheet)** first. Once all required sheets are built, you create a new Dashboard and drag the worksheets from the sidebar into your layout containers.

### Step 1: Create a New Worksheet
1. At the bottom of Tableau Desktop, click the **New Worksheet** icon (the bar chart tab icon with a plus sign next to your sheet list).
2. Double-click the tab name at the bottom and name it according to its dashboard and purpose (e.g., `Overview - Dual-Axis Month Trend` or `Bus Types - Asset Yield Table`).

### Step 2: Build the Visual
1. Use the left **Data Pane** to drag fields onto the **Columns** and **Rows** shelves at the top.
2. Configure the **Marks Card** (Color, Size, Label, Detail, Shape) to specify chart properties.
3. Apply filters directly to the worksheet's **Filters** card.
4. Set custom color themes using the Nordic Ocean codes (e.g., set bars to Ocean Blue `#054A75` or Arctic Cyan `#06B6D4`).

### Step 3: Format the Sheet Background
To ensure a clean white card appearance inside the dashboard:
1. Go to the top menu: **Format** > select **Shading...**
2. In the left sidebar pane, under **Worksheet**, set the background color to **`#FFFFFF`** (white).
3. Hide sheet titles if you prefer to build unified headers on the dashboard (Right-click sheet title on the canvas > select **Hide Title**).

### Step 4: Assemble Sheets onto the Dashboard
1. Switch back to your **Dashboard** tab.
2. In the left-hand sidebar under the **Dashboard** pane, you will see a list of all your created worksheets under the **Sheets** section.
3. Drag a worksheet from the list and hover over the layout containers you built on the canvas. 
4. Release the mouse button when the target container is highlighted in blue. The sheet will resize automatically to fill the container grid.

---

## Phase 6: Dashboard Canvas & Top Navigation Sizing

Configure the workbook coordinates to establish a unified top-navigation widescreen dashboard layout:

1. Create a **New Dashboard**.
2. In the left panel, set **Size** to **Fixed size** > select **Widescreen (1280 x 720)** coordinates.
3. **Top Navigation Container**:
   - Drag a **Horizontal Layout Container** onto the dashboard at the very top.
   - Under the Layout pane, set properties:
     - **Floating**: Uncheck.
     - **Position**: X = `0`, Y = `0`, Width = `1280`, Height = `60`.
     - **Background Color**: White (`#FFFFFF`).
     - **Border**: Set a thin gray border on the bottom (`#E2E8F0`).
4. **Header Title & Logo**:
   - Drag an **Image** object to the far left of the horizontal header. Browse and select `assets/icon_nav_logo.png`. Fit and Center the image.
   - Drag a **Text** object next to the image and type: **`Bus Fleet`** (20pt, Bold, `#0F172A`) with a subtitle **`Analytical Dashboards`** (10pt, Regular, `#64748B`) directly below.
5. **Dashboard Navigation Buttons**:
   - Since Tableau allows you to link dashboards directly, drag a **Navigation Button** object for each of the 3 consolidated dashboards into the middle of the container:
     - Target: Select the respective Dashboard page: `Overview`, `Operations & Assets`, or `Finance & Customers`.
     - Style: **`Text Button`** (or Image Button with active/inactive coloring).
     - **Active state** (styled on the active sheet): Use the blue navigation style (e.g. text color `#054A75` with a light blue background `#E0F2FE` or an active blue indicator).
     - **Inactive state** (styled on the other sheets): Use a slate gray text color (`#64748B`) with transparent background.
     - Set button dimensions to Width = `160`, Height = `35` (since there are 3 larger combined tabs).
     - *Troubleshooting Note*: If the navigation button appears gray even with background set to None, ensure that the **Navigate to** dropdown is linked to a valid sheet or dashboard. Tableau defaults unlinked buttons to a disabled grayed-out state. Also check the **Layout** tab on the left sidebar and verify that its background shading is set to None.

---

## Phase 7: Right-Aligned Sliding Filter Panel (Overlay)

To match the Power BI design, configure a sliding filter panel overlay popping out from the right:

1. Drag a **Vertical Layout Container** onto the dashboard as a **Floating** object.
2. In the Layout pane, set size coordinates to overlay the right margin:
   - X = `1030`
   - Y = `0`
   - Width = `250`
   - Height = `720`
   - Background Color = Pure White (`#FFFFFF`)
   - Add a soft drop shadow under the outer border settings.
3. Drag the filter controls into this floating container:
   - **`Capacity`** (Range Slider)
   - **`Distance`** (Range Slider)
   - **`Bus Type`** (Checkbox list)
4. Add a title "Filters" at the top of the container, along with Reset and Close icons.
5. Click the dropdown arrow on the border of the floating container > select **Add Show/Hide Button**.
6. Move the newly created button to the top-right header: X = `1220`, Y = `15`, Width = `30`, Height = `30`.
7. Right-click the Show/Hide button > select **Edit Button...**:
   - Set **Button Style** to **`Image`**.
   - For **Item Shown** (when filter pane is open, it acts as a Close button):
     - Choose `assets/icon_close_slate.png` (Default state).
     - Choose `assets/icon_close_purple.png` (Hover state).
   - For **Item Hidden** (when filter pane is closed, it acts as the funnel icon):
     - Choose `assets/icon_nav_filters.png` (Default state).
     - Choose `assets/icon_nav_filters_purple.png` (Hover state).
8. Now, clicking the funnel icon instantly overlays or hides the filters container smoothly. Copy this layout across all sheets.

---

## Phase 8: Semicircular Gauge Chart Workaround

Tableau does not have a native semicircular gauge visual, so we implement a rotated Pie/Donut workaround to match the Power BI Occupancy dial:

1. **Create Calculated Fields**:
   - **`Occupied Angle`**: `[Occupancy Rate] * 180`
   - **`Unoccupied Angle`**: `(1.0 - [Occupancy Rate]) * 180`
   - **`Semicircle Spacer`**: `180`
2. **Build the Pie Slices**:
   - Drag **`Measure Names`** to Color.
   - Drag **`Measure Values`** to Angle.
   - Under the Filter card, filter Measure Values to include only `Occupied Angle`, `Unoccupied Angle`, and `Semicircle Spacer`.
3. **Set the Rotation**:
   - Sort the slices in this order: `Occupied Angle` (1st), `Unoccupied Angle` (2nd), and `Semicircle Spacer` (3rd).
   - Double-click the Color legend:
     - Color `Occupied Angle` with Ocean Blue (`#054A75`).
     - Color `Unoccupied Angle` with Light Gray (`#E2E8F0`).
     - Color `Semicircle Spacer` with the same color as the dashboard background: Frost Slate (`#F8FAFC`) (or select White if container is white).
   - Under **Format** properties, rotate the Pie chart starting angle to **`-90` degrees** (or **`270` degrees**). This forces the 180-degree spacer to sit at the bottom, leaving a clean semicircular arc on top.
4. **Make it a Donut**:
   - Drag a dummy calculated field `MIN(1.0)` to Rows twice.
   - Right-click the second pill and select **Dual Axis**.
   - On the second Marks card, remove all measures, change the mark type to **Circle**, set the color to White (`#FFFFFF`), and decrease the size slightly to form the inner hole.
   - Drag the `Occupancy Rate` field onto the **Label** shelf of the center circle mark to display the `0.51` text in the center. Add target indicator at `0.80`.

---

## Phase 9: KPI Card Sparkline Backgrounds

To recreate the background area chart fills inside the top row KPI cards (e.g., on the Overview dashboard):

1. **Create the Sparkline Sheet**:
   - Create a new worksheet (e.g., `Revenue Sparkline Background`).
   - Drag continuous **`Booking Date`** (Day level) to Columns.
   - Drag the KPI measure pill (e.g. **`Total Revenue`**) to Rows.
   - Change the Mark type from Line to **Area**.
2. **Style the Sparkline**:
   - Change color to Arctic Cyan (`#06B6D4`) or Ocean Blue (`#054A75`) depending on the card theme, and set transparency/opacity to **`25%` or `30%`**.
   - Hide the Y-axis and X-axis (Right-click axis > uncheck **Show Header**).
   - Right-click anywhere on the chart canvas > select **Format**:
     - Go to **Lines** tab (grid icon) > set Grid Lines, Zero Lines, and Axis Rulers to **`None`**.
     - Go to **Borders** tab (square icon) > set Row Divider and Column Divider to **`None`**.
3. **Assemble in Dashboard Container**:
   - Create a horizontal or vertical layout card container in your dashboard (background: White, border: light gray `#E2E8F0` with rounded corners).
   - Drag the KPI Callout Text sheet (which contains the large callout number and label text) into the container as a tiled object.
   - Drag the `Revenue Sparkline Background` worksheet onto the canvas as a **Floating** object.
   - Resize and position the floating sparkline sheet to cover the bottom half of the KPI card container (e.g., Width = `290px`, Height = `50px`).
   - Right-click the sparkline sheet container > select **Floating Order** > **Send to Back** (so it floats directly behind the callout text without blocking mouse hover/clicks on the numbers).

---

## Phase 10: Donut Chart Construction Guide

Since Tableau does not have a native "Donut Chart" option in its Show Me pane, you can construct one from scratch using a dual-axis Pie Chart workaround:

### Step 1: Build the Base Pie Chart
1. Create a new worksheet.
2. In the **Marks** card dropdown menu, change the mark type from **Automatic** to **Pie**.
3. Drag the dimension you want to slice by (e.g., `[Bus Type]`) from the Data pane and drop it onto the **Color** shelf of the Marks card.
4. Drag the measure you want to size the slices by (e.g., `[Total Revenue]`) from the Data pane and drop it onto the **Angle** shelf.
5. (Optional) Drag the measure onto the **Label** shelf if you wish to show data labels on the outer slices.

### Step 2: Create a Dual Axis on Rows
1. Double-click the empty space on the **Rows** shelf (at the top of the workspace) to create an ad-hoc calculation.
2. Type **`AVG(0)`** and press Enter. This creates a pill named `AGG(AVG(0))` and renders a horizontal line across the center of your chart.
3. Hold the **Ctrl** key (or **Cmd** key on Mac), click this `AGG(AVG(0))` pill on the Rows shelf, and drag it slightly to the right to duplicate it.
4. You will now have two `AGG(AVG(0))` pills side-by-side on your Rows shelf, which splits your canvas into two identical stacked Pie charts.

### Step 3: Configure the Cutout Hole Mark
1. Look at the **Marks Card** on the left. It will now display three tabs: **All**, **AGG(AVG(0)) (first)**, and **AGG(AVG(0)) (second)**.
2. Click the **third tab** (`AGG(AVG(0)) (second)`) to format only the bottom pie chart.
3. Click and drag **all fields out** of this Marks card (drag `Bus Type` and `Total Revenue` off the card so it is completely empty).
4. Change the Mark type of this second card from **Pie** to **Circle**.
5. Click the **Color** shelf of this second card and set the color to pure White (`#FFFFFF`) (or matching your card/dashboard container background shade).

### Step 4: Merge and Size the Donut
1. Right-click the second `AGG(AVG(0))` pill on the Rows shelf and select **Dual Axis**.
2. The white circle and the pie chart will merge on top of each other.
3. Click the first Marks tab (`AGG(AVG(0)) (first)`) and click the **Size** shelf. Drag the slider to the right to increase the outer Pie chart's size.
4. Click the second Marks tab (`AGG(AVG(0)) (second)`) and click the **Size** shelf. Adjust the slider to size the inner white circle, creating a clean outer ring and cutout hole.
5. (Optional) Drag your summary text or grand total measure onto the **Label** shelf of this second card to display values inside the cutout hole.

### Step 5: Clean Up Gridlines and Headers
1. Right-click the canvas and select **Format...**
2. Go to the **Lines** tab (grid icon) in the formatting sidebar:
   - Set **Zero Lines** and **Grid Lines** to **None**.
   - Set **Axis Rulers** to **None**.
3. Go to the **Borders** tab (square icon) in the formatting sidebar:
   - Set **Row Dividers** and **Column Dividers** to **None**.
4. Right-click the vertical axes on the canvas and uncheck **Show Header** to hide the `0` coordinate markings.
