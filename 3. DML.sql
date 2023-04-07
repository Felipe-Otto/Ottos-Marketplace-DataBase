USE OttosMarketplaceDB

INSERT INTO 
	Customer (FirstName, LastName, CustomerAddress, CustomerEmail, CustomerPhone)
VALUES 
    ('John', 'Doe', '123 Main St', 'john.doe@example.com', '555-123-4567'),
    ('Jane', 'Smith', '456 Park Ave', 'jane.smith@example.com', '555-234-5678'),
    ('Bob', 'Johnson', '789 Broadway', 'bob.johnson@example.com', '555-345-6789'),
    ('Alice', 'Williams', '246 Elm St', 'alice.williams@example.com', '555-456-7890'),
    ('Jack', 'Brown', '135 Pine Ave', 'jack.brown@example.com', '555-567-8901'),
    ('Emily', 'Davis', '579 Oak St', 'emily.davis@example.com', '555-678-9012'),
    ('Michael', 'Wilson', '468 Park Ave', 'michael.wilson@example.com', '555-789-0123'),
    ('Sarah', 'Miller', '246 Elm St', 'sarah.miller@example.com', '555-890-1234'),
    ('David', 'Taylor', '579 Oak St', 'david.taylor@example.com', '555-901-2345'),
    ('Emma', 'Anderson', '468 Park Ave', 'emma.anderson@example.com', '555-012-3456');

INSERT INTO 
	Position (PositionName)
VALUES 
    ('Software Engineer'),
    ('Data Analyst'),
    ('Sales Manager'),
    ('Marketing Coordinator'),
    ('Human Resources Specialist'),
    ('Financial Analyst'),
    ('Product Manager'),
    ('Customer Support Representative'),
    ('IT Administrator'),
    ('Operations Manager');

INSERT INTO 
	Employee (FirstName, LastName, EmployeeAddress, EmployeeEmail, EmployeePhone, PositionKey)
VALUES 
    ('John', 'Doe', '123 Main St', 'john.doe@example.com', '555-123-4567', 1),
    ('Jane', 'Smith', '456 Park Ave', 'jane.smith@example.com', '555-234-5678', 2),
    ('Bob', 'Johnson', '789 Broadway', 'bob.johnson@example.com', '555-345-6789', 3),
    ('Alice', 'Williams', '246 Elm St', 'alice.williams@example.com', '555-456-7890', 4),
    ('Jack', 'Brown', '135 Pine Ave', 'jack.brown@example.com', '555-567-8901', 5),
    ('Emily', 'Davis', '579 Oak St', 'emily.davis@example.com', '555-678-9012', 6),
    ('Michael', 'Wilson', '468 Park Ave', 'michael.wilson@example.com', '555-789-0123', 7),
    ('Sarah', 'Miller', '111 Main St', 'sarah.miller@example.com', '555-890-1234', 8),
    ('David', 'Taylor', '222 Park Ave', 'david.taylor@example.com', '555-901-2345', 9),
    ('Emma', 'Anderson', '333 Oak St', 'emma.anderson@example.com', '555-012-3456', 10);

INSERT INTO 
	Supplier (SupplierName, SupplierAddress, SupplierEmail, SupplierPhone) 
VALUES
	('ABC Corp', '123 Main St', 'abc@abc-incorporated.com', '555-1234'),
	('XYZ Inc', '456 Oak St', 'contact@xyz-corporation.com', '555-5678'),
	('ACME Ltd', '789 Maple Ave', 'info@acme-worldwide.com', '555-9012'),
	('Global Trading Co', '321 Elm St', 'sales@globaltradingco.com', '555-3456'),
	('Pacific Imports', '654 Pine Rd', 'import@pacific-ocean.com', '555-7890'),
	('Mega Corp', '987 Oak Ave', 'contactus@megacorporation.com', '555-2345'),
	('Superior Suppliers', '741 Birch Blvd', 'support@superiorsuppliers.com', '555-6789'),
	('United Exporters', '852 Maple St', 'sales@united-exporters.com', '555-0123'),
	('The Supplier Company', '963 Pine St', 'contact@thesuppliercompany.com', '555-4567'),
	('Global Exports Inc', '369 Elm St', 'sales@global-exports.com', '555-8901');

INSERT INTO 
	ProductCategory (ProductCategoryName, ProductCategoryDescription) 
VALUES
	('Electronics', 'Category for electronic devices and accessories'),
	('Home Appliances', 'Category for home appliances such as refrigerators and washing machines'),
	('Fashion', 'Category for clothing, footwear and accessories'),
	('Toys', 'Category for toys and games'),
	('Books', 'Category for books and magazines'),
	('Sports', 'Category for sports equipment and accessories'),
	('Beauty', 'Category for beauty and personal care products'),
	('Furniture', 'Category for furniture and home decor'),
	('Food and Beverage', 'Category for food and beverage products'),
	('Automotive', 'Category for automotive parts and accessories');

INSERT INTO 
	Product (ProductName, ProductDescription, UnitPrice, StockQuantity, ProductCategoryKey, SupplierKey)
VALUES
	('Smartwatch', 'High-tech smartwatch with multiple features', 199.99, 50, 1, 3),
	('Air Fryer', 'Compact air fryer for healthy cooking', 89.99, 20, 2, 2),
	('Leather Boots', 'Stylish leather boots for men', 129.99, 30, 3, 5),
	('Board Game', 'Strategy board game for 2-4 players', 49.99, 15, 4, 1),
	('Cookbook', 'Collection of recipes from around the world', 24.99, 40, 5, 4),
	('Yoga Mat', 'Eco-friendly yoga mat with non-slip surface', 39.99, 25, 6, 6),
	('Lipstick Set', 'Set of 6 long-lasting lipsticks in different shades', 49.99, 10, 7, 7),
	('Armchair', 'Elegant armchair made of premium materials', 299.99, 5, 8, 9),
	('Organic Coffee', 'Premium organic coffee beans from South America', 14.99, 100, 9, 8),
	('Car Speakers', 'Powerful car speakers for enhanced audio experience', 149.99, 8, 10, 10);

INSERT INTO 
	Store (StoreName, StoreAddress, StorePhone)
VALUES 
	('The Cozy Cottage', '123 Main St, Anytown, USA', '415-555-1234'),
	('Tropical Treasures', '987 Palm St, Island Paradise, USA', '212-555-5678'),
	('The Urban Jungle', '456 Oak St, City Heights, USA', '213-555-8910'),
	('Vintage Vibes', '789 Maple Ave, Old Town, USA', '305-555-2345'),
	('The Book Nook', '234 Elm St, Reading, USA', '206-555-6789'),
	('Sporting Goods Emporium', '456 Pine St, Athleticville, USA', '503-555-3456'),
	('Home Sweet Home Decor', '789 Cherry St, Decor City, USA', '713-555-7890'),
	('The Pet Palace', '345 Cedar St, Purrfectville, USA', '312-555-2345'),
	('The Wine Cellar', '123 Vine St, Grapeville, USA', '617-555-6789'),
	('Electronics Galore', '456 Main St, Techville, USA', '619-555-1234');

INSERT INTO 
	[Order] (OrderDate, OrderStatus, TotalPrice, CustomerKey, StoreKey)
VALUES 
    ('2023-04-01', 'Pending', 50.00, 1, 1),
    ('2023-03-30', 'Processing', 120.00, 2, 2),
    ('2023-04-02', 'Shipped', 75.00, 3, 3),
    ('2023-03-28', 'Delivered', 100.00, 4, 4),
    ('2023-04-03', 'Cancelled', 150.00, 5, 5),
    ('2023-04-05', 'Refunded', 25.00, 6, 6),
    ('2023-03-27', 'On hold', 85.00, 7, 7),
    ('2023-04-06', 'Backordered', 200.00, 8, 8),
    ('2023-04-04', 'Returned', 30.00, 9, 9),
    ('2023-04-07', 'Completed', 175.00, 10, 10),
	('2023-04-07', 'Processing', 450.00, 3, 2),
	('2023-04-06', 'Shipped', 235.00, 5, 1),
	('2023-04-05', 'Delivered', 105.50, 2, 4),
	('2023-04-04', 'Completed', 75.50, 1, 5),
	('2023-04-03', 'Processing', 920.00, 6, 3),
	('2023-04-02', 'Shipped', 315.50, 9, 2),
	('2023-04-01', 'Cancelled', 150.00, 4, 1),
	('2023-03-31', 'Completed', 450.00, 8, 4),
	('2023-03-30', 'Delivered', 500.00, 7, 5),
	('2023-03-29', 'Refunded', 200.00, 10, 3);

INSERT INTO OrderItem (Quantity, UnitPrice, ProductKey, OrderKey)
VALUES
    (2, 25.00, 1, 1),
    (3, 40.00, 2, 2),
    (3, 25.00, 1, 3),
    (2, 50.00, 3, 4),
    (1, 100.00, 4, 5),
	(2, 50.00, 1, 5),
    (1, 25.00, 1, 6),
	(2, 30.00, 5, 7),
	(1, 25.00, 1, 7),
    (2, 100.00, 4, 8),
	(1, 30.00, 5, 9),
	(1, 150.00, 5, 10),
	(1, 25.00, 1, 10),
	(2, 200.00, 6, 11),
	(1, 50.00, 3, 11),
	(1, 200.00, 6, 12),
	(1, 25.00, 1, 12),
	(1, 10.00, 7, 12),
	(1, 100.00, 4, 13),
	(1, 5.50, 8, 13),
	(2, 30.00, 5, 14),
	(1, 10.00, 7, 14),
	(1, 5.50, 8, 14),
	(1, 900.00, 9, 15),
	(2, 10.00, 7, 15),
	(1, 200.00, 6, 16),
	(1, 100.00, 4, 16),
	(1, 10.00, 7, 16),
	(1, 5.50, 8, 16),
	(6, 25.00, 1, 17),
	(2, 225.00, 10, 18),
	(2, 200.00, 6, 19),
	(1, 100.00, 4, 19),
	(1, 200.00, 6, 20);

INSERT INTO 
	Comment (CommentText, CustomerKey, ProductKey)
VALUES
	('I absolutely love this smartwatch! It has so many cool features that make my life easier.', 1, 1),
	('The air fryer works like a charm! It makes cooking healthy meals a breeze.', 2, 2),
	('I bought these leather boots for my husband and he loves them! They are stylish and comfortable.', 3, 3),
	('This board game is so much fun! I play it with my friends all the time.', 4, 4),
	('The cookbook has so many delicious recipes! I can''t wait to try them all.', 5, 5),
	('The yoga mat is great! It provides good support and the non-slip surface is really helpful.', 6, 6),
	('The lipstick set has such pretty shades! I love how long-lasting they are.', 7, 7),
	('The armchair is so elegant and comfortable! It''s the perfect addition to my living room.', 8, 8),
	('The organic coffee is delicious! It has a rich flavor and is very aromatic.', 9, 9),
	('The car speakers are amazing! They provide such clear and powerful sound.', 10, 10);

INSERT INTO 
	ShoppingCart (CustomerKey, ProductKey, Quantity)
VALUES 
	(1, 7, 1),
	(1, 6, 2),
	(1, 4, 1),
	(4, 1, 3),
	(4, 7, 5),
	(10, 10, 2),
	(6, 5, 2),
	(7, 6, 3),
	(8, 9, 2),
	(9, 8, 1),
	(10, 5, 2);