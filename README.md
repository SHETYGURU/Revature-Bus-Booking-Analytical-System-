# Bus Booking Analytics System

Welcome to the unified **Bus Booking Analytics System** repository. This project showcases two parallel implementations of an end-to-end analytical data pipeline, leveraging Python for data extraction, cleaning, and transformation, and visualizing key operations, asset yields, and customer loyalty profiles in two leading business intelligence suites: **Power BI** and **Tableau**.

---

## 📂 Project Subfolders

This repository is split into two primary workspace directories:

| Subfolder | Dashboard Platform | Database Schema | Key Features |
| :--- | :--- | :--- | :--- |
| **📁 [PowerBI Subfolder](Bus%20Booking%20Analytics%20System%20%28PowerBI%29/)** | Power BI (`.pbix`) | `bus_booking_analytics` | Bookmark-driven sliding overlay filter pane, native KPI trend sparklines, and detailed customer cohort demographic gauges. |
| **📁 [Tableau Subfolder](Bus%20Booking%20Analytics%20System%28Tableau%29/)** | Tableau (`.twb`) | `bus_booking_tableau` | Segmented fleet occupancy trends, custom sky blue stencil card icons, and multi-sheet parameter action filtering. |

Both implementations run on a unified Python data engineering backbone:
*   **`data_generation/`**: Simulates raw booking events spanning January 2025 to July 2026, injecting real-world database anomalies (duplicates, invalid dates, out-of-bounds seat allocations, and formatting inconsistencies) and enforcing a strict volume cap of <75 bookings per customer.
*   **`etl_pipeline/`**: Cleans and validates raw tables, standardizes mixed date strings into ISO format (`YYYY-MM-DD`), resolves referential integrity constraints, and loads records directly into **MySQL**.

---

## 👥 The Squad

We are a core team of engineers and architects focused on product-driven systems engineering.

<table align="center" style="width: 100%; border-collapse: collapse; border: 1px solid #30363d; background-color: #0d1117;">
  <tr style="border: none;">
    <td align="center" valign="top" width="33.3%" style="border: 1px solid #30363d; padding: 20px;">
      <img src="https://github.com/SHETYGURU.png" width="100" style="border-radius: 4px; margin-bottom: 10px;" alt="Gururaj Shetty"><br><br>
      <strong><a href="https://github.com/SHETYGURU">Gururaj Shetty</a></strong><br>
      <span style="color: #8b949e; font-size: 14px;">Project Lead & Core Data Engineer</span><br>
      <span style="font-size: 13px; color: #c9d1d9;">GitHub: <a href="https://github.com/SHETYGURU">SHETYGURU</a><br>Email: shettygururaj279@gmail.com</span><br>
      <span style="font-size: 12px; color: #8b949e; display: block; margin-top: 10px;">Developed generator, ETL validation, DB loaders, and docs.</span>
    </td>
    <td align="center" valign="top" width="33.3%" style="border: 1px solid #30363d; padding: 20px;">
      <img src="https://api.dicebear.com/7.x/initials/svg?seed=D2" width="100" style="border-radius: 4px; margin-bottom: 10px;" alt="Developer 2"><br><br>
      <strong>Developer 2</strong><br>
      <span style="color: #8b949e; font-size: 14px;">[Vacant]</span><br>
      <span style="font-size: 13px; color: #c9d1d9;">SQL Schema & Staging</span><br>
      <span style="font-size: 12px; color: #8b949e; display: block; margin-top: 10px;">Responsibilities will include SQL schema optimization and database testing.</span>
    </td>
    <td align="center" valign="top" width="33.3%" style="border: 1px solid #30363d; padding: 20px;">
      <img src="https://api.dicebear.com/7.x/initials/svg?seed=D3" width="100" style="border-radius: 4px; margin-bottom: 10px;" alt="Developer 3"><br><br>
      <strong>Developer 3</strong><br>
      <span style="color: #8b949e; font-size: 14px;">[Vacant]</span><br>
      <span style="font-size: 13px; color: #c9d1d9;">BI & Dashboard Design</span><br>
      <span style="font-size: 12px; color: #8b949e; display: block; margin-top: 10px;">Responsibilities will include Power BI visualization and KPI dashboards.</span>
    </td>
  </tr>
</table>

---

## 🚀 Execution Quickstart

To run either project, navigate into the respective folder and execute the scripts:

### Power BI Workspace
```bash
cd "Bus Booking Analytics System (PowerBI)"
# Generate raw data
python data_generation/data_generator.py
# Clean and load to MySQL database
python etl_pipeline/etl_pipeline.py --user root --password YOUR_PASSWORD
```

### Tableau Workspace
```bash
cd "Bus Booking Analytics System(Tableau)"
# Generate raw data
python data_generation/data_generator.py
# Clean and load to MySQL database
python etl_pipeline/etl_pipeline.py --user root --password YOUR_PASSWORD
```
