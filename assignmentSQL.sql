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

SELECT COUNT(DISTINCT o.id_customer) AS customers_with_multiple_orders
FROM (
    SELECT id_customer, COUNT(DISTINCT id_order) AS num_orders
    FROM order
    GROUP BY id_customer
    HAVING num_orders > 1
) AS o;

--Request 4
--Get a list of all customers which got a box delivered to them two weeks ago, and the count
--of boxes that had been delivered to them up to that week

SELECT o.id_customer, COUNT(DISTINCT o.id_order) AS count_of_boxes_delivered
FROM `order` o
WHERE o.delivery_date >= DATE_SUB(CURDATE(), INTERVAL 2 WEEK)
    AND o.delivery_date < DATE_SUB(CURDATE(), INTERVAL 1 WEEK)
GROUP BY o.id_customer;

--Request 5
--For all our customers, get the date of the latest order delivered to them and include
--associated product_sku, delivery_date and purchase price. If there were two orders
--delivered to the same customer on the same date, they should both appear

SELECT o.id_customer,
       p.product_SKU,
       o.delivery_date,
       o.purchase_price
FROM `order` o
JOIN product p ON o.fk_product = p.id_product
JOIN (
    SELECT id_customer,
           delivery_date,
           MAX(order_id) AS latest_order_id
    FROM `order`
    GROUP BY id_customer, delivery_date
) AS latest_orders ON o.id_customer = latest_orders.id_customer 
                   AND o.delivery_date = latest_orders.delivery_date 
                   AND o.order_id = latest_orders.latest_order_id;

