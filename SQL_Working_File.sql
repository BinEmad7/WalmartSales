SELECT *
FROM Walmart;

-- Number of Cities (98)
SELECT COUNT(DISTINCT city)
FROM Walmart
;

-- Number of Branches (100)
SELECT COUNT(DISTINCT branch)
FROM Walmart
;

-- Cities with more than One Branch (Waxahachie, Weslaco)
SELECT city, COUNT(DISTINCT branch) as branch_count
FROM Walmart
GROUP BY city
HAVING COUNT(DISTINCT branch) > 1
;

-- Top 5 Cities by Total Revenue (Weslaco, Waxahachie, Plano, San Antonio, Port Arthur)
SELECT city, SUM(total_price) Total_Revenue
FROM Walmart
GROUP BY city
ORDER BY SUM(total_price) DESC
;

-- Top 5 Branches by Total Revenue (WALM009, WALM074, WALM003, WALM058, WALM030)
SELECT branch, SUM(total_price) Total_Revenue
FROM Walmart
GROUP BY branch
ORDER BY SUM(total_price) DESC
;

-- Total Units by Category (Fashion accessories:9653, Home and lifestyle:9610,
--							Electronic accessories:1494, Food and beverages:952, 
--							Sports and travel:920, Health and beauty:854)
SELECT category, SUM(quantity) Total_Units
FROM Walmart
GROUP BY category
ORDER BY Total_Units DESC
;

-- Number of Transactions by Payment Methods (Credit card:4256, Ewallet:3881, Cash:1832)
SELECT payment_method, COUNT(*) Number_of_Transactions
FROM Walmart
GROUP BY payment_method
ORDER BY Number_of_Transactions DESC
;

-- Total Revenue by Payment Method (Credit card:488821.02, Ewallet:457316.07, Cash:263589.29)
SELECT payment_method, SUM(total_price) Total_Revenue
FROM Walmart
GROUP BY payment_method
ORDER BY Total_Revenue DESC
;
