-- Additional Queries for Requirements:

-- 7. Simple SELECT (selecting a subset of columns from one table)
SELECT FullName, Email FROM CustomerProfile;

-- 8. SELECT joining two tables (e.g., CustomerProfile and Order)
SELECT cp.FullName, o.OrderDate, o.LeaseTerm
FROM CustomerProfile cp
JOIN `Order` o ON cp.CustomerID = o.CustomerID;

-- 9. Another SELECT joining two tables (e.g., Order and ApartmentUnit)
SELECT o.OrderID, au.UnitType, au.MonthlyRent
FROM `Order` o
JOIN ApartmentUnit au ON o.UnitID = au.UnitID;

-- 10. SELECT with summary function (e.g., average rent of Apartment Units)
SELECT AVG(MonthlyRent) AS AvgRent
FROM ApartmentUnit;

-- 11. SELECT with summary function (e.g., total number of orders)
SELECT COUNT(*) AS TotalOrders
FROM `Order`;

-- 12. SELECT with summary function (e.g., maximum reliability of suppliers)
SELECT MAX(Reliability) AS MaxReliability
FROM Supplier;

-- 13. Multi-table query (e.g., total rent per customer)
SELECT cp.CustomerID, cp.FullName, SUM(au.MonthlyRent) AS TotalRent
FROM CustomerProfile cp
JOIN `Order` o ON cp.CustomerID = o.CustomerID
JOIN ApartmentUnit au ON o.UnitID = au.UnitID
GROUP BY cp.CustomerID, cp.FullName;

-- 14. INSERT another record with the DEFAULT constraint
INSERT INTO Supplier (SupplierName, ContactInfo, Reliability, LeadTime)
VALUES ('XYZ Supplies', 'contact@xyzsupplies.com', 3.8, 15);

-- 15. Update multiple records (e.g., increase rent for all Apartment Units)
UPDATE ApartmentUnit
SET MonthlyRent = MonthlyRent * 1.05;

-- 16. Delete multiple records (e.g., remove all orders before a certain date)
DELETE FROM `Order`
WHERE OrderDate < '2021-01-01';

-- 17. Complex SELECT with multiple conditions (e.g., find suppliers with high reliability and short lead time)
SELECT SupplierName, Reliability, LeadTime
FROM Supplier
WHERE Reliability > 4 AND LeadTime < 20;

-- 18. SELECT with a subquery (e.g., find customers with above-average rent)
SELECT cp.FullName
FROM CustomerProfile cp
WHERE cp.CustomerID IN (
    SELECT o.CustomerID
    FROM `Order` o
    JOIN ApartmentUnit au ON o.UnitID = au.UnitID
    GROUP BY o.CustomerID
    HAVING AVG(au.MonthlyRent) > (SELECT AVG(MonthlyRent) FROM ApartmentUnit)
);
