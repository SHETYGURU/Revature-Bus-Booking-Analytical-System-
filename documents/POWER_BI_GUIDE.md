# Bus Booking Dashboard Setup & Visualisation Guide

This guide details how to establish database connections, model the tables, write DAX measures, and design the interactive dashboard in **Power BI Desktop** exactly as shown in the dashboard visual specifications.

---

## 1. Connecting Data to Power BI

You can load the cleaned datasets into Power BI using one of three methods:

### Method A: Direct CSV Ingestion (Recommended for quick setup)
1. Open **Power BI Desktop**.
2. Click **Get Data** > **Text/CSV**.
3. Import the four cleaned files from the `data/clean/` directory:
   - `bookings_clean.csv`
   - `customers_clean.csv`
   - `buses_clean.csv`
   - `routes_clean.csv`

### Method B: MySQL Database Connection (Production)
1. Ensure your MySQL Server is running and the database `bus_booking_analytics` is populated.
2. In Power BI, click **Get Data** > **MySQL database**.
3. Server: `localhost` (or server IP), Database: `bus_booking_analytics`.
4. Select **Database** credentials tab, enter user `root` and password `root`, and click Connect.
5. Import `Bookings`, `Customers`, `Buses`, and `Routes`.

---

## 2. Data Modeling & Relationships (Star Schema)

Once the tables are loaded, switch to the **Model View** (left-hand sidebar) and establish the relationships to construct a clean star schema:

1. Drag **Customer_ID** from `Customers` to `Bookings` (1 to Many, Single Direction).
2. Drag **Bus_ID** from `Buses` to `Bookings` (1 to Many, Single Direction).
3. Drag **Route_ID** from `Routes` to `Bookings` (1 to Many, Single Direction).

---

## 3. Date Table (Calendar) Setup

To enable time intelligence calculations (such as comparing the current month's revenue to the previous period), create a continuous **Date Table**:

1. In the **Modeling** tab of Power BI Desktop, click **New Table**.
2. Write the following DAX formula:
   ```dax
   Calendar = 
   ADDCOLUMNS(
       CALENDAR(MIN(Bookings[Booking_Date]), MAX(Bookings[Booking_Date])),
       "Year", YEAR([Date]),
       "Month Number", MONTH([Date]),
       "Month Name", FORMAT([Date], "MMMM"),
       "Quarter", "Q" & FORMAT([Date], "Q"),
       "Year Month", FORMAT([Date], "YYYY-MM")
   )
   ```
3. Establish a relationship: Connect **`Calendar[Date]` (1) ───> (*) `Bookings[Booking_Date]`**.
4. Right-click the `Calendar` table > click **Mark as date table**.

---

## 4. Key Business DAX Measures

Create a new table named `_Measures` and write the following DAX formulas:

### Total Revenue
```dax
Total Revenue = SUM(Bookings[Fare_Amount])
```
*Format as Currency, 0 decimal places (e.g. display units: Millions `$1.47M`).*

### Total Bookings
```dax
Total Bookings = COUNT(Bookings[Booking_ID])
```
*Format as Whole Number (e.g. display units: Thousands `2K`).*

### Average Fare
```dax
Average Fare = DIVIDE([Total Revenue], [Total Bookings], 0)
```
*Format as Decimal Number, 2 decimal places (e.g. `786.37`).*

### Unique Customers
```dax
Unique Customers = DISTINCTCOUNT(Bookings[Customer_ID])
```

### Customer Retention Rate
```dax
Customer Retention Rate = 
VAR CustomersWithMultipleBookings = 
    COUNTROWS(
        FILTER(
            VALUES(Bookings[Customer_ID]),
            CALCULATE(COUNT(Bookings[Booking_ID])) > 1
        )
    )
RETURN 
    DIVIDE(CustomersWithMultipleBookings, [Unique Customers], 0)
```
*Format as Decimal Number, 2 decimal places (e.g. `0.99`).*

### Previous Period (MoM) Measures
To display the comparisons on the bottom of the card visuals:

#### Previous Month Revenue
```dax
Previous Month Revenue = 
CALCULATE([Total Revenue], DATEADD('Calendar'[Date], -1, MONTH))
```

#### Revenue MoM Change %
```dax
Revenue MoM % = 
VAR PrevRev = [Previous Month Revenue]
RETURN DIVIDE([Total Revenue] - PrevRev, PrevRev, 0)
```

#### Previous Month Bookings
```dax
Previous Month Bookings = 
CALCULATE([Total Bookings], DATEADD('Calendar'[Date], -1, MONTH))
```

#### Bookings MoM Change %
```dax
Bookings MoM % = 
VAR PrevBookings = [Previous Month Bookings]
RETURN DIVIDE([Total Bookings] - PrevBookings, PrevBookings, 0)
```

#### Previous Month Average Fare
```dax
Previous Month Average Fare = 
CALCULATE([Average Fare], DATEADD('Calendar'[Date], -1, MONTH))
```

#### Average Fare MoM Change %
```dax
Average Fare MoM % = 
VAR PrevFare = [Previous Month Average Fare]
RETURN DIVIDE([Average Fare] - PrevFare, PrevFare, 0)
```

#### Previous Month Retention Rate
```dax
Previous Month Retention = 
CALCULATE([Customer Retention Rate], DATEADD('Calendar'[Date], -1, MONTH))
```

#### Retention Rate MoM Change %
```dax
Retention MoM % = 
VAR PrevRet = [Previous Month Retention]
RETURN DIVIDE([Customer Retention Rate] - PrevRet, PrevRet, 0)
```

---

## 5. Dashboard Visuals Setup

Configure the visuals on the single-page layout matching the reference dashboard:

### A. Title Header
- **Title Text**: `Bus Booking Dashboard` (Font size: `22pt`, Bold, Dark Slate Blue)
- **Subtitle Text**: `Overview of bookings and revenue performance` (Font size: `11pt`, Slate Gray)
- **Top Right Slicer**: Place a **Slicer** visual, select `Bookings[Booking_Date]`, format style as **Dropdown** (Date Range picker).

### B. KPI Cards (Top Row)
To achieve this exact visual layout (circular icon on the left, primary value/label in the center-right, and the trend indicator styled as a pill at the bottom), use the **Card (New)** visual (not the native KPI visual) and configure it as follows:

#### Step 1: Create Trend Label DAX Measures
Create these measures in your `_Measures` table to automatically format the text inside the bottom pills (including arrows and text):

##### Revenue Trend Label
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

##### Bookings Trend Label
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

##### Average Fare Trend Label
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

##### Retention Trend Label
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

#### Step 2: Configure the Card (New) Visuals
Create a **Card (New)** visual on your canvas and set the parameters:

1. **Total Revenue Card**:
   - **Data**: Drag `[Total Revenue]` (Main indicator) and `[Revenue Trend Label]` (for the pill).
   - **Fill Background**: Under *Format Pane* > *Cards* > *Fill*, upload `assets/Bg Theme.jpg` (Green gradient). Image Fit: Fill.
   - **Card Icon**: Under *Format Pane* > *Cards* > *Image*, upload `assets/icon_revenue.png`. Position: Left. Size: 50px.
   - **Pill Shape (Reference Label)**:
     - Go to *Format Pane* > *Reference labels* > select the `Total Revenue` series.
     - Add `[Revenue Trend Label]` as the label value.
     - Select the label, turn on **Background**, and set the background color to a dark semi-transparent green (e.g. Hex `#064E3B`, transparency `30%`) to create the rounded "pill" capsule look. Set text color to white.
2. **Total Bookings Card**:
   - **Data**: Drag `[Total Bookings]` and `[Bookings Trend Label]`.
   - **Fill Background**: Upload `assets/Blue Bg Theme.png`.
   - **Card Icon**: Upload `assets/icon_bookings.png`. Position: Left. Size: 50px.
   - **Pill Shape (Reference Label)**: Configure background to a semi-transparent dark blue (Hex `#1E3A8A`, transparency `30%`). Set text color to white.
3. **Average Fare Card**:
   - **Data**: Drag `[Average Fare]` and `[Average Fare Trend Label]`.
   - **Fill Background**: Upload `assets/Peach Bg Image.jpg`.
   - **Card Icon**: Upload `assets/icon_fare.png`. Position: Left. Size: 50px.
   - **Pill Shape (Reference Label)**: Configure background to a semi-transparent dark orange (Hex `#7C2D12`, transparency `30%`). Set text color to white.
4. **Customer Retention Rate Card**:
   - **Data**: Drag `[Customer Retention Rate]` and `[Retention Trend Label]`.
   - **Fill Background**: Upload `assets/Purple Bg Theme.jpg`.
   - **Card Icon**: Upload `assets/icon_retention.png`. Position: Left. Size: 50px.
   - **Pill Shape (Reference Label)**: Configure background to a semi-transparent dark purple (Hex `#581C87`, transparency `30%`). Set text color to white.

### C. Main Charts (Middle Row)

1. **Total Bookings and Total Revenue by Year, Quarter and Month (Dual Axis Line Chart)**:
   - **X-axis**: Drag `Calendar[Year]`, `Calendar[Quarter]`, `Calendar[Month]` (hierarchy).
   - **Y-axis**: Drag `[Total Bookings]`. (Series Line Color: Electric Blue `#3B82F6`)
   - **Secondary Y-axis**: Drag `[Total Revenue]`. (Series Line Color: Dark Blue `#002D62`)
   - **Lines Formatting**: Set Stroke width to `3px` and turn **Smooth line** to **On**.
2. **Total Revenue by Bus_Type (Donut Chart)**:
   - **Legend**: `Buses[Bus_Type]` (Non-AC Sleeper, AC Sleeper, Non-AC Seater, AC Seater).
   - **Values**: `[Total Revenue]`.
   - **Detail Labels**: Set to **Data value, percent of total** (displays e.g. `870.03K (59.01%)` for Non-AC Sleeper).
   - **Slice Colors**: Custom palette matching the dark blue, light blue, orange, and purple segments.

### D. Lower Section Visuals

1. **Total Revenue by Source (Horizontal Bar Chart)**:
   - **Y-axis (Axis)**: `Routes[Source]`
   - **X-axis (Values)**: `[Total Revenue]` (formatted to show e.g. `300K`, `270K`, etc.)
   - **Bar Color**: Solid Blue (`#1E88E5`).
2. **Booking Date Filter (Slicer)**:
   - **Field**: `Bookings[Booking_Date]`. Style: **Between (Slider)** with rounded handle styling.
3. **Source, Destination Filter (Slicer)**:
   - **Field**: `Routes[Source]`, `Routes[Destination]` (concatenated hierarchy). Style: **Dropdown** picker.
4. **Bus_Type Filter (Slicer)**:
   - **Field**: `Buses[Bus_Type]`. Style: **Vertical list** with checkboxes.
5. **Booking_Status KPI Cards (Lower Right)**:
   Place 3 small Card visuals representing booking counts side-by-side:
   - **Cancelled Card**:
     - **Value**: `COUNTROWS(FILTER(Bookings, Bookings[Booking_Status] = "Cancelled"))` (e.g. `356`).
     - **Icon**: `assets/icon_cancelled.png`.
   - **Confirmed Card**:
     - **Value**: `COUNTROWS(FILTER(Bookings, Bookings[Booking_Status] = "Confirmed"))` (e.g. `1,254`).
     - **Icon**: `assets/icon_confirmed.png`.
   - **Pending Card**:
     - **Value**: `COUNTROWS(FILTER(Bookings, Bookings[Booking_Status] = "Pending"))` (e.g. `410`).
     - **Icon**: `assets/icon_pending.png`.

### Page 2: Operational Performance & Demographics
To satisfy all remaining requirements in the Project Specification PDF, build this second tab in your report:

1. **Customer Distribution (Treemap / Table)**:
   - **Visual Type**: Treemap or Table.
   - **Category (Group)**: `Customers[Name]`
   - **Values**: `[Total Bookings]` (sorted descending to show your top-booking customers).
2. **Seat Occupancy Rate (Gauge Visual)**:
   - **Visual Type**: Gauge.
   - **Value**: `[Occupancy Rate]`
   - **Target Value**: `0.80` (representing your 80% occupancy target).
3. **Route Performance (Matrix / Table)**:
   - **Visual Type**: Matrix.
   - **Rows**: `Routes[Source]` and `Routes[Destination]` (nested hierarchy).
   - **Values**: 
     - `[Total Bookings]`
     - `[Total Revenue]`
     - `[Occupancy Rate]`
   - *This allows management to drill down and review passenger load factor and financial yield for each route.*

