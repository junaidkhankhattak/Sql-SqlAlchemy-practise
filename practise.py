# Create Database
CREATE DATABASE customers_db;

# Create customers Table

CREATE TABLE customers (
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(15),
    city VARCHAR(50)
);

# Create orders Table
CREATE TABLE orders (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT,
    product_name VARCHAR(100) NOT NULL,
    quantity INT NOT NULL,
    order_date DATE,
    
    FOREIGN KEY (customer_id)
    REFERENCES customers(customer_id)
);
# Insert data unto orders

INSERT INTO orders
(customer_id, product_name, quantity, order_date)
VALUES
(1, 'Laptop', 1, '2026-05-16'),
(1, 'Mouse', 2, '2026-05-16'),
(2, 'Keyboard', 1, '2026-05-16');



