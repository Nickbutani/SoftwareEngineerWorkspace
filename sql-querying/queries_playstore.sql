-- Comments in SQL Start with dash-dash --

-- SELECT * from analytics WHERE id = 1880;

-- SELECT id, app_name                                                 
-- FROM analytics                                                                  
-- WHERE last_updated = '2018-08-01';

-- SELECT category, COUNT(*) AS app_count                              
-- FROM analytics                                                                 
-- GROUP BY category;


-- SELECT app_name, COUNT(*) AS review_count
-- FROM analytics
-- GROUP BY app_name
-- ORDER BY review_count DESC
-- LIMIT 5;


-- SELECT app_name, COUNT(*) AS review_count
-- FROM analytics
-- WHERE rating >= 4.8
-- GROUP BY app_name
-- ORDER BY review_count DESC
-- LIMIT 1;

-- SELECT category, AVG(rating) AS avg_rating
-- FROM analytics
-- GROUP BY category
-- ORDER BY avg_rating DESC;

-- SELECT app_name, price, rating
-- FROM analytics
-- WHERE rating < 3
-- ORDER BY price DESC
-- LIMIT 1;

-- SELECT *
-- FROM analytics
-- WHERE min_installs <= 50 AND rating IS NOT NULL
-- ORDER BY rating DESC;

-- SELECT app_name
-- FROM analytics
-- WHERE rating < 3
-- GROUP BY app_name
-- HAVING COUNT(*) >= 10000;

-- SELECT app_name, COUNT(*) AS review_count
-- FROM analytics
-- WHERE price BETWEEN 0.10 AND 1.00
-- GROUP BY app_name
-- ORDER BY review_count DESC
-- LIMIT 10;

-- SELECT app_name, MAX(last_updated) AS latest_update
-- FROM analytics;

-- SELECT app_name, MAX(price) AS max_price
-- FROM analytics;

-- SELECT COUNT(*) AS total_reviews
-- FROM analytics;

-- SELECT category
-- FROM analytics
-- GROUP BY category
-- HAVING COUNT(*) > 300;

-- SELECT app_name, min_installs, COUNT(*) AS review_count, min_installs / COUNT(*) AS proportion
-- FROM analytics
-- WHERE min_installs >= 100000
-- GROUP BY app_name, min_installs
-- ORDER BY proportion DESC
-- LIMIT 1;
