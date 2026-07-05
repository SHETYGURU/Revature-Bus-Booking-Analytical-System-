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

Design a 2-page report using a sleek dark theme or corporate blue/slate palette, placing a unified **Filter Pane / Sidebar** on both pages and enabling **Sync Slicers** so filters apply globally across the report.

### Page 1: Executive Revenue & Booking Trends
- **KPI Cards (Top Bar)**:
  - Total Revenue (formatted as Currency)
  - Total Bookings
  - Average Fare
  - Customer Retention Rate
- **Booking Trends (Line Chart)**:
  - Axis: `Bookings[Booking_Date]` (Grouped by Month/Week)
  - Values: `[Total Bookings]` and `[Total Revenue]`
- **Revenue by Bus Coach Type (Donut/Pie Chart)**:
  - Legend: `Buses[Bus_Type]`
  - Values: `[Total Revenue]`
- **Top 5 Routes by Revenue (Horizontal Bar Chart)**:
  - Axis: `Routes[Source]` & `Routes[Destination]` (concatenated)
  - Values: `[Total Revenue]`
- **Interactive Slicers (Left/Right Sidebar)**:
  - **Date Range Slider**: `Bookings[Booking_Date]` (Between/Slider)
  - **Route Selector**: `Routes[Source] -> Routes[Destination]` (Dropdown)
  - **Bus Type Filter**: `Buses[Bus_Type]` (Vertical List)
  - **Booking Status**: `Bookings[Booking_Status]` (Horizontal Tile Buttons)

### Page 2: Operational Performance & Demographics
- **Customer Distribution (Table / Treemap)**:
  - Category: `Customers[Name]`
  - Value: `[Total Bookings]`
- **Seat Occupancy Rate (Gauge Visual)**:
  - Target value: `0.80` (80% goal)
  - Value: `[Occupancy Rate]`
- **Interactive Slicers (Left/Right Sidebar - Synced with Page 1)**:
  - **Date Range Slider**: `Bookings[Booking_Date]` (Between/Slider)
  - **Route Selector**: `Routes[Source] -> Routes[Destination]` (Dropdown)
  - **Bus Type Filter**: `Buses[Bus_Type]` (Vertical List)
  - **Booking Status**: `Bookings[Booking_Status]` (Horizontal Tile Buttons)

---

## 5. Synchronizing Slicers Across Pages

To ensure that filtering a value (e.g., selecting *AC Sleeper*) on Page 1 automatically filters Page 2:

1. Click on a Slicer visual on Page 1.
2. In the top ribbon, go to **View** > click on **Sync slicers** to open the panel on the right.
3. In the **Sync slicers panel**:
   - For both **Page 1** and **Page 2**, check the boxes for **Sync** (circular arrow column) and **Visible** (eye icon column).
4. Repeat this step for each of the four slicers.
5. You can now copy and paste the slicers from Page 1 to Page 2 (when prompted to sync, select **Sync**). This creates an identical, linked sidebar on both pages.

