CREATE DATABASE OttosMarketplaceDB;

USE OttosMarketplaceDB;

CREATE TABLE Customer (
	CustomerKey INT PRIMARY KEY,
	FirstName VARCHAR(50) NOT NULL,
	LastName VARCHAR(50) NOT NULL,
	CustomerAddress VARCHAR(100) NOT NULL,
	CustomerEmail VARCHAR(50) NOT NULL,
	CustomerPhone VARCHAR(20) NOT NULL,
	CONSTRAINT UK_Customer_CustomerEmail UNIQUE(CustomerEmail),
	CONSTRAINT UK_Customer_CustomerPhone UNIQUE(CustomerPhone));

CREATE TABLE Position (
	PositionKey INT PRIMARY KEY,
	PositionName VARCHAR(50) NOT NULL,
	CONSTRAINT UK_Position_PositionName UNIQUE(PositionName));

CREATE TABLE Employee (
	EmployeeKey INT PRIMARY KEY,
	FirstName VARCHAR(50) NOT NULL,
	LastName VARCHAR(50) NOT NULL,
	EmployeeAddress VARCHAR(100) NOT NULL,
	EmployeeEmail VARCHAR(50) NOT NULL,
	EmployeePhone VARCHAR(20) NOT NULL,
	PositionKey INT FOREIGN KEY REFERENCES Position(PositionKey),
	CONSTRAINT UK_Employee_EmployeeAddress UNIQUE(EmployeeAddress),
	CONSTRAINT UK_Employee_EmployeeEmail UNIQUE(EmployeeEmail),
	CONSTRAINT UK_Employee_EmployeePhone UNIQUE(EmployeePhone));

CREATE TABLE Supplier (
	SupplierKey INT PRIMARY KEY,
	SupplierName VARCHAR(100) NOT NULL,
	SupplierAddress VARCHAR(100) NOT NULL,
	SupplierEmail VARCHAR(50) NOT NULL,
	SupplierPhone VARCHAR(20) NOT NULL,
	CONSTRAINT UK_Supplier_SupplierName UNIQUE(SupplierName),
	CONSTRAINT UK_Supplier_SupplierEmail UNIQUE(SupplierEmail),
	CONSTRAINT UK_Supplier_SupplierPhone UNIQUE(SupplierPhone));

CREATE TABLE ProductCategory (
	ProductCategoryKey INT PRIMARY KEY,
	ProductCategoryName VARCHAR(50) NOT NULL,
	ProductCategoryDescription VARCHAR(200) NOT NULL,
	CONSTRAINT UK_ProductCategory_ProductCategoryName UNIQUE(ProductCategoryName));

CREATE TABLE Product (
	ProductKey INT PRIMARY KEY,
	ProductName VARCHAR(100) NOT NULL,
	ProductDescription VARCHAR(200) NOT NULL,
	UnitPrice DECIMAL(10,2) NOT NULL,
	StockQuantity INT NOT NULL,
	ProductCategoryKey INT FOREIGN KEY REFERENCES ProductCategory(ProductCategoryKey),
	SupplierKey INT FOREIGN KEY REFERENCES Supplier(SupplierKey));

CREATE TABLE Store (
	StoreKey INT PRIMARY KEY,
	StoreName VARCHAR(200) NOT NULL,
	StoreAddress VARCHAR(100) NOT NULL,
	StorePhone VARCHAR(20) NOT NULL,
	CONSTRAINT UK_Store_StoreName UNIQUE(StoreName),
	CONSTRAINT UK_Store_StorePhone UNIQUE(StorePhone));

CREATE TABLE [Order] (
	OrderKey INT PRIMARY KEY,
	OrderDate DATE NOT NULL,
	OrderStatus VARCHAR(100) NOT NULL,
	TotalPrice DECIMAL(10,2) NOT NULL,
	CustomerKey INT FOREIGN KEY REFERENCES Customer(CustomerKey),
	StoreKey INT FOREIGN KEY REFERENCES Store(StoreKey),
	CONSTRAINT CK_Order_OrderStatus CHECK(OrderStatus IN ('Pending', 'Processing', 'Shipped', 'Delivered', 'Cancelled', 'Refunded', 'On hold', 'Backordered', 'Returned', 'Completed')));

CREATE TABLE OrderItem (
	OrderItemKey INT PRIMARY KEY,
	Quantity INT NOT NULL,
	UnitPrice DECIMAL(10,2),
	ProductKey INT FOREIGN KEY REFERENCES Product(ProductKey),
	OrderKey INT FOREIGN KEY REFERENCES [Order](OrderKey),
	CONSTRAINT CK_OrderItem_Quantity CHECK(Quantity > 0));

CREATE TABLE Comment (
	CommentKey INT PRIMARY KEY,
	CommentText VARCHAR(500) NOT NULL,
	CustomerKey INT FOREIGN KEY REFERENCES Customer(CustomerKey),
	ProductKey INT FOREIGN KEY REFERENCES Product(ProductKey));

CREATE TABLE ShoppingCart (
	ShoppingCartKey INT PRIMARY KEY,
	CustomerKey INT FOREIGN KEY REFERENCES Customer(CustomerKey),
	ProductKey INT FOREIGN KEY REFERENCES Product(ProductKey),
	Quantity INT NOT NULL,
	CONSTRAINT CK_ShoppingCart_Quantity CHECK(Quantity > 0));
