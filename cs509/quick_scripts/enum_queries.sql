-- Use the neon_nest_apt database
USE neon_nest_apt;

-- 1. Add a new ENUM column to an existing table (e.g., CustomerProfile)
ALTER TABLE CustomerProfile
ADD MembershipType ENUM('Basic', 'Premium', 'VIP') NOT NULL;

-- 2. Insert a new record with a valid ENUM value
INSERT INTO CustomerProfile (FullName, Email, PhoneNumber, RegistrationDate, Address, PreferredFeatures, MembershipType)
VALUES ('John Doe', 'johndoe@example.com', '123-456-7890', CURDATE(), '1234 Main St', 'Pool, Gym', 'Basic');

-- 3. Update the newly inserted record
UPDATE CustomerProfile
SET Email = 'newemail@example.com', MembershipType = 'Premium'
WHERE FullName = 'John Doe';

-- 4. Delete the new record
DELETE FROM CustomerProfile
WHERE FullName = 'John Doe';

-- 5. Demonstrate AUTO_INCREMENT
-- CustomerID is an AUTO_INCREMENT field
INSERT INTO CustomerProfile (FullName, Email, PhoneNumber, RegistrationDate, Address, PreferredFeatures, MembershipType)
VALUES ('Jane Doe', 'janedoe@example.com', '098-765-4321', CURDATE(), '5678 Main St', 'Balcony', 'VIP');

-- 6. Demonstrate DEFAULT constraint
-- First, add a column with DEFAULT constraint (e.g., in the Supplier table)
ALTER TABLE Supplier
ADD DefaultOrderSize INT DEFAULT 100;

-- Then insert a record without specifying the DefaultOrderSize
INSERT INTO Supplier (SupplierName, ContactInfo, Reliability, LeadTime)
VALUES ('ABC Supplies', 'contact@abcsupplies.com', 4.5, 30);

-- Clean-up: Remove the added columns and records
-- ALTER TABLE CustomerProfile DROP COLUMN MembershipType;
-- ALTER TABLE Supplier DROP COLUMN DefaultOrderSize;
