# Power BI Step-by-Step Dashboard Setup Guide (From Scratch)

This comprehensive tutorial guides you through building the **Bus Booking Dashboard** from absolute scratch, including database ingestion, data modeling, DAX calculations, page layout configurations, and creating the vertical navigation sidebar exactly as specified.

---

## Phase 1: Database Connection

To load your cleansed data from the local MySQL database:

1. Open **Power BI Desktop** (start with a blank report).
2. On the **Home** ribbon, click **Get Data** > select **MySQL database**.
3. In the Connection Dialog:
   - **Server**: `localhost`
   - **Database**: `bus_booking_analytics`
   - **Connectivity mode**: `Import`
4. Click **OK**.
5. When the credential prompt appears:
   - Select the **Database** tab in the left-hand sidebar (do *not* select Windows).
   - **User name**: `root`
   - **Password**: `root`
   - Click **Connect**.
6. In the **Navigator** window:
   - Select the four tables: `bookings`, `buses`, `customers`, and `routes`.
   - Click **Load**.

---

## Phase 2: Data Modeling (Star Schema)

Establish relationships to allow filters to flow correctly:

1. Switch to the **Model View** (left-sidebar icon of Power BI).
2. Create relationships by dragging and dropping keys (1 to Many, single-direction filter):
   - **`customers[Customer_ID]` (1) ───> (*) `bookings[Customer_ID]`**
   - **`buses[Bus_ID]` (1) ───> (*) `bookings[Bus_ID]`**
   - **`routes[Route_ID]` (1) ───> (*) `bookings[Route_ID]`**

---

## Phase 3: Date Table (Calendar) Setup

To enable Month-over-Month (MoM) calculations, set up a continuous calendar:

1. Switch to the **Table View** (left-sidebar).
2. In the **Modeling** ribbon, click **New Table**.
3. Enter the following DAX formula:
   ```dax
   Calendar = 
   ADDCOLUMNS(
       CALENDAR(MIN(bookings[Booking_Date]), MAX(bookings[Booking_Date])),
       "Year", YEAR([Date]),
       "Month Number", MONTH([Date]),
       "Month Name", FORMAT([Date], "MMMM"),
       "Quarter", "Q" & FORMAT([Date], "Q"),
       "Year Month", FORMAT([Date], "YYYY-MM")
   )
   ```
4. Right-click the `Calendar` table in your Data pane > select **Mark as date table** > choose `Date` as the key column.
5. Switch to **Model View** and link the dates:
   - **`Calendar[Date]` (1) ───> (*) `bookings[Booking_Date]`**
   - *Note: Ensure both `bookings[Booking_Date]` and `Calendar[Date]` are formatted as **Date** data type under the Column Tools ribbon.*

---

## Phase 4: Core Business DAX Measures

Organize your formulas by clicking **Enter Data** on the Home tab, naming the table `_Measures`, loading it, and writing these calculations:

### 1. Main Indicators

#### Total Revenue
```dax
Total Revenue = SUM(bookings[Fare_Amount])
```
*Format: Currency (`$ English (United States)`), 0 decimal places.*

#### Total Bookings
```dax
Total Bookings = COUNT(bookings[Booking_ID])
```
*Format: Whole Number.*

#### Average Fare
```dax
Average Fare = DIVIDE([Total Revenue], [Total Bookings], 0)
```
*Format: Currency, 2 decimal places.*

#### Unique Customers
```dax
Unique Customers = DISTINCTCOUNT(bookings[Customer_ID])
```

#### Customer Retention Rate
```dax
Customer Retention Rate = 
VAR CustomersWithMultipleBookings = 
    COUNTROWS(
        FILTER(
            VALUES(bookings[Customer_ID]),
            CALCULATE(COUNT(bookings[Booking_ID])) > 1
        )
    )
RETURN 
    DIVIDE(CustomersWithMultipleBookings, [Unique Customers], 0)
```
*Format: Decimal Number, 2 decimal places.*

---

### 2. Time Intelligence (Previous Month)

#### Previous Month Revenue
```dax
Previous Month Revenue = CALCULATE([Total Revenue], DATEADD('Calendar'[Date], -1, MONTH))
```

#### Revenue MoM %
```dax
Revenue MoM % = 
VAR PrevRev = [Previous Month Revenue]
RETURN DIVIDE([Total Revenue] - PrevRev, PrevRev, 0)
```

#### Previous Month Bookings
```dax
Previous Month Bookings = CALCULATE([Total Bookings], DATEADD('Calendar'[Date], -1, MONTH))
```

#### Bookings MoM %
```dax
Bookings MoM % = 
VAR PrevBookings = [Previous Month Bookings]
RETURN DIVIDE([Total Bookings] - PrevBookings, PrevBookings, 0)
```

#### Previous Month Average Fare
```dax
Previous Month Average Fare = CALCULATE([Average Fare], DATEADD('Calendar'[Date], -1, MONTH))
```

#### Average Fare MoM %
```dax
Average Fare MoM % = 
VAR PrevFare = [Previous Month Average Fare]
RETURN DIVIDE([Average Fare] - PrevFare, PrevFare, 0)
```

#### Previous Month Retention
```dax
Previous Month Retention = CALCULATE([Customer Retention Rate], DATEADD('Calendar'[Date], -1, MONTH))
```

#### Retention MoM %
```dax
Retention MoM % = 
VAR PrevRet = [Previous Month Retention]
RETURN DIVIDE([Customer Retention Rate] - PrevRet, PrevRet, 0)
```

---

### 3. Pill-Shape Custom Labels
These measures format the trend text inside the bottom capsules dynamically:

#### Revenue Trend Label
```dax
Revenue Trend Label = 
VAR MoM = [Revenue MoM %]
RETURN 
    IF(
        ISBLANK(MoM),
        "No Data vs Last Period",
        IF(
            MoM >= 0,
            "↑ " & FORMAT(MoM, "0.0%") & " vs Last Period",
            "↓ " & FORMAT(MoM, "0.0%") & " vs Last Period"
        )
    )
```

#### Bookings Trend Label
```dax
Bookings Trend Label = 
VAR MoM = [Bookings MoM %]
RETURN 
    IF(
        ISBLANK(MoM),
        "No Data vs Last Period",
        IF(
            MoM >= 0,
            "↑ " & FORMAT(MoM, "0.0%") & " vs Last Period",
            "↓ " & FORMAT(MoM, "0.0%") & " vs Last Period"
        )
    )
```

#### Average Fare Trend Label
```dax
Average Fare Trend Label = 
VAR MoM = [Average Fare MoM %]
RETURN 
    IF(
        ISBLANK(MoM),
        "No Data vs Last Period",
        IF(
            MoM >= 0,
            "↑ " & FORMAT(MoM, "0.0%") & " vs Last Period",
            "↓ " & FORMAT(MoM, "0.0%") & " vs Last Period"
        )
    )
```

#### Retention Trend Label
```dax
Retention Trend Label = 
VAR MoM = [Retention MoM %]
RETURN 
    IF(
        ISBLANK(MoM),
        "No Data vs Last Period",
        IF(
            MoM >= 0,
            "↑ " & FORMAT(MoM, "0.0%") & " vs Last Period",
            "↓ " & FORMAT(MoM, "0.0%") & " vs Last Period"
        )
    )
```

---

## Phase 5: Canvas & Sidebar Sizing Setup

Configure your workspace geometry to fit a single widescreen window:

1. Click on the canvas background. Go to the **Format** pane > **Canvas settings** > Type: **16:9 Widescreen** (`1280 x 720` pixels).
2. In the top **View** ribbon, set **Page View** to **`Fit to Page`**.
3. Create your multi-page structure in Power BI. Create the following page tabs:
   - `Overview`
   - `Bookings`
   - `Revenue`
   - `Customers`
   - `Bus Types`
   - `Routes`
   - `Reports`
4. **Left Navigation Sidebar**:
   - Insert a **Rectangle Shape** (Insert > Shapes > Rectangle).
   - Set coordinates: X = `0px`, Y = `0px`, Width = `180px`, Height = `720px` (full vertical height).
   - Fill: White (`#FFFFFF`). Border: Outline color Light Gray (`#E2E8F0`), Width: `1px`.
   - Place your navigation logo image (`assets/icon_nav_logo.png`) at X = `15px`, Y = `20px`, Width = `45px`, Height = `45px`.
5. **Navigation Buttons Setup (Individual Sidebar Buttons)**:
   Because the native Page Navigator visual does not allow you to set *different* custom icons for each page, you must create 7 individual buttons. 

   Furthermore, since each page tab in Power BI (Overview, Bookings, etc.) is a separate canvas, **there is no native "Selected" state setting**. Instead, you will style the **Default** state of the active button differently on each specific page:

   - **Active State** (e.g. style the `Overview` button this way only when editing the `Overview` page canvas):
     - **Fill**: Toggle **On**, set background color to very light purple (Hex `#F3E8FF` or `#F5F3FF`), transparency `0%`.
     - **Icon**: Toggle **On**, set type to **`Custom`** and upload the **filled purple version** (e.g. `assets/icon_nav_overview_purple.png`). Position: **`Left`**, size **`20px`**.
     - **Text**: Toggle **On**, set value to the page name (e.g. `Overview`). Font: `Segoe UI Semibold`, size `10pt`, color Purple (`#7C3AED`). Alignment: **`Left`**. In padding settings, set **Left padding** to **`45px`** to push the text next to the icon.
     - **Vertical Purple Indicator Bar (Workaround)**: 
       Since standard Blank Buttons only support uniform 4-sided borders (no native left-only border), build the line using a small shape:
       - Insert a **Rectangle Shape** (Insert > Shapes > Rectangle).
       - Set dimensions: Width = `3px`, Height = `45px` (matching the button height).
       - Position it on the far left edge of the active button (X = `10px`).
       - Turn off the shape outline border, and set **Fill Color** to Purple (`#7C3AED`).
   
   - **Inactive State** (style the other 6 buttons this way on the current page canvas):
     - **Fill**: Toggle **Off** (transparent background).
     - **Icon**: Toggle **On**, set type to **`Custom`** and upload the **slate gray version** (e.g. `assets/icon_nav_bookings.png` for Bookings button). Position: **`Left`**, size **`20px`**.
     - **Text**: Toggle **On**, set value to the page name. Font: `Segoe UI Semibold`, size `10pt`, color Slate Gray (`#64748B`). Alignment: **`Left`**, **Left padding** set to **`45px`**.

   Set the size for all 7 buttons: Width = `160px`, Height = `45px`. Place them vertically in the sidebar starting from Y = `100px` down to Y = `460px` (with X = `10px`). Copy and paste this sidebar set to all page canvases, then swap which button is styled as **Active** on each page and move the vertical purple indicator bar shape next to it.

6. **Filters button**: Place a Blank Button at X = `15px`, Y = `660px`, size `150px` x `40px`. 
   - Under Style > Icon, upload `assets/icon_nav_filters.png`. 
   - Under Style > Text, toggle **On**, set text to `Filters`. Font size `10pt`, color Slate Gray (`#64748B`). Left padding set to `45px`. Action set to toggle a Bookmark or Filter panel.

---

## Phase 6: Creating Dashboard Visuals

Configure the visuals on the single-page layout matching the reference dashboard:

### A. Title Header
- **Title Text**: `Bus Booking Dashboard` (X = `100px`, Y = `15px`, Width = `500px`, Height = `40px`. Font: `Segoe UI`, size `20pt`, Bold, color `#0F172A`).
- **Subtitle Text**: `Overview of bookings and revenue performance` (X = `100px`, Y = `50px`, size `10pt`, color `#64748B`).
- **Top Right Slicer**: Place a Slicer visual at X = `950px`, Y = `15px`, Width = `300px`, Height = `40px`. Select field `bookings[Booking_Date]`, format style as **Dropdown**.

---

### B. KPI Cards (Top Row)
Create a single **Card (New)** visual spanning the top row (X = `100px`, Y = `85px`, Width = `1160px`, Height = `120px`):

1. **Fields Assignment**:
   - Drag `[Total Revenue]`, `[Total Bookings]`, `[Average Fare]`, and `[Customer Retention Rate]` into the Data box.
2. **Horizontal Layout**:
   - Go to **Format pane > Layout** > Orientation: **`Horizontal`**, Columns: **`4`**, Card spacing: `15px`.
   - Set **Vertical alignment** to **`Middle`** (under Layout).
3. **Card Alignment**:
   - Go to **Callout values** > Horizontal alignment: **`Left`** (all text aligns next to the icons).
4. **Card Background Gradients**:
   Expand **Cards > Fill > Series** and select card-by-card:
   - *Total Revenue*: Upload `assets/Bg Theme.jpg` (Green). Image Fit: Fill.
   - *Total Bookings*: Upload `assets/Blue Bg Theme.png` (Blue). Image Fit: Fill.
   - *Average Fare*: Upload `assets/Peach Bg Image.jpg` (Orange). Image Fit: Fill.
   - *Customer Retention Rate*: Upload `assets/Purple Bg Theme.jpg` (Purple). Image Fit: Fill.
5. **Floating Icons**:
   Expand **Cards > Image > Series** and upload the transparent 3D shadow icons:
   - *Total Revenue*: `assets/icon_revenue.png`. Position: Left, Spacing: `15px`, size `50px`.
   - *Total Bookings*: `assets/icon_bookings.png`. Position: Left, size `50px`.
   - *Average Fare*: `assets/icon_fare.png`. Position: Left, size `50px`.
   - *Customer Retention Rate*: `assets/icon_retention.png`. Position: Left, size `50px`.
6. **Pill-Shape Trend Indicators (Detail Background)**:
   - Go to **Reference labels** > set **Cards** to **`Total Revenue`**.
   - Add `[Revenue Trend Label]` to **Add label** field.
   - Toggle **`Title`** to **`Off`** (removes duplicate measure name).
   - Toggle **`Value`** to **`Off`** (removes duplicate text value).
   - Toggle **`Detail`** to **`On`** and expand it:
     - Drag `[Revenue Trend Label]` to detail. Set color to **White**, size **`10`**.
     - Expand **Background** (inside Detail) > Toggle **`On`**. Set color to dark green (`#064E3B`), transparency **`30%`** (forms the capsule pill).
     - Under **Reference label layout** (or layout settings), change **Alignment** to **`Left`** (shifts pill under text).
   - Repeat the pill styling for the other three cards using their respective trend label measures and background colors (Blue, Orange, Purple) at `30%` transparency.

---

### C. Main Charts (Middle Row)

1. **Total Bookings and Total Revenue by Year, Quarter and Month (Dual Axis Line Chart)**:
   - Coordinates: X = `100px`, Y = `220px`, Width = `570px`, Height = `240px`.
   - **X-axis**: Drag `Calendar[Year]`, `Calendar[Quarter]`, `Calendar[Month]`.
   - **Y-axis**: Drag `[Total Bookings]`. (Line Color: Electric Blue `#3B82F6`)
   - **Secondary Y-axis**: Drag `[Total Revenue]`. (Line Color: Dark Blue `#002D62`)
   - **Formatting**: Stroke width `3px`, Smooth line toggled **On**.
2. **Total Revenue by Bus_Type (Donut Chart)**:
   - Coordinates: X = `690px`, Y = `220px`, Width = `570px`, Height = `240px`.
   - **Legend**: `buses[Bus_Type]` (Non-AC Sleeper, AC Sleeper, Non-AC Seater, AC Seater).
   - **Values**: `[Total Revenue]`.
   - **Labels**: Set to **Data value, percent of total** (displays e.g. `870.03K (59.01%)`).

---

### D. Lower Section Visuals

1. **Total Revenue by Source (Horizontal Bar Chart)**:
   - Coordinates: X = `100px`, Y = `475px`, Width = `570px`, Height = `230px`.
   - **Y-axis**: `routes[Source]`
   - **X-axis**: `[Total Revenue]`. (Bar Color: Solid Blue `#1E88E5`).
2. **Interactive Filters Sidebar Grid**:
   Place these visuals side-by-side:
   - **Date Filter Slicer**: X = `690px`, Y = `475px`, Width = `280px`, Height = `110px`. Field: `bookings[Booking_Date]`, Style: **Between (Slider)**.
   - **Source/Destination Slicer**: X = `990px`, Y = `475px`, Width = `270px`, Height = `110px`. Field: `routes[Source]`, `routes[Destination]`, Style: **Dropdown**.
   - **Bus Type Slicer**: X = `690px`, Y = `595px`, Width = `280px`, Height = `110px`. Field: `buses[Bus_Type]`, Style: **Vertical List**.
3. **Booking_Status KPI Cards (Lower Right)**:
   Place a Card (New) visual at X = `990px`, Y = `595px`, Width = `270px`, Height = `110px` showing status splits:
   - **Cancelled**: Value `COUNTROWS(FILTER(bookings, bookings[Booking_Status] = "Cancelled"))` (Icon: `assets/icon_cancelled.png`).
   - **Confirmed**: Value `COUNTROWS(FILTER(bookings, bookings[Booking_Status] = "Confirmed"))` (Icon: `assets/icon_confirmed.png`).
   - **Pending**: Value `COUNTROWS(FILTER(bookings, bookings[Booking_Status] = "Pending"))` (Icon: `assets/icon_pending.png`).
