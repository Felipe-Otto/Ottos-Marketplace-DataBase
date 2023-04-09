USE OttosMarketplaceDB

INSERT INTO 
	Customer (CustomerKey, FirstName, LastName, CustomerAddress, CustomerEmail, CustomerPhone)
VALUES 
  (1, 'John', 'Doe', '123 Main St', 'john.doe@example.com', '555-123-4567'),
  (2, 'Jane', 'Smith', '456 Park Ave', 'jane.smith@example.com', '555-234-5678'),
  (3, 'Bob', 'Johnson', '789 Broadway', 'bob.johnson@example.com', '555-345-6789'),
  (4, 'Alice', 'Williams', '246 Elm St', 'alice.williams@example.com', '555-456-7890'),
  (5, 'Jack', 'Brown', '135 Pine Ave', 'jack.brown@example.com', '555-567-8901'),
  (6, 'Emily', 'Davis', '579 Oak St', 'emily.davis@example.com', '555-678-9012'),
  (7, 'Michael', 'Wilson', '468 Park Ave', 'michael.wilson@example.com', '555-789-0123'),
  (8, 'Sarah', 'Miller', '246 Elm St', 'sarah.miller@example.com', '555-890-1234'),
  (9, 'David', 'Taylor', '579 Oak St', 'david.taylor@example.com', '555-901-2345'),
  (10, 'Emma', 'Anderson', '468 Park Ave', 'emma.anderson@example.com', '555-012-3456');

INSERT INTO 
	Position (PositionKey, PositionName)
VALUES 
  (1, 'Software Engineer'),
  (2, 'Data Analyst'),
  (3, 'Sales Manager'),
  (4, 'Marketing Coordinator'),
  (5, 'Human Resources Specialist'),
  (6, 'Financial Analyst'),
  (7, 'Product Manager'),
  (8, 'Customer Support Representative'),
  (9, 'IT Administrator'),
  (10, 'Operations Manager');

INSERT INTO 
	Employee (EmployeeKey, FirstName, LastName, EmployeeAddress, EmployeeEmail, EmployeePhone, PositionKey)
VALUES 
  (1, 'John', 'Doe', '123 Main St', 'john.doe@example.com', '555-123-4567', 1),
  (2, 'Jane', 'Smith', '456 Park Ave', 'jane.smith@example.com', '555-234-5678', 2),
  (3, 'Bob', 'Johnson', '789 Broadway', 'bob.johnson@example.com', '555-345-6789', 3),
  (4, 'Alice', 'Williams', '246 Elm St', 'alice.williams@example.com', '555-456-7890', 4),
  (5, 'Jack', 'Brown', '135 Pine Ave', 'jack.brown@example.com', '555-567-8901', 5),
  (6, 'Emily', 'Davis', '579 Oak St', 'emily.davis@example.com', '555-678-9012', 6),
  (7, 'Michael', 'Wilson', '468 Park Ave', 'michael.wilson@example.com', '555-789-0123', 7),
  (8, 'Sarah', 'Miller', '111 Main St', 'sarah.miller@example.com', '555-890-1234', 8),
  (9, 'David', 'Taylor', '222 Park Ave', 'david.taylor@example.com', '555-901-2345', 9),
  (10, 'Emma', 'Anderson', '333 Oak St', 'emma.anderson@example.com', '555-012-3456', 10);

INSERT INTO 
	Supplier (SupplierKey, SupplierName, SupplierAddress, SupplierEmail, SupplierPhone) 
VALUES
	(1, 'ABC Corp', '123 Main St', 'abc@abc-incorporated.com', '555-1234'),
	(2, 'XYZ Inc', '456 Oak St', 'contact@xyz-corporation.com', '555-5678'),
	(3, 'ACME Ltd', '789 Maple Ave', 'info@acme-worldwide.com', '555-9012'),
	(4, 'Global Trading Co', '321 Elm St', 'sales@globaltradingco.com', '555-3456'),
	(5, 'Pacific Imports', '654 Pine Rd', 'import@pacific-ocean.com', '555-7890'),
	(6, 'Mega Corp', '987 Oak Ave', 'contactus@megacorporation.com', '555-2345'),
	(7, 'Superior Suppliers', '741 Birch Blvd', 'support@superiorsuppliers.com', '555-6789'),
	(8, 'United Exporters', '852 Maple St', 'sales@united-exporters.com', '555-0123'),
	(9, 'The Supplier Company', '963 Pine St', 'contact@thesuppliercompany.com', '555-4567'),
	(10, 'Global Exports Inc', '369 Elm St', 'sales@global-exports.com', '555-8901');

INSERT INTO 
	ProductCategory (ProductCategoryKey, ProductCategoryName, ProductCategoryDescription) 
VALUES
	(1, 'Electronics', 'Category for electronic devices and accessories'),
	(2, 'Home Appliances', 'Category for home appliances such as refrigerators and washing machines'),
	(3, 'Fashion', 'Category for clothing, footwear and accessories'),
	(4, 'Toys', 'Category for toys and games'),
	(5, 'Books', 'Category for books and magazines'),
	(6, 'Sports', 'Category for sports equipment and accessories'),
	(7, 'Beauty', 'Category for beauty and personal care products'),
	(8, 'Furniture', 'Category for furniture and home decor'),
	(9, 'Food and Beverage', 'Category for food and beverage products'),
	(10, 'Automotive', 'Category for automotive parts and accessories');
	
INSERT INTO 
	Product (ProductKey, ProductName, ProductDescription, UnitPrice, StockQuantity, ProductCategoryKey, SupplierKey)
VALUES
	(1, 'Smartwatch', 'High-tech smartwatch with multiple features', 199.99, 50, 1, 3),
	(2, 'Air Fryer', 'Compact air fryer for healthy cooking', 89.99, 20, 2, 2),
	(3, 'Leather Boots', 'Stylish leather boots for men', 129.99, 30, 3, 5),
	(4, 'Board Game', 'Strategy board game for 2-4 players', 49.99, 15, 4, 1),
	(5, 'Cookbook', 'Collection of recipes from around the world', 24.99, 40, 5, 4),
	(6, 'Yoga Mat', 'Eco-friendly yoga mat with non-slip surface', 39.99, 25, 6, 6),
	(7, 'Lipstick Set', 'Set of 6 long-lasting lipsticks in different shades', 49.99, 10, 7, 7),
	(8, 'Armchair', 'Elegant armchair made of premium materials', 299.99, 5, 8, 9),
	(9, 'Organic Coffee', 'Premium organic coffee beans from South America', 14.99, 100, 9, 8),
	(10, 'Car Speakers', 'Powerful car speakers for enhanced audio experience', 149.99, 8, 10, 10);

INSERT INTO 
	Store (StoreKey, StoreName, StoreAddress, StorePhone)
VALUES 
	(1, 'The Cozy Cottage', '123 Main St, Anytown, USA', '415-555-1234'),
	(2, 'Tropical Treasures', '987 Palm St, Island Paradise, USA', '212-555-5678'),
	(3, 'The Urban Jungle', '456 Oak St, City Heights, USA', '213-555-8910'),
	(4, 'Vintage Vibes', '789 Maple Ave, Old Town, USA', '305-555-2345'),
	(5, 'The Book Nook', '234 Elm St, Reading, USA', '206-555-6789'),
	(6, 'Sporting Goods Emporium', '456 Pine St, Athleticville, USA', '503-555-3456'),
	(7, 'Home Sweet Home Decor', '789 Cherry St, Decor City, USA', '713-555-7890'),
	(8, 'The Pet Palace', '345 Cedar St, Purrfectville, USA', '312-555-2345'),
	(9, 'The Wine Cellar', '123 Vine St, Grapeville, USA', '617-555-6789'),
	(10, 'Electronics Galore', '456 Main St, Techville, USA', '619-555-1234');

INSERT INTO 
	[Order] (OrderKey, OrderDate, OrderStatus, TotalPrice, CustomerKey, StoreKey)
VALUES 
  (1, '2023-04-01', 'Pending', 50.00, 1, 1),
  (2,'2023-03-30', 'Processing', 120.00, 2, 2),
  (3, '2023-04-02', 'Shipped', 75.00, 3, 3),
  (4, '2023-03-28', 'Delivered', 100.00, 4, 4),
  (5, '2023-04-03', 'Cancelled', 150.00, 5, 5),
  (6, '2023-04-05', 'Refunded', 25.00, 6, 6),
  (7, '2023-03-27', 'On hold', 85.00, 7, 7),
  (8, '2023-04-06', 'Backordered', 200.00, 8, 8),
  (9, '2023-04-04', 'Returned', 30.00, 9, 9),
  (10, '2023-04-07', 'Completed', 175.00, 10, 10),
	(11, '2023-04-07', 'Processing', 450.00, 3, 2),
	(12, '2023-04-06', 'Shipped', 235.00, 5, 1),
	(13, '2023-04-05', 'Delivered', 105.50, 2, 4),
	(14, '2023-04-04', 'Completed', 75.50, 1, 5),
	(15, '2023-04-03', 'Processing', 920.00, 6, 3),
	(16, '2023-04-02', 'Shipped', 315.50, 9, 2),
	(17, '2023-04-01', 'Cancelled', 150.00, 4, 1),
	(18, '2023-03-31', 'Completed', 450.00, 8, 4),
	(19, '2023-03-30', 'Delivered', 500.00, 7, 5),
	(20, '2023-03-29', 'Refunded', 200.00, 10, 3);

INSERT INTO 
	OrderItem (OrderItemKey, Quantity, UnitPrice, ProductKey, OrderKey)
VALUES
  (1, 2, 25.00, 1, 1),
  (2, 3, 40.00, 2, 2),
  (3, 3, 25.00, 1, 3),
  (4, 2, 50.00, 3, 4),
  (5, 1, 100.00, 4, 5),
	(6, 2, 50.00, 1, 5),
  (7, 1, 25.00, 1, 6),
	(8, 2, 30.00, 5, 7),
	(9, 1, 25.00, 1, 7),
  (10, 2, 100.00, 4, 8),
	(11, 1, 30.00, 5, 9),
	(12, 1, 150.00, 5, 10),
	(13, 1, 25.00, 1, 10),
	(14, 2, 200.00, 6, 11),
	(15, 1, 50.00, 3, 11),
	(16, 1, 200.00, 6, 12),
	(17, 1, 25.00, 1, 12),
	(18, 1, 10.00, 7, 12),
	(19, 1, 100.00, 4, 13),
	(20, 1, 5.50, 8, 13),
	(21, 2, 30.00, 5, 14),
	(22, 1, 10.00, 7, 14),
	(23, 1, 5.50, 8, 14),
	(24, 1, 900.00, 9, 15),
	(25, 2, 10.00, 7, 15),
	(26, 1, 200.00, 6, 16),
	(27, 1, 100.00, 4, 16),
	(28, 1, 10.00, 7, 16),
	(29, 1, 5.50, 8, 16),
	(30, 6, 25.00, 1, 17),
	(31, 2, 225.00, 10, 18),
	(32, 2, 200.00, 6, 19),
	(33, 1, 100.00, 4, 19),
	(34, 1, 200.00, 6, 20);

INSERT INTO 
	Comment (CommentKey, CommentText, CustomerKey, ProductKey)
VALUES
	(1, 'I absolutely love this smartwatch! It has so many cool features that make my life easier.', 1, 1),
	(2, 'The air fryer works like a charm! It makes cooking healthy meals a breeze.', 2, 2),
	(3, 'I bought these leather boots for my husband and he loves them! They are stylish and comfortable.', 3, 3),
	(4, 'This board game is so much fun! I play it with my friends all the time.', 4, 4),
	(5, 'The cookbook has so many delicious recipes! I can''t wait to try them all.', 5, 5),
	(6, 'The yoga mat is great! It provides good support and the non-slip surface is really helpful.', 6, 6),
	(7, 'The lipstick set has such pretty shades! I love how long-lasting they are.', 7, 7),
	(8, 'The armchair is so elegant and comfortable! It''s the perfect addition to my living room.', 8, 8),
	(9, 'The organic coffee is delicious! It has a rich flavor and is very aromatic.', 9, 9),
	(10, 'The car speakers are amazing! They provide such clear and powerful sound.', 10, 10);

INSERT INTO 
	ShoppingCart (ShoppingCartKey, CustomerKey, ProductKey, Quantity)
VALUES 
	(1, 1, 7, 1),
	(2, 1, 6, 2),
	(3, 1, 4, 1),
	(4, 4, 1, 3),
	(5, 4, 7, 5),
	(6, 10, 10, 2),
	(7, 6, 5, 2),
	(8, 7, 6, 3),
	(9, 8, 9, 2),
	(10, 9, 8, 1);