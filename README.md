# Bus Booking Analytics System 🚌📊

Welcome to the **Bus Booking Analytics System**, an end-to-end data engineering and analytics solution designed to ingest, cleanse, validate, and query bus booking operations, customer distribution, and revenue trends.

This project implements a multi-tier relational model using **Python** for ETL, **SQLite** for local development, **MySQL** for relational persistence, and **Power BI** for visual intelligence.

---

## 🛠️ Technology Stack
- **Data Engineering & Analysis**: Python 3.10+, Pandas, NumPy
- **Relational Databases**: SQLite (local development), MySQL (production persistence)
- **Interactive UI & Presentation**: Jupyter Notebooks (`.ipynb`)
- **Business Intelligence**: Power BI

---

## 📁 Repository Structure
```
Bus Booking Analytics System/
│
├── documents/                               # Project Specs & Raw Reference Data
│   ├── Bus Booking Analytics System.pdf     # System Objectives & Architecture Spec
│   ├── bus_booking_1000_rows.csv            # Original baseline booking CSV
│   ├── WALKTHROUGH.md                       # Detailed cleaning statistics and metrics
│   ├── CONTRIBUTORS.md                      # Team structure (3 members)
│   └── WORK_STRUCTURE.md                    # Work Breakdown Structure (WBS) & roles
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

## 🚀 Getting Started

### 1. Installation
Ensure you have Python installed, then install the required libraries:
```bash
pip install pandas numpy mysql-connector-python jupyter
```

### 2. Running the Data Generator
To regenerate the large dirty dataset (2,100 rows + anomalies):
```bash
python data_generation/data_generator.py
```
Or open and execute the cells in [data_generation.ipynb](file:///c:/Users/user/Desktop/Revature%20Phase%202/Bus%20Booking%20Analytics%20System/data_generation/data_generation.ipynb).

### 3. Running the ETL Pipeline
To clean the dirty data, standardise formats (e.g. mixed date string parsing), perform validation checks, and load into the databases:
```bash
python etl_pipeline/etl_pipeline.py
```
Or open and execute the cells in [etl_pipeline.ipynb](file:///c:/Users/user/Desktop/Revature%20Phase%202/Bus%20Booking%20Analytics%20System/etl_pipeline/etl_pipeline.ipynb).

---

## 📊 Key Highlights & Results
- **Deduplication**: Successfully deduplicates raw records using Primary Keys (`Booking_ID`).
- **Mixed Date Handling**: Parses varied dates (e.g., `DD/MM/YYYY`, `MM-DD-YYYY`, `YYYY-MM-DD`) into standard format without dropping rows.
- **Referential Checks**: Ensures all bookings align with valid Customers, Buses, and Routes.
- **Seat Capacities**: Ensures seat bookings do not exceed the physical capacity limits of coaches.

For a detailed analysis of the results, query counts, and database structures, please see **[WALKTHROUGH.md](file:///c:/Users/user/Desktop/Revature%20Phase%202/Bus%20Booking%20Analytics%20System/documents/WALKTHROUGH.md)**.
