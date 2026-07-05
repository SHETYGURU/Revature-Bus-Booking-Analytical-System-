# Power BI Dashboard Setup & Visualisation Guide

This guide details how to establish database connections, model the tables, write DAX measures, and design the interactive dashboard in **Power BI Desktop** using the cleaned datasets.

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
4. Enter credentials (user/password) and import `Bookings`, `Customers`, `Buses`, and `Routes`.
*Note: You may need to install the MySQL Connector Net dependency if prompted by Power BI.*

---

## 2. Data Modeling & Relationships (Star Schema)

Once the tables are loaded, switch to the **Model View** (left-hand sidebar) and establish the relationships to construct a clean star schema:

1. Drag **Customer_ID** from `Customers` to `Bookings` (1 to Many, Single Direction).
2. Drag **Bus_ID** from `Buses` to `Bookings` (1 to Many, Single Direction).
3. Drag **Route_ID** from `Routes` to `Bookings` (1 to Many, Single Direction).

```
  ┌────────────────┐         ┌───────────────┐
  │   Customers    │         │     Buses     │
  │ (Customer_ID)  │         │   (Bus_ID)    │
  └───────┬────────┘         └───────┬───────┘
          │ 1                        │ 1
          │                          │
          │ ───* ┌──────────────┐ *───┘
          ├──────┤   Bookings   ├──────┐
          │      └──────────────┘      │
          │ *                          │ *
          │                            │
          │                          1 │
  ┌───────┴────────┐                   │
  │     Routes     ├───────────────────┘
  │   (Route_ID)   │
  └────────────────┘
```

---

## 3. Key Business DAX Measures

Create a new table (e.g., `_Measures`) and write the following DAX formulas to populate the business metrics (Section 9):

### Total Bookings
```dax
Total Bookings = COUNT(Bookings[Booking_ID])
```

### Total Revenue
```dax
Total Revenue = SUM(Bookings[Fare_Amount])
```

### Average Fare per Booking
```dax
Average Fare = DIVIDE([Total Revenue], [Total Bookings], 0)
```

### Unique Customers
```dax
Unique Customers = DISTINCTCOUNT(Bookings[Customer_ID])
```

### Customer Retention Rate
Percentage of customers who have made more than one booking.
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

### Seat Occupancy Rate
Estimating seat bookings against total available capacity (assuming 10 scheduled trips per bus in this dataset duration).
```dax
Occupancy Rate = 
VAR TotalCapacity = SUMX(Buses, Buses[Capacity] * 10)
RETURN 
    DIVIDE([Total Bookings], TotalCapacity, 0)
```

---

## 4. Dashboard Design & Layout (Section 8)

Design a 2-page report using a sleek dark theme or corporate blue/slate palette:

### Page 1: Executive Revenue & Booking Trends
- **KPI Cards (Top Bar)**:
  - Total Revenue (formatted as Currency)
  - Total Bookings
  - Average Fare
  - Customer Retention Rate
- **Booking Trends (Line Chart)**:
  - **Visual Type**: Select the **Line chart** visual.
  - **Fields Configuration**:
    - **X-axis**: Drag `Bookings[Booking_Date]`. Right-click this field in the axis well and ensure it is set to **Date Hierarchy** (enables drill down from Year -> Quarter -> Month -> Day) or switch to raw `Booking_Date` for a continuous timeline view.
    - **Y-axis**: Drag the `[Total Bookings]` measure (left scale).
    - **Secondary Y-axis**: Drag the `[Total Revenue]` measure (right scale). This creates a dual-axis trend chart overlaying booking volume and financial revenue.
  - **Visual Formatting (Format Pane)**:
    - **Lines**:
      - Under *Series*, select *All*. Set **Line Type** to **Smooth** (creates premium curved wave lines instead of straight jagged angles). Set **Stroke width** to `3px`.
    - **Colors**:
      - Set `Total Bookings` line color to Cyan/Electric Blue (`#06B6D4`).
      - Set `Total Revenue` line color to Vibrant Amber/Gold (`#F59E0B`).
    - **Markers**:
      - Turn **On** markers. Set shape to **Circle**, size to `5pt`, and turn on *Show border* (white color, `1px` width) for a polished, dot-indicator appearance.
    - **Gridlines**:
      - Under *Gridlines*, turn **Off** vertical lines. Set **Horizontal lines** to **Dotted**, color to light gray (`#E2E8F0`), and transparency to `50%`.
    - **Data Labels**:
      - Turn **On** data labels ONLY if filtering down to a small date range (e.g. 1 month) to prevent visual clutter. Under label settings, select *Values* > set *Display units* to *Auto*.
    - **Title**:
      - Set title text to: `Booking and Revenue Trends Over Time`
      - Font: `Segoe UI Semibold`, size `14pt`, bold, and centered.
    - **Tooltip**:
      - Ensure default tooltips are active so hovering over any marker displays the specific Date, exact Bookings count, and total Revenue formatted as Currency.
- **Revenue by Bus Coach Type (Donut/Pie Chart)**:
  - Legend: `Buses[Bus_Type]`
  - Values: `[Total Revenue]`
- **Top 5 Routes by Revenue (Horizontal Bar Chart)**:
  - Axis: `Routes[Source]` & `Routes[Destination]` (concatenated)
  - Values: `[Total Revenue]`

### Page 2: Operational Performance & Demographics
- **Customer Distribution (Table / Treemap)**:
  - Category: `Customers[Name]`
  - Value: `[Total Bookings]`
- **Seat Occupancy Rate (Gauge Visual)**:
  - Target value: `0.80` (80% goal)
  - Value: `[Occupancy Rate]`
- **Interactive Slicers / Filters (Left Sidebar)**:
  - **Date Range Slider**: `Bookings[Booking_Date]`
  - **Route Selector**: `Routes[Source] -> Routes[Destination]`
  - **Bus Type Filter**: `Buses[Bus_Type]`
  - **Booking Status Filter**: `Bookings[Booking_Status]`
