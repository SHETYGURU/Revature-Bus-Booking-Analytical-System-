# Project Walkthrough - Bus Booking Analytics System (Tableau)

This document provides a summary of the Tableau data pipeline execution, details on the injected "dirty" data anomalies, and key analytical queries retrieved from the database.

---

## ETL Transformation & Cleaning Report

Our ETL pipeline (`etl_pipeline/etl_pipeline.py`) processes the raw datasets and records the following operations:

### 1. Deduplication
- **Anomaly**: Duplicated `Booking_ID` rows (5% duplicate rate injected).
- **Resolution**: Removed **979 duplicate booking records** (retaining the first unique occurrence).

### 2. Null Value Resolution
- **Anomaly**: Null/empty phone numbers for some customers, missing `Fare_Amount` in bookings.
- **Resolution**:
  - Filled **21 missing customer phone numbers** with the placeholder `'Unknown'`.
  - Dropped **390 booking records** that had missing `Fare_Amount` values.
  - Filled **9 missing customer genders** with `'Female'`.
  - Filled **16 missing customer ages** with the median age.

### 3. Date Standardization
- **Anomaly**: Date columns containing mixed date string formats (e.g., `DD/MM/YYYY`, `MM-DD-YYYY`, and `YYYY-MM-DD`).
- **Resolution**: Cleaned and standardised all mixed formats to standard `YYYY-MM-DD` representation without dropping rows (using Pandas `format='mixed'`).

### 4. Constraint Enforcement
- **Anomaly**: Negative fares (e.g., `-250.0`) and bookings where `Travel_Date` was set before `Booking_Date`.
- **Resolution**:
  - Dropped **286 bookings** with non-positive `Fare_Amount`.
  - Dropped **372 bookings** where the `Travel_Date` occurred before the `Booking_Date`.
  - Corrected **30 age outliers** (< 18 or > 100) to the median customer age of **48**.

### 5. Physical Capacity Check
- **Anomaly**: Seat bookings assigned numbers exceeding the bus capacity (e.g. seat numbers > 40 for sleepers).
- **Resolution**: Dropped **186 bookings** violating physical seat limits.

---

## Summary of Dataset Counts

| Dataset Name | Raw Rows | Cleaned Rows | Rows Removed / Handled |
| :--- | :---: | :---: | :---: |
| **Bookings** | 20,562 | 18,349 | 2,213 removed |
| **Customers** | 301 | 301 | 21 phone numbers corrected |
| **Buses** | 11 | 11 | 0 removed (casings cleaned) |
| **Routes** | 11 | 11 | 0 removed (casings cleaned) |

---

## Verification & Analytical Queries (MySQL Database)

Below are the key business insights retrieved from the SQLite database `data/bus_booking_analytics.db` (and identically loaded into MySQL `bus_booking_tableau`) after pipeline execution:

### 1. KPI Metrics Summary
- **Total Ingested Bookings**: 18,349 records
- **Total Revenue**: $15,195,322.69
- **Average Fare per Booking**: $828.13

### 2. Top 5 High-Revenue Routes
| Source | Destination | Booking Count | Route Revenue |
| :--- | :--- | :---: | :---: |
| Mumbai | Ahmedabad | 1,835 | $1,876,147.77 |
| Kolkata | Patna | 1,629 | $1,846,206.03 |
| Chennai | Hyderabad | 1,533 | $1,826,969.45 |
| Bangalore | Hyderabad | 1,720 | $1,825,724.55 |
| Hyderabad | Bangalore | 1,617 | $1,755,917.79 |

### 3. Revenue Allocation by Coach Type
- **AC Sleeper**: $4,262,502.50 (4,696 bookings)
- **Non-AC Sleeper**: $4,105,159.76 (4,513 bookings)
- **AC Seater**: $3,987,542.34 (5,385 bookings)
- **Non-AC Seater**: $2,840,118.09 (3,755 bookings)

---

## Accessing the Outputs
The cleaned files are available in CSV format in the [data/clean/](file:///c:/Users/user/Desktop/Revature%20Phase%202/Bus%20Booking%20Analytics%20System(Tableau)/data/clean/) folder, and the SQLite database is located at [data/bus_booking_analytics.db](file:///c:/Users/user/Desktop/Revature%20Phase%202/Bus%20Booking%20Analytics%20System(Tableau)/data/bus_booking_analytics.db). The production MySQL database name is **`bus_booking_tableau`**.
