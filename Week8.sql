-- Nguyễn Minh Phi 20206296

SELECT * FROM classicmodels.products
WHERE productDescription LIKE '%white%' OR '%black%'
  AND productDescription LIKE '%opening hood%';
  
SELECT salesRepEmployeeNumber, COUNT(*) AS count
FROM classicmodels.customers
GROUP BY salesRepEmployeeNumber
ORDER BY count DESC;

SELECT c.*
FROM customers c
JOIN orders o ON c.customerNumber = o.customerNumber
JOIN orderdetails od ON o.orderNumber = od.orderNumber
WHERE od.productCode = 'S18_2795';

CREATE VIEW combined_orders AS
SELECT o.customerNumber, o.orderNumber, SUM(od.priceEach * od.quantityOrdered) AS sale
FROM orders o
JOIN orderdetails od ON o.orderNumber = od.orderNumber
GROUP BY o.customerNumber, o.orderNumber;

-- Truy vấn 5 khách hàng có sale lớn nhất
SELECT c.customerNumber, c.customerName, c.phone, co.sale
FROM customers c
JOIN combined_orders co ON c.customerNumber = co.customerNumber
ORDER BY co.sale DESC
LIMIT 5;

-- Tạo view để kết hợp thông tin từ các bảng
CREATE VIEW combined_products AS
SELECT od.productCode, p.productName, SUM(od.priceEach * od.quantityOrdered) AS sale
FROM orderdetails od
JOIN products p ON od.productCode = p.productCode
GROUP BY od.productCode, p.productName;

-- Truy vấn 5 sản phẩm có sale lớn nhất
SELECT cp.productCode, cp.productName, cp.sale
FROM combined_products cp
ORDER BY cp.sale DESC
LIMIT 5;
