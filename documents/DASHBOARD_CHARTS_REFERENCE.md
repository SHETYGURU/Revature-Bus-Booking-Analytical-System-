# Bus Booking Analytics - Page-by-Page Chart & Business Rationale Guide

This reference document defines the complete visual inventory for all 7 dashboard pages under the **Nordic Ocean Top-Horizontal Navigation** grid layout. Each visual includes type, coordinates, field settings, and the **business problem it solves**.

---

## Page 1: Overview (Executive Health & High-Level KPIs)
*Provides a high-level summary of operational health, gross cash flows, and key performance signals for leadership.*

### 1. Top KPI Row (Card Visual - New)
*   **Visual Type**: Card (new)
*   **Coordinates**: X = `15px`, Y = `85px`, Width = `1250px`, Height = `120px` (4 columns side-by-side)
*   **Fields**: `[Total Revenue]`, `[Total Bookings]`, `[Average Fare]`, `[Customer Retention Rate]`
*   **Why it is used**: Instantly displays the primary health indicators of the business. Leadership can immediately grasp current revenue scale, purchase volume, average customer ticket price, and brand loyalty without looking at granular details.

### 2. Daily Bookings & Revenue Trend (Dual-Axis Line Chart)
*   **Visual Type**: Line Chart (with dual Y-axes)
*   **Coordinates**: X = `15px`, Y = `220px`, Width = `610px`, Height = `240px`
*   **Fields**: X-axis: `Calendar[Date]`, Y-axis 1: `[Total Bookings]`, Y-axis 2: `[Total Revenue]`
*   **Why it is used**: Solves **operational seasonality**. Shows if booking spikes correlate with revenue spikes over time, helping management identify high-travel seasons, holiday trends, and mid-week dips.

### 3. Share of Revenue by Bus Category (Donut Chart)
*   **Visual Type**: Donut Chart
*   **Coordinates**: X = `645px`, Y = `220px`, Width = `620px`, Height = `240px`
*   **Fields**: Legend: `buses[Bus_Type]`, Values: `[Total Revenue]`
*   **Why it is used**: Solves **product category yield**. Identifies which bus class (e.g., AC Sleeper vs. AC Seater) brings in the bulk of money. This tells management which segment has the highest pricing power.

### 4. Top Passenger Sourced Cities (Horizontal Bar Chart)
*   **Visual Type**: Clustered Bar Chart (horizontal)
*   **Coordinates**: X = `15px`, Y = `475px`, Width = `610px`, Height = `230px`
*   **Fields**: Y-axis: `routes[Source]`, X-axis: `[Total Revenue]`
*   **Why it is used**: Solves **market footprint analysis**. Pinpoints where the demand/revenue originates geographically, directly guiding regional marketing spend.

### 5. Detailed Booking Status Breakdown (Card Visual - New)
*   **Visual Type**: Card (new)
*   **Coordinates**: X = `645px`, Y = `475px`, Width = `620px`, Height = `230px`
*   **Fields**: `[Confirmed Bookings]`, `[Cancelled Bookings]`, `[Pending Bookings]`
*   **Why it is used**: Monitors **transaction completion quality**. Tracks leakage due to cancellations and helps alert staff to pending/unpaid booking backlogs.

---

## Page 2: Bookings (Operational Volume & Booking Behavior)
*Analyzes transaction throughput, customer planning habits, and route loads.*

### 1. Monthly Travel Demand (Area Chart)
*   **Visual Type**: Area Chart
*   **Coordinates**: X = `15px`, Y = `85px`, Width = `560px`, Height = `280px`
*   **Fields**: X-axis: `Calendar[Date]`, Y-axis: `[Total Bookings]`
*   **Why it is used**: Visualizes the **volume curve** of passenger travel. Area shading highlights peak operational load days, helping operations allocate drivers and maintain buses.

### 2. Booking Lead Time Distribution (Donut Chart)
*   **Visual Type**: Donut Chart
*   **Coordinates**: X = `590px`, Y = `85px`, Width = `310px`, Height = `280px`
*   **Fields**: Legend: `Lead Time Group` (Same Day, 1-3 Days, etc.), Values: `[Total Bookings]`
*   **Why it is used**: Solves **customer planning behavior**. Knowing if customers book last-minute or weeks in advance tells dynamic pricing systems when to raise fares and guides booking window restrictions.

### 3. Slicer/Status Breakdown (Clustered Column Chart)
*   **Visual Type**: Clustered Column Chart
*   **Coordinates**: X = `915px`, Y = `85px`, Width = `350px`, Height = `280px`
*   **Fields**: X-axis: `bookings[Booking_Status]`, Y-axis: `[Total Bookings]`
*   **Why it is used**: Displays the ratio of successful vs cancelled volume visually. Useful for immediate comparison of cancellation spikes.

### 4. Coach Status Matrix Table (Matrix)
*   **Visual Type**: Matrix Table
*   **Coordinates**: X = `15px`, Y = `385px`, Width = `700px`, Height = `310px`
*   **Fields**: Rows: `buses[Bus_Type]`, Values: `[Confirmed Bookings]`, `[Cancelled Bookings]`, `[Pending Bookings]`
*   **Why it is used**: Identifies if a specific coach category has **unusually high cancellations** (e.g. if AC Sleepers are getting cancelled more, there might be a pricing or quality issue with that specific fleet).

### 5. Passenger Traffic by Route Corridor (Horizontal Bar Chart)
*   **Visual Type**: Clustered Bar Chart (horizontal)
*   **Coordinates**: X = `730px`, Y = `385px`, Width = `535px`, Height = `310px`
*   **Fields**: Y-axis: `Route_Path` (Source-Destination), X-axis: `[Total Bookings]`
*   **Why it is used**: Solves **fleet routing load**. Identifies high-traffic corridors, signaling the need to add more weekly departures to maximize capacity.

---

## Page 3: Revenue (Yields & Price Optimization)
*Identifies revenue trends, pricing yields, and ticket fare distribution.*

### 1. Cumulative Revenue Growth (Line Chart)
*   **Visual Type**: Line Chart
*   **Coordinates**: X = `15px`, Y = `85px`, Width = `610px`, Height = `280px`
*   **Fields**: X-axis: `Calendar[Date]`, Y-axis: `Cumulative Revenue` (running total)
*   **Why it is used**: Tracks **running financial performance** against yearly targets. The steepness of the curve indicates the rate of sales acceleration.

### 2. Revenue Contributed by Coach Type (Pie Chart)
*   **Visual Type**: Pie Chart
*   **Coordinates**: X = `645px`, Y = `85px`, Width = `620px`, Height = `280px`
*   **Fields**: Legend: `buses[Bus_Type]`, Values: `[Total Revenue]`
*   **Why it is used**: Helps managers see which vehicle class drives the most money to optimize coach acquisitions.

### 3. Fare Ticket Price Distribution (Clustered Column Chart)
*   **Visual Type**: Clustered Column Chart
*   **Coordinates**: X = `15px`, Y = `385px`, Width = `610px`, Height = `310px`
*   **Fields**: X-axis: `Fare_Range` (calculated bins like $10-20, $20-30), Y-axis: `[Total Bookings]`
*   **Why it is used**: Solves **price elasticity analysis**. Shows the ticket price ranges where the majority of transactions occur, identifying the "sweet spot" for baseline ticket pricing.

### 4. Sales Yield per Route Corridor (Horizontal Bar Chart)
*   **Visual Type**: Clustered Bar Chart (horizontal)
*   **Coordinates**: X = `645px`, Y = `385px`, Width = `620px`, Height = `310px`
*   **Fields**: Y-axis: `Route_Path` (Source-Destination), X-axis: `[Total Revenue]`
*   **Why it is used**: Highlights which travel paths generate the highest sales volume, identifying prime corridors for premium price adjustments.

---

## Page 4: Customers (Demographics & Customer Behavior)
*Tracks passenger demographics, gender balance, age brackets, and customer value.*

### 1. Passenger Gender Split (Pie Chart)
*   **Visual Type**: Pie Chart
*   **Coordinates**: X = `15px`, Y = `85px`, Width = `380px`, Height = `280px`
*   **Fields**: Legend: `customers[Gender]`, Values: `[Total Bookings]`
*   **Why it is used**: Analyzes demographic balance to tailor onboard marketing and safety messaging.

### 2. Passenger Volume by Age Bracket (Clustered Column Chart)
*   **Visual Type**: Clustered Column Chart
*   **Coordinates**: X = `410px`, Y = `85px`, Width = `430px`, Height = `280px`
*   **Fields**: X-axis: `customers[Age_Group]` (Under 25, 25-45, 45+), Y-axis: `[Total Bookings]`
*   **Why it is used**: Solves **target audience profiling**. Helps target specific age cohorts with booking campaigns (e.g. student discounts for under 25, executive sleeping layouts for 25-45).

### 3. Customer Retention Rate Target (Gauge Visual)
*   **Visual Type**: Gauge Visual
*   **Coordinates**: X = `855px`, Y = `85px`, Width = `410px`, Height = `280px`
*   **Fields**: Value: `_Measures[Customer Retention Rate]`, Target: `0.80` (80% goal)
*   **Why it is used**: Monitors **customer loyalty and repeat bookings**. Measures retention performance against a corporate goal to flag if customer attrition is rising.

### 4. Customer High-Value Table (Table)
*   **Visual Type**: Table
*   **Coordinates**: X = `15px`, Y = `385px`, Width = `1250px`, Height = `310px`
*   **Fields**: `Customer_ID`, `Name`, `Gender`, `Age`, `Total Bookings`, `Total Revenue`
*   **Why it is used**: Lists top customers for VIP loyalty outreach programs.

---

## Page 5: Bus Types (Asset Utilization & Capacity)
*Analyzes vehicle performance and maps fleet configuration efficiency.*

### 1. Average Fleet Occupancy Goal (Gauge Visual)
*   **Visual Type**: Gauge Visual
*   **Coordinates**: X = `15px`, Y = `85px`, Width = `350px`, Height = `280px`
*   **Fields**: Value: `_Measures[Occupancy Rate]`, Target: `0.80` (80% load target)
*   **Why it is used**: Measures **fleet capacity utilization**. Tells management if buses are traveling empty, indicating if departures should be consolidated.

### 2. Fleet Configuration Spread (Pie Chart)
*   **Visual Type**: Pie Chart
*   **Coordinates**: X = `380px`, Y = `85px`, Width = `430px`, Height = `280px`
*   **Fields**: Legend: `buses[Bus_Type]`, Values: `buses[Bus_Number]` (Distinct Count)
*   **Why it is used**: Displays fleet mix at a glance to manage vehicle procurement and maintenance schedules.

### 3. Fleet Seating Demand Split (Donut Chart)
*   **Visual Type**: Donut Chart
*   **Coordinates**: X = `825px`, Y = `85px`, Width = `440px`, Height = `280px`
*   **Fields**: Legend: `buses[Bus_Type]`, Values: `[Total Bookings]`
*   **Why it is used**: Compares fleet mix against actual passenger demand to align vehicle purchases with customer preferences.

### 4. Asset Performance & Yield Table (Table)
*   **Visual Type**: Table
*   **Coordinates**: X = `15px`, Y = `385px`, Width = `1250px`, Height = `310px`
*   **Fields**: `Bus_ID`, `Bus_Number`, `Bus_Type`, `Capacity`, `Total Bookings`, `Total Revenue`, `Occupancy Rate`
*   **Why it is used**: Pinpoints underperforming buses with low occupancy rates or low revenue to schedule them for route adjustments.

---

## Page 6: Routes (Geographical Performance & Mileage Yield)
*Pinpoints the most profitable corridors and checks mileage yield.*

### 1. Stepped Corridor Matrix (Matrix)
*   **Visual Type**: Matrix Table
*   **Coordinates**: X = `15px`, Y = `85px`, Width = `780px`, Height = `280px`
*   **Fields**: Rows: `routes[Source]` > `routes[Destination]`, Values: `[Total Bookings]`, `[Total Revenue]`, `[Occupancy Rate]`
*   **Why it is used**: Allows dynamic exploration of route performance. Expand source cities to immediately view which destinated corridors drive performance.

### 2. Source Hub Traffic Share (Donut Chart)
*   **Visual Type**: Donut Chart
*   **Coordinates**: X = `815px`, Y = `85px`, Width = `450px`, Height = `280px`
*   **Fields**: Legend: `routes[Source]`, Values: `[Total Bookings]`
*   **Why it is used**: Tracks station loads to manage employee staffing and bus parking space.

### 3. Revenue by Route Corridor (Horizontal Bar Chart)
*   **Visual Type**: Clustered Bar Chart (horizontal)
*   **Coordinates**: X = `15px`, Y = `385px`, Width = `780px`, Height = `310px`
*   **Fields**: Y-axis: `Route_Path` (Source-Destination), X-axis: `[Total Revenue]`
*   **Why it is used**: Ranks routes by sales output to allocate premium marketing budgets.

### 4. Mileage Yield Correlation (Scatter Plot)
*   **Visual Type**: Scatter Chart
*   **Coordinates**: X = `815px`, Y = `385px`, Width = `450px`, Height = `310px`
*   **Fields**: X-axis: `routes[Distance]`, Y-axis: `[Total Revenue]`, Details: `Route_ID`
*   **Why it is used**: Solves **distance-to-yield efficiency**. Shows if longer distances yield proportionally higher revenues, helping spot routes that are underpriced for their fuel distance cost.

---

## Page 7: Reports (Master Transaction Ledger)
*A dedicated detail ledger page for tracking individual bookings, searching, and exporting data.*

### 1. Top Right Slicer (Search Bar Slicer)
*   **Visual Type**: Dropdown Slicer with Search enabled
*   **Coordinates**: X = `1015px`, Y = `85px`, Width = `250px`, Height = `50px`
*   **Fields**: `customers[Name]` (Search box activated via visual header `...`)
*   **Why it is used**: Quick lookup tool. Front-desk staff can search a customer's name to display their entire booking history.

### 2. Master Booking Ledger (Table)
*   **Visual Type**: Table Visual
*   **Coordinates**: X = `15px`, Y = `150px`, Width = `1250px`, Height = `550px`
*   **Fields**: `Booking_ID`, `Booking_Date`, `Travel_Date`, `Customer Name`, `Bus Number`, `Route (Source-Dest)`, `Fare_Amount`, `Booking_Status`
*   **Why it is used**: The primary audit log. Used to export clean transactional data to CSV for external audits or passenger check-in verification.
