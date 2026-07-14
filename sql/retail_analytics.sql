-------------------------------------------------------
-- Total Products
-------------------------------------------------------

SELECT COUNT(*) AS total_products
FROM retail_products_curated;

-------------------------------------------------------
-- Products per Category
-------------------------------------------------------

SELECT
    category,
    COUNT(*) AS total_products
FROM retail_products_curated
GROUP BY category
ORDER BY total_products DESC;

-------------------------------------------------------
-- Average Electronics Price
-------------------------------------------------------

SELECT
    ROUND(AVG(price),2) AS avg_price
FROM retail_products_curated
WHERE category='electronics';

-------------------------------------------------------
-- Top 3 Most Expensive Products
-------------------------------------------------------

SELECT
    title,
    price
FROM retail_products_curated
ORDER BY price DESC
LIMIT 3;

-------------------------------------------------------
-- Cheapest Product
-------------------------------------------------------

SELECT
    title,
    price
FROM retail_products_curated
ORDER BY price
LIMIT 1;

-------------------------------------------------------
-- Average Price by Category
-------------------------------------------------------

SELECT
    category,
    ROUND(AVG(price),2) AS avg_price
FROM retail_products_curated
GROUP BY category
ORDER BY avg_price DESC;

-------------------------------------------------------
-- Maximum Price
-------------------------------------------------------

SELECT
    MAX(price) AS maximum_price
FROM retail_products_curated;

-------------------------------------------------------
-- Minimum Price
-------------------------------------------------------

SELECT
    MIN(price) AS minimum_price
FROM retail_products_curated;

-------------------------------------------------------
-- Total Inventory Value
-------------------------------------------------------

SELECT
    SUM(price) AS inventory_value
FROM retail_products_curated;

-------------------------------------------------------
-- Products Above Average Price
-------------------------------------------------------

SELECT
    title,
    price
FROM retail_products_curated
WHERE price >
(
    SELECT AVG(price)
    FROM retail_products_curated
)
ORDER BY price DESC;

-------------------------------------------------------
-- Rating Wise Products
-------------------------------------------------------

SELECT
    title,
    rating.rate,
    rating.count
FROM retail_products_curated
ORDER BY rating.rate DESC;

-------------------------------------------------------
-- Highest Rated Product
-------------------------------------------------------

SELECT
    title,
    rating.rate
FROM retail_products_curated
ORDER BY rating.rate DESC
LIMIT 1;

-------------------------------------------------------
-- Lowest Rated Product
-------------------------------------------------------

SELECT
    title,
    rating.rate
FROM retail_products_curated
ORDER BY rating.rate
LIMIT 1;