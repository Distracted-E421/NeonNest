NeonNest Apartments

Ethan Epperson-Jones

https://github.com/Distracted-E421/NeonNest.git

SQL ENV = Ubuntu(WSL)

NeonNest Apartments

The only builders of cyberpunk themed apartments solely made from computer parts.

Estimated Company Size

People: 200 employees, including designers, tech specialists, and customer service.

Headquartered in Austin, Texas

**Supply Chain**

**Heat Sinks**

Sources: EVGA, Cooler Master

Usage: Integrated into the apartment's climate control system.

**GPUs (Graphics Processing Units)**

Sources: AMD, Nvidia

Usage: Powers the interactive walls and home theater systems.

**RGB RAM Sticks**

Sources: G.Skill, Corsair

Usage: Used in decorative lighting fixtures and mood lighting.

**Monitors**

Sources: ASUS, LG

Usage: Serve as smart windows and interactive wall displays.

**ATX Power Supplies**

Sources: Seasonic, NZXT

Usage: Converted into home energy storage solutions.

**Water-Cooling Hardline Tubing and Fittings**

Sources: Thermal Lake, EKWB

Usage: Used in the apartment's water supply and also as a decorative element.

**CustomerProfile**

| **Attribute**     | **Data Type** |
|-------------------|---------------|
| FullName          | VarChar(100)  |
| Email             | VarChar(100)  |
| PhoneNumber       | VarChar(20)   |
| RegistrationDate  | Date          |
| Address           | VarChar(255)  |
| PreferredFeatures | VarChar(255)  |

Represents the customers of NeonNest Apartments, tracks the unique identifier of the customer, their full name, contact information, the date they registered with the service, their address, and their preferred features in an apartment.

**ApartmentUnit**

| **Attribute**      | **Data Type** |
|--------------------|---------------|
| UnitType           | VarChar(50)   |
| FloorNumber        | Integer       |
| UnitFeatures       | VarChar(255)  |
| UnitID             | Integer       |
| MonthlyRent        | Decimal(10,2) |
| AvailabilityStatus | Boolean       |

Details an individual apartment unit available for rent. Includes a unique identifier for each unit, the type of unit (e.g., studio, one-bedroom), the floor number, specific features of the unit, the monthly rent cost, and whether the unit is currently available.

**Order**

| **Attribute** | **Data Type** |
|---------------|---------------|
| OrderID       | Integer       |
| CustomerID    | Integer       |
| UnitID        | Integer       |
| OrderDate     | Date          |
| MoveInDate    | Date          |
| LeaseTerm     | Integer       |

Captures information about the leasing orders placed by customers. Includes a unique order identifier, references to the customer and the apartment unit, the date the order was placed, the scheduled move-in date, and the term of the lease.

**SupplyItem**

| **Attribute**     | **Data Type** |
|-------------------|---------------|
| ItemID            | Integer       |
| ItemName          | VarChar(100)  |
| SupplierID        | Integer       |
| QuantityAvaliable | Integer       |
| UnitCost          | Decimal(10,2) |
| UsageDescription  | VarChar(255)  |

Represents the various items that NeonNest Apartments uses in the construction and maintenance of their apartment units. It tracks each item's unique identifier, name, the supplier's identifier, the quantity available for use, the cost per unit, and a description of how the item is used.

**Supplier**

| **Attribute** | **Data Type** |
|---------------|---------------|
| SupplierID    | Integer       |
| SupplierName  | VarChar(100)  |
| ContactInfo   | VarChar(255)  |
| Reliability   | Decimal(3,2)  |
| LeadTime      | Integer       |

Contains information about the suppliers that provide materials to NeonNest Apartments. It includes a unique identifier for each supplier, the supplier's name, their contact information, a reliability rating based on past performance, and the average lead time for orders.

![A screenshot of a computer Description automatically generated](media/74aa390355cf07890b53dd198c540a6a.png)

Crow’s Foot Notation ERD:

CustomerProfile to Order (1..\*):

Each CustomerProfile can be linked to multiple Order records, indicating that a single customer can place several orders. However, each Order is associated with exactly one CustomerProfile. This is a one-to-many relationship.

Order to ApartmentUnit (1..1):

Each Order is linked to exactly one ApartmentUnit, and vice versa. This indicates a one-to-one relationship where each order corresponds to a single apartment unit, ensuring that an order cannot be split across multiple units.

SupplyItem to Supplier (..):

A many-to-many relationship exists between SupplyItem and Supplier. This implies that each SupplyItem can be provided by multiple suppliers, and each Supplier can provide multiple supply items. This relationship often requires an intermediate table or entity to effectively manage the connections between supply items and suppliers.

![A screenshot of a computer program Description automatically generated](media/7c3ac835004f211799f12da1b3e84f01.png)

UML Notation ERD:

CustomerProfile to Order (1..\*):

This UML relationship is similar to the Crow’s Foot version. It shows that a single customer (from CustomerProfile) can have multiple orders (Order), but each order is associated with only one customer. The notation 1..\* near CustomerProfile and 1 near Order clarifies this.

Order to ApartmentUnit (1..1):

The relationship here is again a one-to-one, meaning each Order is for a single ApartmentUnit. The 1..1 notation in UML clearly demonstrates this exclusive pairing.

SupplyItem to Supplier (..):

In the UML version, this many-to-many relationship is indicated by the \* symbol at both ends of the relationship line. It represents that multiple SupplyItem entities can be associated with multiple Supplier entities, necessitating a more complex relationship management, usually via a junction table in database design.

Created Database:

Empty Database:

Populated Database:

Queries

![A screenshot of a computer Description automatically generated](media/388a33bcd5b05de5e3a1c2e359b9949b.png)![A screenshot of a computer Description automatically generated](media/6aaffcdd7e9d1922d04359037ae0446d.png)![A screenshot of a computer Description automatically generated](media/a1855cd0022159f3fffb3847d543a127.png)![A screenshot of a computer Description automatically generated](media/13a713f1fff63de33398dd20d556e842.png)![A screenshot of a computer Description automatically generated](media/db658f230c74d74efa24c7e9c0debdde.png)![A screenshot of a computer program Description automatically generated](media/7c84b7cec358c4520122dc7a2a19e36b.png)![A screenshot of a computer program Description automatically generated](media/6d3af0660407d1e3611d7ca8ee40b763.png)![A screenshot of a computer program Description automatically generated](media/c5ccfdafeb7a4419937e0d4e80714b14.png)
