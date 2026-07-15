import pandas as pd
import random
import os
import datetime

# Set seed for reproducibility
random.seed(42)

def generate_base_buses():
    # 11 Buses (IDs 200 to 210)
    bus_ids = list(range(200, 211))
    bus_types = ["AC Sleeper", "Non-AC Sleeper", "AC Seater"]
    states = ["KA", "MH", "DL", "TS", "AP", "HR", "GJ", "UP"]
    
    buses_data = []
    for b_id in bus_ids:
        state = random.choice(states)
        code1 = f"{random.randint(1, 99):02d}"
        code2 = random.choice(["A", "B", "C", "D", "E", "F", "G", "H", "J", "K"])
        num = f"{random.randint(1000, 9999)}"
        bus_number = f"{state}-{code1}-{code2}-{num}"
        
        bus_type = random.choice(bus_types)
        capacity = 40 if "Sleeper" in bus_type else 50
        
        buses_data.append({
            "Bus_ID": b_id,
            "Bus_Number": bus_number,
            "Bus_Type": bus_type,
            "Capacity": capacity
        })
    return pd.DataFrame(buses_data)

def generate_base_routes():
    # 11 Routes (IDs 300 to 310)
    route_ids = list(range(300, 311))
    predefined_routes = [
        {"Source": "Mumbai", "Destination": "Pune", "Distance": 150},
        {"Source": "Bangalore", "Destination": "Chennai", "Distance": 350},
        {"Source": "Delhi", "Destination": "Jaipur", "Distance": 270},
        {"Source": "Hyderabad", "Destination": "Bangalore", "Distance": 570},
        {"Source": "Chennai", "Destination": "Hyderabad", "Distance": 630},
        {"Source": "Mumbai", "Destination": "Ahmedabad", "Distance": 520},
        {"Source": "Delhi", "Destination": "Chandigarh", "Distance": 250},
        {"Source": "Pune", "Destination": "Goa", "Distance": 450},
        {"Source": "Kolkata", "Destination": "Patna", "Distance": 580},
        {"Source": "Bangalore", "Destination": "Hyderabad", "Distance": 570},
        {"Source": "Delhi", "Destination": "Agra", "Distance": 230}
    ]
    
    city_coords = {
        "Mumbai": (19.0760, 72.8777),
        "Pune": (18.5204, 73.8567),
        "Bangalore": (12.9716, 77.5946),
        "Chennai": (13.0827, 80.2707),
        "Delhi": (28.6139, 77.2090),
        "Jaipur": (26.9124, 75.7873),
        "Hyderabad": (17.3850, 78.4867),
        "Ahmedabad": (23.0225, 72.5714),
        "Chandigarh": (30.7333, 76.7794),
        "Goa": (15.2993, 74.1240),
        "Patna": (25.5941, 85.1376),
        "Kolkata": (22.5726, 88.3639),
        "Agra": (27.1767, 78.0081)
    }
    
    routes_data = []
    for idx, r_id in enumerate(route_ids):
        route_info = predefined_routes[idx]
        
        # Inject mixed-case casing dirt on some routes
        raw_source = route_info["Source"]
        raw_dest = route_info["Destination"]
        
        source = raw_source
        dest = raw_dest
        if idx % 3 == 0:
            # e.g., mUmBaI, pUnE
            source = "".join([c.lower() if i % 2 == 0 else c.upper() for i, c in enumerate(source)])
            dest = "".join([c.lower() if i % 2 == 1 else c.upper() for i, c in enumerate(dest)])
            
        s_lat, s_lon = city_coords[raw_source]
        d_lat, d_lon = city_coords[raw_dest]
            
        routes_data.append({
            "Route_ID": r_id,
            "Source": source,
            "Destination": dest,
            "Distance": route_info["Distance"],
            "Source_Latitude": s_lat,
            "Source_Longitude": s_lon,
            "Dest_Latitude": d_lat,
            "Dest_Longitude": d_lon
        })
    return pd.DataFrame(routes_data)

def generate_base_customers():
    # 301 Customers (IDs 100 to 400)
    customer_ids = list(range(100, 401))
    first_names = [
        "Aarav", "Vihaan", "Vivaan", "Ananya", "Diya", "Saisha", "Arjun", "Sai", "Aditya", 
        "Krishna", "Ishaan", "Shaurya", "Rohit", "Priya", "Neha", "Pooja", "Amit", "Rajesh", 
        "Suresh", "Ramesh", "Sneha", "Riya", "Rahul", "Vikram", "Sandeep", "Deepika", "Kiran", 
        "Sunita", "Kavita", "Anil", "Sanjay", "Meera", "Karan", "Simran", "Rahul", "Neha"
    ]
    last_names = [
        "Sharma", "Verma", "Gupta", "Patel", "Kumar", "Singh", "Joshi", "Mehta", "Rao", 
        "Reddy", "Nair", "Patil", "Kulkarni", "Iyer", "Choudhury", "Das", "Banerjee", 
        "Chatterjee", "Sen", "Mishra", "Pandey", "Yadav", "Prasad", "Bhat", "Gill"
    ]
    
    customers_data = []
    generated_emails = set()
    
    for idx, c_id in enumerate(customer_ids):
        fname = random.choice(first_names)
        lname = random.choice(last_names)
        name = f"{fname} {lname}"
        
        # Inject dirty casing on names
        if idx % 5 == 0:
            name = name.lower()
        elif idx % 5 == 1:
            name = name.upper()
        elif idx % 5 == 2:
            # mixed case like aArAv sHaRmA
            name = "".join([c.lower() if i % 2 == 0 else c.upper() for i, c in enumerate(name)])
            
        email_base = f"{fname.lower()}.{lname.lower()}"
        email = f"{email_base}@email.com"
        counter = 1
        while email in generated_emails:
            email = f"{email_base}{counter}@email.com"
            counter += 1
        generated_emails.add(email)
        
        # Inconsistent phone number format and some missing
        if idx % 15 == 0:
            phone = None
        else:
            phone_prefix = random.choice(['7', '8', '9'])
            phone = phone_prefix + "".join(random.choices("0123456789", k=9))
            
        # Generate Gender with dirty casing and abbreviations
        gender = random.choice(["Male", "Female"])
        if idx % 12 == 0:
            gender = gender.lower()
        elif idx % 12 == 1:
            gender = gender.upper()
        elif idx % 12 == 2:
            gender = gender[0]  # 'M' or 'F'
        elif idx % 25 == 0:
            gender = None  # Missing
            
        # Generate Age with outliers and nulls
        age = random.randint(18, 75)
        if idx % 20 == 0:
            age = None  # Missing
        elif idx % 20 == 1:
            age = random.randint(-15, -1)  # Negative age anomaly
        elif idx % 20 == 2:
            age = random.randint(110, 150)  # Outlier age anomaly
            
        customers_data.append({
            "Customer_ID": c_id,
            "Name": name,
            "Email": email,
            "Phone": phone,
            "Gender": gender,
            "Age": age
        })
    return pd.DataFrame(customers_data)

def generate_dirty_bookings(customers_df, buses_df, routes_df, num_records=2000):
    cust_ids = customers_df["Customer_ID"].tolist()
    bus_ids = buses_df["Bus_ID"].tolist()
    route_ids = routes_df["Route_ID"].tolist()
    
    statuses = ["Confirmed", "Pending", "Cancelled"]
    bookings_data = []
    
    # Skew customer bookings to achieve a Customer Retention Rate (~73%, slightly below the 76% goal)
    # 27% of customers book exactly once (single-trip travelers)
    # 73% of customers book repeatedly (frequent flyers)
    num_customers = len(cust_ids)
    single_trip_count = int(num_customers * 0.27) # ~81 customers
    
    single_trip_custs = cust_ids[:single_trip_count]
    frequent_custs = cust_ids[single_trip_count:]
    
    single_trip_pool = list(single_trip_custs)
    random.shuffle(single_trip_pool)
    
    # We want to span from 2025-01-01 to 2026-07-14 (present month/date)
    start_date = datetime.date(2025, 1, 1)
    end_date = datetime.date(2026, 7, 14)
    total_days = (end_date - start_date).days + 1
    
    b_id = 1
    
    # Generate scheduled runs across the timeline
    for d in range(total_days):
        current_date = start_date + datetime.timedelta(days=d)
        
        # Schedule 1 run per day on average to keep data size around 15k-20k
        # Choose a random Route and Bus for this day's run
        bus_id = random.choice(bus_ids)
        route_id = random.choice(route_ids)
        
        bus_cap = buses_df[buses_df["Bus_ID"] == bus_id]["Capacity"].values[0]
        dist = routes_df[routes_df["Route_ID"] == route_id]["Distance"].values[0]
        bus_type = buses_df[buses_df["Bus_ID"] == bus_id]["Bus_Type"].values[0]
        
        # Target high occupancy rate: 70% to 90% (practically realistic)
        occupancy_rate = random.uniform(0.70, 0.90)
        num_seats_to_book = int(bus_cap * occupancy_rate)
        
        # Select unique seat numbers for this run
        all_seats = list(range(1, bus_cap + 1))
        booked_seats = random.sample(all_seats, k=num_seats_to_book)
        
        # Generate bookings for this run
        for seat_num in booked_seats:
            if single_trip_pool and random.random() < 0.05:
                cust_id = single_trip_pool.pop()
            else:
                cust_id = random.choice(frequent_custs)
            
            # Booking Date is 0 to 14 days before Travel Date (lead time)
            # Use a weighted distribution for lead time (mostly 1-5 days)
            lead_time = random.choice([0, 1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 6, 7, 10, 14])
            booking_date = current_date - datetime.timedelta(days=lead_time)
            
            # Prevent booking date from going before Jan 1, 2025
            if booking_date < start_date:
                booking_date = start_date
                
            # Base fare rate based on bus type
            base_rate = 1.5 if "AC" in bus_type else 1.0
            fare = float(dist * base_rate + (200 if "Sleeper" in bus_type else 50))
            
            # Inject pricing seasonality to make the revenue trend line unique from bookings line!
            # Weekend surcharge (Friday, Saturday, Sunday)
            if current_date.weekday() >= 4:
                fare *= 1.15
            # Summer peak (May & June)
            if current_date.month in [5, 6]:
                fare *= 1.20
            # Festive season peak (October & November)
            elif current_date.month in [10, 11]:
                fare *= 0.85 if current_date.month == 11 else 1.25 # minor dip in late nov, peak oct
                
            # Add minor random price fluctuations
            fare += random.uniform(-15.0, 15.0)
            fare = round(fare, 2)
            
            # Dynamic status distribution: Confirmed is majority (82%), Cancelled (12%), Pending (6%)
            status = random.choices(statuses, weights=[0.82, 0.12, 0.06])[0]
            
            bookings_data.append({
                "Booking_ID": b_id,
                "Customer_ID": cust_id,
                "Bus_ID": bus_id,
                "Route_ID": route_id,
                "Booking_Date": booking_date.strftime('%Y-%m-%d'),
                "Travel_Date": current_date.strftime('%Y-%m-%d'),
                "Seat_Number": seat_num,
                "Fare_Amount": fare,
                "Booking_Status": status
            })
            b_id += 1
            
    df = pd.DataFrame(bookings_data)
    num_records = len(df)
    
    # --- Inject Dirt ---
    # 1. Duplicate records (5% duplicates)
    dup_indices = random.sample(range(num_records), k=int(num_records * 0.05))
    duplicates = df.iloc[dup_indices].copy()
    # Shift Booking_ID slightly or keep same to test PK deduplication
    # Let's keep exact duplicates to test deduplication
    df = pd.concat([df, duplicates], ignore_index=True)
    
    # 2. Missing Fare (2% nulls)
    null_fare_indices = random.sample(range(len(df)), k=int(len(df) * 0.02))
    df.loc[null_fare_indices, "Fare_Amount"] = None
    
    # 3. Negative Fare (1.5% negative fares)
    neg_fare_indices = random.sample(range(len(df)), k=int(len(df) * 0.015))
    df.loc[neg_fare_indices, "Fare_Amount"] = -250.0
    
    # 4. Invalid Travel Dates (1.5% where Travel_Date < Booking_Date)
    invalid_date_indices = random.sample(range(len(df)), k=int(len(df) * 0.015))
    for idx in invalid_date_indices:
        b_date = pd.to_datetime(df.loc[idx, "Booking_Date"])
        t_date = b_date - datetime.timedelta(days=random.randint(1, 4))
        df.loc[idx, "Travel_Date"] = t_date.strftime('%Y-%m-%d')
        
    # 5. Inconsistent Date Formats (5% mixed formats like DD/MM/YYYY or MM-DD-YYYY)
    date_format_indices = random.sample(range(len(df)), k=int(len(df) * 0.05))
    for idx in date_format_indices:
        b_dt = pd.to_datetime(df.loc[idx, "Booking_Date"])
        t_dt = pd.to_datetime(df.loc[idx, "Travel_Date"])
        if random.choice([True, False]):
            # DD/MM/YYYY
            df.loc[idx, "Booking_Date"] = b_dt.strftime('%d/%m/%Y')
            df.loc[idx, "Travel_Date"] = t_dt.strftime('%d/%m/%Y')
        else:
            # MM-DD-YYYY
            df.loc[idx, "Booking_Date"] = b_dt.strftime('%m-%d-%Y')
            df.loc[idx, "Travel_Date"] = t_dt.strftime('%m-%d-%Y')
            
    # 6. Over-capacity Seat Number (1% of records)
    over_capacity_indices = random.sample(range(len(df)), k=int(len(df) * 0.01))
    for idx in over_capacity_indices:
        bus_id = df.loc[idx, "Bus_ID"]
        bus_cap = buses_df[buses_df["Bus_ID"] == bus_id]["Capacity"].values[0]
        df.loc[idx, "Seat_Number"] = bus_cap + random.randint(1, 10)
        
    # 7. Inconsistent Status Casing (5% of records)
    status_casing_indices = random.sample(range(len(df)), k=int(len(df) * 0.05))
    for idx in status_casing_indices:
        status = df.loc[idx, "Booking_Status"]
        if random.choice([True, False]):
            df.loc[idx, "Booking_Status"] = status.lower()
        else:
            df.loc[idx, "Booking_Status"] = "".join([c.lower() if i % 2 == 0 else c.upper() for i, c in enumerate(status)])
            
    # Shuffle dataset
    df = df.sample(frac=1, random_state=42).reset_index(drop=True)
    return df

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_dir = os.path.join(base_dir, 'data')
    os.makedirs(data_dir, exist_ok=True)
    
    print("Generating base entities...")
    buses_df = generate_base_buses()
    routes_df = generate_base_routes()
    customers_df = generate_base_customers()
    
    print("Generating raw bookings with injected dirt (>1000 rows)...")
    bookings_df = generate_dirty_bookings(customers_df, buses_df, routes_df, num_records=2000)
    
    # Save raw datasets
    bookings_df.to_csv(os.path.join(data_dir, 'bus_booking_raw.csv'), index=False)
    customers_df.to_csv(os.path.join(data_dir, 'customers.csv'), index=False)
    buses_df.to_csv(os.path.join(data_dir, 'buses.csv'), index=False)
    routes_df.to_csv(os.path.join(data_dir, 'routes.csv'), index=False)
    
    print(f"Generated Raw Bookings: {len(bookings_df)} rows. Saved to data/bus_booking_raw.csv")
    print(f"Generated Customers: {len(customers_df)} rows. Saved to data/customers.csv")
    print(f"Generated Buses: {len(buses_df)} rows. Saved to data/buses.csv")
    print(f"Generated Routes: {len(routes_df)} rows. Saved to data/routes.csv")

if __name__ == "__main__":
    main()
