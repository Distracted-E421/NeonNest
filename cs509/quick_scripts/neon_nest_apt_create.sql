-- Create neon_nest_apt database
CREATE DATABASE neon_nest_apt;

-- Use neon_nest_apt database
USE neon_nest_apt;

-- Table for CustomerProfile
CREATE TABLE CustomerProfile (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY,
    FullName VARCHAR(100),
    Email VARCHAR(100),
    PhoneNumber VARCHAR(20),
    RegistrationDate DATE,
    Address VARCHAR(255),
    PreferredFeatures VARCHAR(255)
);

-- Table for ApartmentUnit
CREATE TABLE ApartmentUnit (
    UnitID INT AUTO_INCREMENT PRIMARY KEY,
    UnitType VARCHAR(50),
    FloorNumber INT,
    UnitFeatures VARCHAR(255),
    MonthlyRent DECIMAL(10, 2),
    AvailabilityStatus BOOLEAN
);

-- Table for Order
CREATE TABLE `Order` (
    OrderID INT AUTO_INCREMENT PRIMARY KEY,
    CustomerID INT,
    UnitID INT,
    OrderDate DATE,
    MoveInDate DATE,
    LeaseTerm INT,
    FOREIGN KEY (CustomerID) REFERENCES CustomerProfile(CustomerID),
    FOREIGN KEY (UnitID) REFERENCES ApartmentUnit(UnitID)
);

-- Table for SupplyItem
CREATE TABLE SupplyItem (
    ItemID INT AUTO_INCREMENT PRIMARY KEY,
    ItemName VARCHAR(100),
    SupplierID INT,
    QuantityAvailable INT,
    UnitCost DECIMAL(10, 2),
    UsageDescription VARCHAR(255)
);

-- Table for Supplier
CREATE TABLE Supplier (
    SupplierID INT AUTO_INCREMENT PRIMARY KEY,
    SupplierName VARCHAR(100),
    ContactInfo VARCHAR(255),
    Reliability DECIMAL(3, 2),
    LeadTime INT
);
