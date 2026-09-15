INSERT INTO users (id, name, email)
VALUES (1, 'Alex', 'alex@example.com');
INSERT INTO users (id, name, email)
VALUES
    (2, 'Maria', 'maria@example.com'),
    (3, 'John', 'john@example.com'),
    (4, 'Vlad', 'vlad@example.com'),
    (5, 'Irina', 'irina@example.com'),
    (6, 'Bob', 'bob@example.com'),
    (7, 'Katya', 'katya@example.com'),
    (8, 'Rick', 'rick@example.com'),
    (9, 'Anna', 'anna@example.com'),
    (10, 'Jess', 'Jess@example.com');


INSERT INTO products (id, price, category)
VALUES
	(1, 100, 'Electronics'),
    (2, 250, 'Clothing'),
    (3, 15, 'Books'),
    (4, 500, 'Electronics'),
    (5, 30, 'Home'),
    (6, 120, 'Sports'),
    (7, 45, 'Books'),
    (8, 300, 'Clothing'),
    (9, 80, 'Home'),
    (10, 20, 'Sports');


INSERT INTO orders (id, user_id, total)
VALUES
	(1, 1, 500),
    (2, 2, 4000),
    (3, 3, 80),
    (4, 2, 150),
    (5, 4, 7),
    (6, 6, 12),
    (7, 1, 3000),
    (8, 7, 700),
    (9, 8, 850),
    (10, 1, 100);


INSERT INTO order_items (id, product_id, order_id, price, quantity)
VALUES
    (1, 4, 1, 500, 1),
    (2, 4, 2, 500, 8),
    (3, 9, 3, 80, 1),
    (4, 5, 4, 30, 5),
    (5, 3, 5, 15, 1),
    (6, 10, 6, 20, 1),
    (7, 8, 7, 300, 10),
    (8, 8, 8, 300, 2),
    (9, 9, 8, 80, 1),
    (10, 10, 8, 20, 1),
    (11, 2, 9, 250, 1),
    (12, 8, 9, 300, 2),
    (13, 1, 10, 100, 1);


SELECT* FROM users;

SELECT* FROM products
WHERE category = 'Clothing';

SELECT* FROM orders 
ORDER BY total;

SELECT* FROM orders 
ORDER BY total DESC;

UPDATE users
SET name = 'Nina'
WHERE id = 8;

DELETE FROM products 
WHERE id = 10;

SELECT users.name, orders.total
FROM users
INNER JOIN orders
ON users.id  = orders.user_id

SELECT users.name, orders.total
FROM users
LEFT JOIN orders
ON users.id = orders.user_id;

SELECT *
FROM users
FULL JOIN orders
ON users.id = orders.user_id;

SELECT COUNT(*) FROM users;
SELECT AVG(price) FROM products;
SELECT MIN(total) FROM orders;
SELECT MAX(total) FROM orders;
SELECT SUM(total) FROM orders;

SELECT category, COUNT(*) as product_count
FROM products
GROUP BY category;

SELECT user_id, SUM(total) as total_spent
FROM orders
GROUP BY user_id;

CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_orders_user_id ON orders(user_id);
