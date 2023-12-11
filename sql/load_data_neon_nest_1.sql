-- Load data into CustomerProfile table
LOAD DATA LOCAL INFILE '/home/mal/NeonNest/data/csv/CustomerProfile.csv'
INTO TABLE CustomerProfile
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES;

-- Load data into ApartmentUnit table
LOAD DATA LOCAL INFILE '/home/mal/NeonNest/data/csv/ApartmentUnit.csv'
INTO TABLE ApartmentUnit
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES;

-- Load data into Order table
LOAD DATA LOCAL INFILE '/home/mal/NeonNest/data/csv/Order.csv'
INTO TABLE `Order`
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES;

-- Load data into SupplyItem table
LOAD DATA LOCAL INFILE '/home/mal/NeonNest/data/csv/SupplyItem.csv'
INTO TABLE SupplyItem
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES;

-- Load data into Supplier table
LOAD DATA LOCAL INFILE '/home/mal/NeonNest/data/csv/Supplier.csv'
INTO TABLE Supplier
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES;