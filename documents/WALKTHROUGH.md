# Project Walkthrough - Bus Booking Analytics System

This document provides a summary of the data pipeline execution, details on the injected "dirty" data anomalies, and key analytical queries retrieved from the database.

---

## ETL Transformation & Cleaning Report

Our ETL pipeline (`etl_pipeline/etl_pipeline.py`) acts as the gatekeeper for data quality. The script processes the raw datasets and outputs the following cleaning operations:

### 1. Deduplication
- **Anomaly**: 100 rows containing duplicated `Booking_ID` values.
- **Resolution**: Removed **100 duplicate booking records** (retaining the first unique occurrence).

### 2. Null Value Resolution
- **Anomaly**: Null/empty phone numbers for some customers, missing `Fare_Amount` in bookings.
- **Resolution**:
  - Filled **21 missing customer phone numbers** with the placeholder `'Unknown'`.
  - Dropped **39 booking records** that had missing `Fare_Amount` values.

### 3. Date Standardization
- **Anomaly**: Date columns containing mixed date string formats (e.g., `DD/MM/YYYY`, `MM-DD-YYYY`, and `YYYY-MM-DD`).
- **Resolution**: Cleaned and standardised all mixed formats to standard `YYYY-MM-DD` representation without dropping rows (using Pandas `format='mixed'`).

### 4. Constraint Enforcement
- **Anomaly**: Negative fares (e.g., `-250.0`) and bookings where `Travel_Date` was set before `Booking_Date`.
- **Resolution**:
  - Dropped **27 bookings** with non-positive `Fare_Amount`.
  - Dropped **40 bookings** where the `Travel_Date` occurred before the `Booking_Date`.

### 5. Physical Capacity Check
- **Anomaly**: Seat bookings assigned numbers (e.g., seat 48) exceeding the bus capacity (e.g. max 40 for sleepers).
- **Resolution**: Dropped **18 bookings** violating physical seat limits.

---

## Summary of Dataset Counts

| Dataset Name | Raw Rows | Cleaned Rows | Rows Removed / Handled |
| :--- | :---: | :---: | :---: |
| **Bookings** | 2,100 | 1,876 | 224 removed |
| **Customers** | 301 | 301 | 21 phone numbers corrected |
| **Buses** | 11 | 11 | 0 removed (casings cleaned) |
| **Routes** | 11 | 11 | 0 removed (casings cleaned) |

---

## Verification & Analytical Queries (SQLite Database)

Below are the key business insights retrieved from the SQLite database `data/bus_booking_analytics.db` after loading:

### 1. KPI Metrics Summary
- **Total Ingested Bookings**: 1,876 records
- **Total Revenue**: $1,462,220.00
- **Average Fare per Booking**: $779.43

### 2. Top 5 High-Revenue Routes
| Source | Destination | Booking Count | Route Revenue |
| :--- | :--- | :---: | :---: |
| Chennai | Hyderabad | 163 | $180,185.00 |
| Kolkata | Patna | 172 | $177,140.00 |
| Bangalore | Hyderabad | 173 | $174,565.00 |
| Mumbai | Ahmedabad | 178 | $168,740.00 |
| Hyderabad | Bangalore | 160 | $160,850.00 |

### 3. Revenue Allocation by Coach Type
- **Non-AC Seater**: $534,450.00 (791 bookings)
- **AC Seater**: $429,900.00 (637 bookings)
- **Non-AC Sleeper**: $297,870.00 (438 bookings)
- **AC Sleeper**: $200,000.00 (304 bookings)

---

## Accessing the Outputs
The cleaned files are available in CSV format in the [data/clean/](file:///c:/Users/user/Desktop/Revature%20Phase%202/Bus%20Booking%20Analytics%20System/data/clean/) folder, and the fully populated database file is located at [data/bus_booking_analytics.db](file:///c:/Users/user/Desktop/Revature%20Phase%202/Bus%20Booking%20Analytics%20System/data/bus_booking_analytics.db).
