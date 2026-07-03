# Bus Booking Analytics System

Welcome to the **Bus Booking Analytics System**, an end-to-end data engineering and analytics solution designed to ingest, cleanse, validate, and query bus booking operations, customer distribution, and revenue trends.

This project implements a multi-tier relational model using **Python** for ETL, **SQLite** for local development, **MySQL** for relational persistence, and **Power BI** for visual intelligence.

---

## Technology Stack
- **Data Engineering & Analysis**: Python 3.10+, Pandas, NumPy
- **Relational Databases**: SQLite (local development), MySQL (production persistence)
- **Interactive UI & Presentation**: Jupyter Notebooks (`.ipynb`)
- **Business Intelligence**: Power BI

---

## Repository Structure
```
Bus Booking Analytics System/
│
├── documents/                               # Project Specs, Reference Data & Core Docs
│   ├── Bus Booking Analytics System.pdf     # System Objectives & Architecture Spec
│   ├── bus_booking_1000_rows.csv            # Original baseline booking CSV
│   ├── WALKTHROUGH.md                       # Detailed cleaning stats & SQL analytics
│   └── WORK_STRUCTURE.md                    # WBS & development workflow sequence
│
├── data/                                    # Active Datasets Directory
│   ├── bus_booking_raw.csv                  # Newly generated dirty bookings (>2,000 rows)
│   ├── customers.csv                        # Raw Customers list (injected casing & phone nulls)
│   ├── buses.csv                            # Buses list (types & capacities)
│   ├── routes.csv                           # Routes list (source, destination, distance)
│   ├── bus_booking_analytics.db             # Local SQLite database with populated clean tables
│   └── clean/                               # Cleansed, standardized, and validated CSV files
│       ├── bookings_clean.csv
│       ├── customers_clean.csv
│       ├── buses_clean.csv
│       └── routes_clean.csv
│
├── data_generation/                         # Generation Module
│   ├── data_generator.py                    # Generation script (seeds 2,100 records + anomalies)
│   └── data_generation.ipynb                # Notebook detailing the generation strategy
│
├── etl_pipeline/                            # ETL Pipeline Module
│   ├── etl_pipeline.py                      # Cleansing, parsing, and SQL database loading script
│   └── etl_pipeline.ipynb                   # Execution notebook with cleaning logs & SQL analytics
│
└── README.md                                # This main documentation file
```

---

## Key Project Use Cases & Applications

### 1. Route Profitability & Optimization
- **Goal**: Identify which routes generate the highest sales volume and travel demand to optimize route allocations.
- **Application**: By analyzing SQL aggregates, we discovered that the **Chennai - Hyderabad** route generates the highest revenue ($180,185.00), while **Mumbai - Ahmedabad** has the highest booking frequency (178 bookings). Operators can allocate more premium AC Sleeper coaches to these routes to maximize returns.

### 2. Dynamic Pricing & Fare Optimization
- **Goal**: Evaluate fare structures across bus types and travel distances.
- **Application**: The ETL logs show that Seater buses (both AC and Non-AC) generate more than 60% of total booking revenue due to higher passenger capacity. Dynamic pricing tiers can be modeled based on booking dates vs travel dates to capture premiums during last-minute travel windows.

### 3. Capacity & Supply Chain Integrity
- **Goal**: Prevent booking overlaps and coach over-selling.
- **Application**: The ETL capacity engine automatically intercepts bookings where the seat number exceeds the physical bus capacity, preventing operational issues (such as over-allocating seats on Sleeper buses limited to 40 passengers).

### 4. Automated Data Quality Control (ETL Gatekeeper)
- **Goal**: Keep database structures clean and standardized.
- **Application**: The pipeline standardizes mixed date strings (e.g. `DD/MM/YYYY` and `MM-DD-YYYY`) into ISO standard format `YYYY-MM-DD` and drops bookings with negative prices or corrupt foreign keys. This ensures Power BI models consume clean, validated records without encountering runtime rendering errors.

---

## Getting Started

### 1. Installation
Ensure you have Python installed, then install the required libraries:
```bash
pip install pandas numpy mysql-connector-python jupyter
```

### 2. Running the Data Generator
To regenerate the raw dirty dataset (2,100 rows + anomalies):
```bash
python data_generation/data_generator.py
```
Or open and execute the cells in **[data_generation.ipynb](file:///c:/Users/user/Desktop/Revature%20Phase%202/Bus%20Booking%20Analytics%20System/data_generation/data_generation.ipynb)**.

### 3. Running the ETL Pipeline
To clean the dirty data, standardize formats (mixed date formats), perform integrity checks, and load into the databases:
```bash
python etl_pipeline/etl_pipeline.py
```
Or open and execute the cells in **[etl_pipeline.ipynb](file:///c:/Users/user/Desktop/Revature%20Phase%202/Bus%20Booking%20Analytics%20System/etl_pipeline/etl_pipeline.ipynb)**.

---

## Contributors and Team Structure

Below is the team structure for the project:

| Team Member | Role | Profile & Responsibilities |
| :--- | :--- | :--- |
| **Gururaj Shetty (SHETYGURU)** | Project Lead & Core Data Engineer | **GitHub**: [SHETYGURU](https://github.com/SHETYGURU) <br> **Email**: shettygururaj279@gmail.com <br> Developed the dataset generator, built the ETL validation pipeline, configured SQLite/MySQL DB connections, and drafted the documentation structure. |
| **Developer 2** | *[Vacant]* | SQL schema optimization and staging tests. |
| **Developer 3** | *[Vacant]* | Power BI dashboard design and metric KPI report creations. |

---

## Project Documentation Links
- **Detailed Cleaning Results & Database Counts**: See **[WALKTHROUGH.md](file:///c:/Users/user/Desktop/Revature%20Phase%202/Bus%20Booking%20Analytics%20System/documents/WALKTHROUGH.md)**.
- **Work Breakdown Structure & Sequences**: See **[WORK_STRUCTURE.md](file:///c:/Users/user/Desktop/Revature%20Phase%202/Bus%20Booking%20Analytics%20System/documents/WORK_STRUCTURE.md)**.
