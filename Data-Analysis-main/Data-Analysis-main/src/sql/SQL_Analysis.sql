-- 1. Total Revenue per Mall and Product Category
SELECT Mall, Product_Category, SUM(Total_Bill) AS TotalSales
FROM raw_data
GROUP BY Mall, Product_Category
ORDER BY Mall, TotalSales DESC;


--Peak Shopping Time for Each Product Category
SELECT Product_Category, Time_of_the_Day, SUM(Total_Bill) AS TotalSales
FROM raw_data
GROUP BY Product_Category, Time_of_the_Day
ORDER BY Product_Category, TotalSales DESC;

-- 3. Age Group Preferences per Product Category
SELECT Product_Category, Age_Group, COUNT(*) AS Purchases
FROM raw_data
GROUP BY Product_Category, Age_Group
ORDER BY Product_Category, Purchases DESC;

-- 4. Returning Customer Ratio by Product Category
SELECT Product_Category,
       SUM(CASE WHEN Is_Returning_Customer = 1 THEN 1 ELSE 0 END) AS Returning,
       COUNT(*) AS Total,
       CAST(SUM(CASE WHEN Is_Returning_Customer = 1 THEN 1 ELSE 0 END) * 100.0 / COUNT(*) AS DECIMAL(5,2)) AS ReturningRatePercent
FROM raw_data
GROUP BY Product_Category
ORDER BY ReturningRatePercent DESC;

-- 5. Highest-Spending Age Groups per Department
SELECT Product_Category, Age_Group, AVG(Total_Bill) AS AvgBill
FROM raw_data
GROUP BY Product_Category, Age_Group
ORDER BY Product_Category, AvgBill DESC;


-- 6. Items Bought vs. Revenue per Department
SELECT Product_Category,
       SUM(Items_Bought) AS TotalItems,
       SUM(Total_Bill) AS TotalRevenue,
       CAST(SUM(Total_Bill)/NULLIF(SUM(Items_Bought),0) AS DECIMAL(6,2)) AS RevenuePerItem
FROM raw_data
GROUP BY Product_Category
ORDER BY RevenuePerItem DESC;

-- 7. Visit Duration Insight per Product Category
SELECT Product_Category,
       AVG(Visit_Duration) AS AvgMinutes,
       MAX(Visit_Duration) AS MaxVisit,
       MIN(Visit_Duration) AS MinVisit
FROM raw_data
GROUP BY Product_Category
ORDER BY AvgMinutes DESC;

-- 8. Payment Method Distribution per Department
SELECT Product_Category, Payment_Method, COUNT(*) AS PaymentCount
FROM raw_data
GROUP BY Product_Category, Payment_Method
ORDER BY Product_Category;

-- 9. Sales Heatmap by Day of the Week
SELECT Day_of_the_Week, Product_Category, SUM(Total_Bill) AS TotalSales
FROM raw_data
GROUP BY Day_of_the_Week, Product_Category
ORDER BY Day_of_the_Week, TotalSales DESC;

-- 10. Mall-Wise Returning Customer Sales
SELECT Mall, Product_Category,
       SUM(CASE WHEN Is_Returning_Customer = 1 THEN Total_Bill ELSE 0 END) AS ReturningCustomerSales
FROM raw_data
GROUP BY Mall, Product_Category
ORDER BY Mall, ReturningCustomerSales DESC;


