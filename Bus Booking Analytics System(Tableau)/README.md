# Bus Booking Analytics System (Tableau Version)

Welcome to the **Bus Booking Analytics System (Tableau Version)**, an end-to-end data engineering and analytics solution designed to ingest, cleanse, validate, and query bus booking operations, customer distribution, and revenue trends.

This project implements a multi-tier relational model using **Python** for ETL, **SQLite** for local development, **MySQL** for relational persistence, and **Tableau** for business intelligence.

---

## Technology Stack
- **Data Engineering & Analysis**: Python 3.10+, Pandas, NumPy
- **Relational Databases**: SQLite (local development), MySQL (production persistence)
- **Interactive UI & Presentation**: Jupyter Notebooks (`.ipynb`)
- **Business Intelligence**: Tableau Desktop / Tableau Cloud

---

## Repository Structure
```
Bus Booking Analytics System(Tableau)/
│
├── documents/                               # Project Specs, Reference Data & Core Docs
│   ├── TABLEAU_GUIDE.md                     # Tableau Connection, Relationships & Calculated Fields Guide
│   ├── DASHBOARD_DESIGN_GUIDE_TABLEAU.md    # Containers layout, grid configurations & typography
│   ├── DASHBOARD_PAGES_DETAIL_TABLEAU.md    # Page-by-page visual setups & filter containers
│   └── WALKTHROUGH.md                       # Detailed cleaning stats & SQL analytics
│
├── data/                                    # Active Datasets Directory
│   ├── bus_booking_raw.csv                  # Newly generated dirty bookings (~20,000 rows, Seed 100)
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
│   └── data_generator.py                    # Generation script (seeds 20,500+ records + anomalies, Seed 100)
│
├── etl_pipeline/                            # ETL Pipeline Module
│   └── etl_pipeline.py                      # Cleansing, parsing, and SQL database loading script (MySQL: bus_booking_tableau)
│
└── README.md                                # This main documentation file
```

---

## Getting Started

### 1. Installation
Ensure you have Python installed, then install the required libraries:
```bash
pip install pandas numpy mysql-connector-python
```

### 2. Running the Data Generator
To regenerate the raw dirty dataset (approx 20,500 rows + anomalies):
```bash
python data_generation/data_generator.py
```

### 3. Running the ETL Pipeline
To clean the dirty data, standardize formats, perform integrity checks, and load into SQLite and the MySQL production database:
```bash
python etl_pipeline/etl_pipeline.py --mysql --password <mysql_root_password>
```

---

## Project Documentation Links
- **Tableau Connection & Calculated Fields Guide**: See **[TABLEAU_GUIDE.md](documents/TABLEAU_GUIDE.md)** ([local absolute link](file:///c:/Users/user/Desktop/Revature%20Phase%202/Bus%20Booking%20Analytics%20System(Tableau)/documents/TABLEAU_GUIDE.md)).
- **Tableau Layout & Design Specs**: See **[DASHBOARD_DESIGN_GUIDE_TABLEAU.md](documents/DASHBOARD_DESIGN_GUIDE_TABLEAU.md)** ([local absolute link](file:///c:/Users/user/Desktop/Revature%20Phase%202/Bus%20Booking%20Analytics%20System(Tableau)/documents/DASHBOARD_DESIGN_GUIDE_TABLEAU.md)).
- **Tableau Pages & Sheet Configurations**: See **[DASHBOARD_PAGES_DETAIL_TABLEAU.md](documents/DASHBOARD_PAGES_DETAIL_TABLEAU.md)** ([local absolute link](file:///c:/Users/user/Desktop/Revature%20Phase%202/Bus%20Booking%20Analytics%20System(Tableau)/documents/DASHBOARD_PAGES_DETAIL_TABLEAU.md)).
- **Detailed Cleaning Results & Database Counts**: See **[WALKTHROUGH.md](documents/WALKTHROUGH.md)** ([local absolute link](file:///c:/Users/user/Desktop/Revature%20Phase%202/Bus%20Booking%20Analytics%20System(Tableau)/documents/WALKTHROUGH.md)).
