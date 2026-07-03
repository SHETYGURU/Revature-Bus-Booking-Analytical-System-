import pandas as pd
import sqlite3
import os
import mysql.connector
from mysql.connector import Error

def load_csv_data(data_dir):
    print("Loading CSV files...")
    # Load raw bookings if exists, otherwise fall back to 1000 rows
    raw_bookings_path = os.path.join(data_dir, 'bus_booking_raw.csv')
    if os.path.exists(raw_bookings_path):
        print(f"Loading raw bookings from {raw_bookings_path}")
        bookings = pd.read_csv(raw_bookings_path)
    else:
        print("Raw bookings not found, falling back to 1000 rows.")
        bookings = pd.read_csv(os.path.join(data_dir, 'bus_booking_1000_rows.csv'))
        
    customers = pd.read_csv(os.path.join(data_dir, 'customers.csv'))
    buses = pd.read_csv(os.path.join(data_dir, 'buses.csv'))
    routes = pd.read_csv(os.path.join(data_dir, 'routes.csv'))
    return bookings, customers, buses, routes

def transform_and_validate(bookings, customers, buses, routes):
    print("--- ETL CLEANING & TRANSFORMATION REPORT ---")
    initial_bookings_count = len(bookings)
    initial_customers_count = len(customers)
    
    # --- 1. Date Format Standardization ---
    # Parse dates flexibly. Since formats can be mixed (YYYY-MM-DD, DD/MM/YYYY, MM-DD-YYYY),
    # we convert them to datetime objects, coercing invalid inputs to NaT.
    bookings['Booking_Date'] = pd.to_datetime(bookings['Booking_Date'], format='mixed', errors='coerce')
    bookings['Travel_Date'] = pd.to_datetime(bookings['Travel_Date'], format='mixed', errors='coerce')
    
    invalid_dates_parsing = bookings['Booking_Date'].isna() | bookings['Travel_Date'].isna()
    invalid_parsing_count = invalid_dates_parsing.sum()
    if invalid_parsing_count > 0:
        print(f"[Warning] Date Parsing: Found {invalid_parsing_count} rows with unparseable dates. Removing them.")
        bookings = bookings[~invalid_dates_parsing]
        
    # --- 2. Duplicate Removal ---
    # Deduplicate Bookings based on Booking_ID
    duplicates_count = bookings.duplicated(subset=['Booking_ID']).sum()
    bookings_clean = bookings.drop_duplicates(subset=['Booking_ID']).copy()
    print(f"Deduplication: Removed {duplicates_count} duplicate booking records.")
    
    # --- 3. Handling Null Values ---
    # Drop records from Bookings where Fare_Amount is null
    null_fares_count = bookings_clean['Fare_Amount'].isnull().sum()
    bookings_clean = bookings_clean.dropna(subset=['Fare_Amount'])
    print(f"Null Handling: Removed {null_fares_count} booking records with missing Fare_Amount.")
    
    # Fill missing phone numbers in Customers with "Unknown"
    customers_clean = customers.copy()
    null_phones_count = customers_clean['Phone'].isnull().sum()
    customers_clean['Phone'] = customers_clean['Phone'].fillna('Unknown')
    print(f"Null Handling: Filled {null_phones_count} missing customer phone numbers with 'Unknown'.")
    
    # --- 4. Data Standardization ---
    # Convert dates to standard YYYY-MM-DD string format
    bookings_clean['Booking_Date'] = bookings_clean['Booking_Date'].dt.strftime('%Y-%m-%d')
    bookings_clean['Travel_Date'] = bookings_clean['Travel_Date'].dt.strftime('%Y-%m-%d')
    
    # Title casing for customer names
    customers_clean['Name'] = customers_clean['Name'].str.title()
    
    # Title casing for Route sources and destinations
    routes_clean = routes.copy()
    routes_clean['Source'] = routes_clean['Source'].str.title()
    routes_clean['Destination'] = routes_clean['Destination'].str.title()
    
    # Capitalize booking status (Confirmed, Pending, Cancelled)
    bookings_clean['Booking_Status'] = bookings_clean['Booking_Status'].str.capitalize()
    
    # --- 5. Data Consistency Checks ---
    # Travel_Date >= Booking_Date
    date_check_mask = pd.to_datetime(bookings_clean['Travel_Date']) >= pd.to_datetime(bookings_clean['Booking_Date'])
    invalid_travel_dates_count = (~date_check_mask).sum()
    if invalid_travel_dates_count > 0:
        print(f"Constraint Check: Removed {invalid_travel_dates_count} bookings where Travel_Date was before Booking_Date.")
        bookings_clean = bookings_clean[date_check_mask]
        
    # Fare_Amount > 0
    fare_check_mask = bookings_clean['Fare_Amount'] > 0
    invalid_fares_count = (~fare_check_mask).sum()
    if invalid_fares_count > 0:
        print(f"Constraint Check: Removed {invalid_fares_count} bookings with non-positive Fare_Amount (e.g. negative values).")
        bookings_clean = bookings_clean[fare_check_mask]
        
    # Referential Integrity Checks
    # Remove bookings with invalid Customer_ID
    invalid_custs_mask = ~bookings_clean['Customer_ID'].isin(customers_clean['Customer_ID'])
    invalid_custs_count = invalid_custs_mask.sum()
    if invalid_custs_count > 0:
        print(f"Referential Integrity: Removed {invalid_custs_count} bookings mapping to non-existent Customer_IDs.")
        bookings_clean = bookings_clean[~invalid_custs_mask]
        
    # Remove bookings with invalid Bus_ID
    invalid_buses_mask = ~bookings_clean['Bus_ID'].isin(buses['Bus_ID'])
    invalid_buses_count = invalid_buses_mask.sum()
    if invalid_buses_count > 0:
        print(f"Referential Integrity: Removed {invalid_buses_count} bookings mapping to non-existent Bus_IDs.")
        bookings_clean = bookings_clean[~invalid_buses_mask]
        
    # Remove bookings with invalid Route_ID
    invalid_routes_mask = ~bookings_clean['Route_ID'].isin(routes_clean['Route_ID'])
    invalid_routes_count = invalid_routes_mask.sum()
    if invalid_routes_count > 0:
        print(f"Referential Integrity: Removed {invalid_routes_count} bookings mapping to non-existent Route_IDs.")
        bookings_clean = bookings_clean[~invalid_routes_mask]
        
    # Bus Capacity Check (make sure Seat_Number does not exceed Capacity)
    merged_seats = bookings_clean.merge(buses, on='Bus_ID', how='left')
    over_capacity_mask = merged_seats['Seat_Number'] > merged_seats['Capacity']
    over_capacity_count = over_capacity_mask.sum()
    if over_capacity_count > 0:
        over_capacity_ids = merged_seats.loc[over_capacity_mask, 'Booking_ID']
        print(f"Capacity Check: Removed {over_capacity_count} bookings where Seat_Number exceeded Bus Capacity.")
        bookings_clean = bookings_clean[~bookings_clean['Booking_ID'].isin(over_capacity_ids)]
        
    final_bookings_count = len(bookings_clean)
    final_customers_count = len(customers_clean)
    
    print("\n--- SUMMARY OF PROCESS ---")
    print(f"Bookings: {initial_bookings_count} raw rows -> {final_bookings_count} clean rows (Removed {initial_bookings_count - final_bookings_count} rows).")
    print(f"Customers: {initial_customers_count} raw rows -> {final_customers_count} clean rows.")
    print("--------------------------------------------")
    
    return bookings_clean, customers_clean, buses, routes_clean

def load_to_sqlite(bookings, customers, buses, routes, db_path):
    print(f"Loading data into SQLite database: {db_path}...")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Enable foreign keys
    cursor.execute("PRAGMA foreign_keys = ON;")
    
    # Drop tables to recreate them freshly
    cursor.execute("DROP TABLE IF EXISTS Bookings;")
    cursor.execute("DROP TABLE IF EXISTS Customers;")
    cursor.execute("DROP TABLE IF EXISTS Buses;")
    cursor.execute("DROP TABLE IF EXISTS Routes;")
    
    # Create tables
    cursor.execute("""
    CREATE TABLE Customers (
        Customer_ID INTEGER PRIMARY KEY,
        Name TEXT NOT NULL,
        Email TEXT NOT NULL UNIQUE,
        Phone TEXT NOT NULL
    );
    """)
    
    cursor.execute("""
    CREATE TABLE Buses (
        Bus_ID INTEGER PRIMARY KEY,
        Bus_Number TEXT NOT NULL UNIQUE,
        Bus_Type TEXT NOT NULL,
        Capacity INTEGER NOT NULL
    );
    """)
    
    cursor.execute("""
    CREATE TABLE Routes (
        Route_ID INTEGER PRIMARY KEY,
        Source TEXT NOT NULL,
        Destination TEXT NOT NULL,
        Distance INTEGER NOT NULL
    );
    """)
    
    cursor.execute("""
    CREATE TABLE Bookings (
        Booking_ID INTEGER PRIMARY KEY,
        Customer_ID INTEGER NOT NULL,
        Bus_ID INTEGER NOT NULL,
        Route_ID INTEGER NOT NULL,
        Booking_Date TEXT NOT NULL,
        Travel_Date TEXT NOT NULL,
        Seat_Number INTEGER NOT NULL,
        Fare_Amount REAL NOT NULL,
        Booking_Status TEXT NOT NULL,
        FOREIGN KEY (Customer_ID) REFERENCES Customers(Customer_ID),
        FOREIGN KEY (Bus_ID) REFERENCES Buses(Bus_ID),
        FOREIGN KEY (Route_ID) REFERENCES Routes(Route_ID)
    );
    """)
    
    # Insert clean data
    customers.to_sql('Customers', conn, if_exists='append', index=False)
    buses.to_sql('Buses', conn, if_exists='append', index=False)
    routes.to_sql('Routes', conn, if_exists='append', index=False)
    bookings.to_sql('Bookings', conn, if_exists='append', index=False)
    
    conn.commit()
    conn.close()
    print("Successfully loaded datasets into SQLite database.")

def load_to_mysql(bookings, customers, buses, routes, db_config):
    print("Connecting to MySQL...")
    try:
        conn = mysql.connector.connect(**db_config)
        if conn.is_connected():
            cursor = conn.cursor()
            
            db_name = db_config.get('database', 'bus_booking_analytics')
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
            cursor.execute(f"USE {db_name}")
            
            cursor.execute("DROP TABLE IF EXISTS Bookings;")
            cursor.execute("DROP TABLE IF EXISTS Customers;")
            cursor.execute("DROP TABLE IF EXISTS Buses;")
            cursor.execute("DROP TABLE IF EXISTS Routes;")
            
            cursor.execute("""
            CREATE TABLE Customers (
                Customer_ID INT PRIMARY KEY,
                Name VARCHAR(255) NOT NULL,
                Email VARCHAR(255) NOT NULL UNIQUE,
                Phone VARCHAR(20) NOT NULL
            );
            """)
            
            cursor.execute("""
            CREATE TABLE Buses (
                Bus_ID INT PRIMARY KEY,
                Bus_Number VARCHAR(20) NOT NULL UNIQUE,
                Bus_Type VARCHAR(50) NOT NULL,
                Capacity INT NOT NULL
            );
            """)
            
            cursor.execute("""
            CREATE TABLE Routes (
                Route_ID INT PRIMARY KEY,
                Source VARCHAR(100) NOT NULL,
                Destination VARCHAR(100) NOT NULL,
                Distance INT NOT NULL
            );
            """)
            
            cursor.execute("""
            CREATE TABLE Bookings (
                Booking_ID INT PRIMARY KEY,
                Customer_ID INT NOT NULL,
                Bus_ID INT NOT NULL,
                Route_ID INT NOT NULL,
                Booking_Date DATE NOT NULL,
                Travel_Date DATE NOT NULL,
                Seat_Number INT NOT NULL,
                Fare_Amount DECIMAL(10, 2) NOT NULL,
                Booking_Status VARCHAR(20) NOT NULL,
                FOREIGN KEY (Customer_ID) REFERENCES Customers(Customer_ID),
                FOREIGN KEY (Bus_ID) REFERENCES Buses(Bus_ID),
                FOREIGN KEY (Route_ID) REFERENCES Routes(Route_ID)
            );
            """)
            
            # Insert Customers
            cust_tuples = [tuple(x) for x in customers.to_numpy()]
            cursor.executemany("INSERT INTO Customers (Customer_ID, Name, Email, Phone) VALUES (%s, %s, %s, %s)", cust_tuples)
            
            # Insert Buses
            bus_tuples = [tuple(x) for x in buses.to_numpy()]
            cursor.executemany("INSERT INTO Buses (Bus_ID, Bus_Number, Bus_Type, Capacity) VALUES (%s, %s, %s, %s)", bus_tuples)
            
            # Insert Routes
            route_tuples = [tuple(x) for x in routes.to_numpy()]
            cursor.executemany("INSERT INTO Routes (Route_ID, Source, Destination, Distance) VALUES (%s, %s, %s, %s)", route_tuples)
            
            # Insert Bookings
            booking_tuples = [tuple(x) for x in bookings.to_numpy()]
            cursor.executemany("""
                INSERT INTO Bookings (Booking_ID, Customer_ID, Bus_ID, Route_ID, Booking_Date, Travel_Date, Seat_Number, Fare_Amount, Booking_Status)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, booking_tuples)
            
            conn.commit()
            print("Successfully loaded datasets into MySQL database.")
            
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        print("Falling back... Configure your connection details in MySQL configuration to execute directly.")
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_dir = os.path.join(base_dir, 'data')
    
    if not os.path.exists(data_dir):
        data_dir = 'data'
        
    bookings, customers, buses, routes = load_csv_data(data_dir)
    bookings_c, customers_c, buses_c, routes_c = transform_and_validate(bookings, customers, buses, routes)
    
    # Save cleaned files
    clean_dir = os.path.join(data_dir, 'clean')
    os.makedirs(clean_dir, exist_ok=True)
    bookings_c.to_csv(os.path.join(clean_dir, 'bookings_clean.csv'), index=False)
    customers_c.to_csv(os.path.join(clean_dir, 'customers_clean.csv'), index=False)
    buses_c.to_csv(os.path.join(clean_dir, 'buses_clean.csv'), index=False)
    routes_c.to_csv(os.path.join(clean_dir, 'routes_clean.csv'), index=False)
    print(f"Cleaned CSVs saved to {clean_dir}")
    
    # Load into local SQLite database
    db_path = os.path.join(data_dir, 'bus_booking_analytics.db')
    load_to_sqlite(bookings_c, customers_c, buses_c, routes_c, db_path)

if __name__ == "__main__":
    main()
