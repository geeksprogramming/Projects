Inventory Management System – Data Engineering & Analytics Project

## Project Overview:
This project delivers a complete data engineering and analytics solution for managing inventory products and inventory services. It features synthetic data generation, dimensional modeling, automated ETL pipelines, and interactive business dashboards. The system supports comprehensive reporting and is designed for scalability and realworld applicability.

## Objectives:
Design two separate ER models: Inventory Product and Inventory Service  
Generate clean, realistic synthetic data using Databricks  
Build starschemabased fact and dimension tables  
Automate the data processing workflow endtoend  
Visualize business KPIs using Power BI dashboards  


## Tech Stack:

Tool	     Purpose
Databricks - Data generation, modeling, ETL, automation
Power BI   - Business intelligence and visual reporting
Delta Lake - Storage layer for scalable data processing
SQL	       - Schema design and data transformation
Python	   - Data generation and workflow scripting

## Data Modeling:

Inventory Product ER Diagram:

Captures detailed relationships among products, orders, customers, agents, retailers, warehouses, payment modes, and statuses.

Dimension Tables:

 DimCustomer  
 DimProductCategory  
 DimProduct  
 DimWarehouse  
 DimRetailer  
 DimAgent  
 DimPayment  
 DimDate  
 DimProductStatus  
 DimWholesaler  
 DimOrderStatus  
 DimLocation  

Fact Tables:

 FactProduct  
 FactProductPurchase  
 FactProductStatus  
 FactOrderStatus  

Inventory Service ER Diagram:
Focuses on customer service interactions, categories, agents, and payments.

Dimension Tables:

 DimCustomer  
 DimService  
 DimServiceCategory  
 DimDate  
 DimPaymentMode  
 DimAgent  
 DimRetailer  

Fact Table:

 FactInventoryService  


## Data Pipeline and Automation:

 Data Generation: Synthetic data created for both models using Python and Databricks Notebooks  
 Schema Design: Dimensional modeling with clean, normalized structures  
 ETL Pipeline: Custom ETL workflows for data cleansing, transformation, and loading  
 Scheduling: Automated workflow orchestration via Databricks job clusters  
 Storage: All structured data stored in Delta Lake format for performance and scalability  


## Power BI Dashboards:

The project includes two fully interactive dashboards developed in Power BI:

### Inventory Product Dashboard:
 Product categorywise sales performance  
 Retailer and warehouse analysis  
 Order and product status over time  
 Customer behavior segmentation  

### Inventory Service Dashboard:
 Booking trends by service category  
 Agent and retailer performance comparison  
 Payment method analysis  
 Monthly service volume and status trends  


## How to Run the Project:

1. Clone the repository  
2. Upload the notebooks to Databricks and run ETL scripts  
3. Connect Power BI to the Delta tables or export them as CSV  
4. Open the Power BI file to explore reports or build custom visuals  

## Project Structure:

Inventory Management/

  src/
  
    data_generation/     # Code for generating sample data
    
    dimensions/          # Scripts for dimension tables
    
    facts/               # Scripts for fact tables

  reports/
  
    inventory Management.pbix       # Power BI report

  docs/
  
    project_report.pdf   # Project write-up or documentation

  README.md              # Project overview and usage
