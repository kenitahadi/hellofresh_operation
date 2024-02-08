--Request 1
--For the customer with email address ‘ilovefood83@hotmail.com’ show all product_skus the
--customer has an active subscription for

SELECT p.product_SKU
FROM customer c
JOIN subscription s ON c.id_customer = s.fk_customer
JOIN product p ON s.fk_product_subscribed_to = p.id_product
WHERE c.email = 'ilovefood83@hotmail.com' 
AND s.status = 'active';

--Request 2
--Get a list of all the customers (id_customer) that have an active subscription to a product
--that corresponds to a product family with product_family_handle = ‘classic-box’

SELECT DISTINCT c.id_customer
FROM customer c
JOIN subscription s ON c.id_customer = s.fk_customer
JOIN product p ON s.fk_product_subscribed_to = p.id_product
JOIN product_family pf ON p.fk_product_family = pf.id_product_family
WHERE s.status = 'active'
AND pf.product_family_handle = 'classic-box';


--Request 3
--Count of customers that have ordered more than one product


--Request 4
--Get a list of all customers which got a box delivered to them two weeks ago, and the count
--of boxes that had been delivered to them up to that week

--Request 5
--For all our customers, get the date of the latest order delivered to them and include
--associated product_sku, delivery_date and purchase price. If there were two orders
--delivered to the same customer on the same date, they should both appear
