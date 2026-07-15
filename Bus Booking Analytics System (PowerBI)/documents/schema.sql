-- Bus Booking Analytics System - Database Schema (DDL)
-- Target Database: MySQL

CREATE DATABASE IF NOT EXISTS bus_booking_analytics;
USE bus_booking_analytics;

-- 1. Customers Dimension Table
CREATE TABLE IF NOT EXISTS Customers (
    Customer_ID INT PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    Email VARCHAR(255) NOT NULL UNIQUE,
    Phone VARCHAR(20) NOT NULL,
    Gender VARCHAR(10) NOT NULL,
    Age INT NOT NULL
);

-- 2. Buses Dimension Table
CREATE TABLE IF NOT EXISTS Buses (
    Bus_ID INT PRIMARY KEY,
    Bus_Number VARCHAR(20) NOT NULL UNIQUE,
    Bus_Type VARCHAR(50) NOT NULL,
    Capacity INT NOT NULL
);

-- 3. Routes Dimension Table
CREATE TABLE IF NOT EXISTS Routes (
    Route_ID INT PRIMARY KEY,
    Source VARCHAR(100) NOT NULL,
    Destination VARCHAR(100) NOT NULL,
    Distance INT NOT NULL,
    Source_Latitude DECIMAL(9, 6),
    Source_Longitude DECIMAL(9, 6),
    Dest_Latitude DECIMAL(9, 6),
    Dest_Longitude DECIMAL(9, 6)
);

-- 4. Bookings Fact Table
CREATE TABLE IF NOT EXISTS Bookings (
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
