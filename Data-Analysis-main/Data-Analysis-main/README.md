Gaming Booth Optimization – Data Analytics Project

## Project Overview
This project focuses on identifying the best mall, time of day, and day of the week to open a gaming booth. The goal is to maximize foot traffic and revenue by analyzing visitor behavior data using tools like Excel, SQL (SSMS), and Python.

We worked with a dataset containing mall visitor details such as age group, visit timing, and total bill. By studying this data, we aimed to understand when and where potential customers are most active and spend the most.

## Objectives
- Explore visitor trends across three different malls
- Identify which age groups are the most profitable
- Analyze spending behavior by day of the week and time of day
- Recommend the best mall, time, and day to set up the gaming booth

## Tools Used

 Tool         Purpose                                      
 Excel       - Initial cleaning, pivot tables, charts      
 SQL (SSMS)  - Data filtering, aggregation, pattern finding
 Python      - Deeper analysis, visualization with pandas and seaborn

## Dataset Description
The dataset includes:
- Mall – Mall name (3 malls)
- Age Group – Visitor age ranges (e.g., 10–20, 21–30, etc.)
- Day of the Week – Monday to Sunday
- Time of the Day – Morning, Afternoon, Evening
- Total Bill – Total amount spent by each visitor
- Items Bought
- Product Category
- Payment Method
- Returning Customer – Yes/No
- Visit Duration

## Workflow

### Excel
- Cleaned and organized the raw data
- Created pivot tables to view trends by age, time, and mall
- Plotted charts for better understanding

### SQL (SSMS)
- Ran queries to group and filter data by mall, time, and age
- Compared average and total bills
- Identified busiest days and most profitable age groups

### Python
- Loaded data using pandas
- Visualized patterns using seaborn and matplotlib
- Built charts like heatmaps and bar plots to support conclusions

## Folder Structure

Data Analysis/

  src/
  
    DashBoard/              Code and files for Excel pivot tables and charts
    
    SQL_Analysis/            SQL queries used in SSMS
    
    Python_Analysis/         Python notebook for data analysis

  reports/
  
    Data Analysis Report.pdf   Final report with analysis and insights

  README.md                  Project summary and instructions

## How to Run This Project

1. Start with the cleaned_dataset.xlsx file in the docs folder.
2. Open the Excel file inside excel_work to see basic summaries and pivot charts.
3. Use the SQL queries in sql_queries with SSMS to explore key trends.
4. Open the Python notebook in python_scripts to generate final plots.
5. Read the Data Analysis Report.pdf for detailed findings and recommendations.

## Final Takeaways

- Best Mall: sarath city mall had the highest overall spending and more returning visitors
- Best Time: Evening hours showed the highest customer activity
- Best Day: Saturday was the busiest and most profitable day
- Target Age Group: 21–30-year-olds spent the most consistently

This analysis gives a clear direction on when and where to launch the gaming booth for the best results.

Created as part of a data analytics coursework project.
