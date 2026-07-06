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

### B. KPI Visuals (Top Row)
To match the dashboard, use the dedicated **KPI** visual in Power BI (which displays a large indicator, a sparkline trend line in the background, and an automatic target comparison percentage at the bottom). Create four separate KPI visuals side-by-side:

1. **Total Revenue KPI**:
   - **Indicator**: `Total Revenue` (Display Units: Millions, e.g., `1.47M`)
   - **Trend axis**: `Calendar[Date]` (or `Calendar[Year Month]`)
   - **Target**: `Previous Month Revenue`
   - **Visual Background**: In the Format pane, set background to **Image** > upload `assets/Bg Theme.jpg` (Green gradient).
   - **Visual Icon**: Place the icon `assets/icon_revenue.png` on the left (e.g. overlaying an Image visual or setting card icon).
   - **Status Label**: The bottom label will automatically display the growth rate (e.g. `12.5% vs Last Period`).
2. **Total Bookings KPI**:
   - **Indicator**: `Total Bookings` (Display Units: Thousands, e.g., `2K`)
   - **Trend axis**: `Calendar[Date]` (or `Calendar[Year Month]`)
   - **Target**: `Previous Month Bookings`
   - **Visual Background**: Set background to **Image** > upload `assets/Blue Bg Theme.png`.
   - **Visual Icon**: Place the icon `assets/icon_bookings.png` on the left.
3. **Average Fare KPI**:
   - **Indicator**: `Average Fare` (No display units, 2 decimal places, e.g. `786.37`)
   - **Trend axis**: `Calendar[Date]` (or `Calendar[Year Month]`)
   - **Target**: `Previous Month Average Fare`
   - **Visual Background**: Set background to **Image** > upload `assets/Peach Bg Image.jpg`.
   - **Visual Icon**: Place the icon `assets/icon_fare.png` on the left.
4. **Customer Retention Rate KPI**:
   - **Indicator**: `Customer Retention Rate` (No display units, 2 decimal places, e.g. `0.99`)
   - **Trend axis**: `Calendar[Date]` (or `Calendar[Year Month]`)
   - **Target**: `Previous Month Retention`
   - **Visual Background**: Set background to **Image** > upload `assets/Purple Bg Theme.jpg`.
   - **Visual Icon**: Place the icon `assets/icon_retention.png` on the left.

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
