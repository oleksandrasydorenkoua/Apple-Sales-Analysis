# Apple Sales Analysis

## Project Overview
This project analyzes Apple product sales using a CSV dataset from Kaggle. It demonstrates skills in **SQL**, **Python**, **pandas**, and **matplotlib** for data analysis and visualization.

## Dataset
The project uses the file `apple_sales.csv`, which contains information about:
Sale ID, Sale date, Year, Quarter, Month, Country, Region, City, Product name, Category, Storage, Color, Unit price in USD, Discounts in %, Units sold, Discounted prices in USD, Revenue in USD, Currency, Exchange rate used for conversion, Revenue in local currency, Sales channel, Payment method, Customer segment, Customer age group, Previous OS device, Customer rating, Return status.

## Tech Stack
- Python
- pandas
- matplotlib
- SQLite
- VS Code

## Analysis Workflow
1. Load the CSV into a SQLite database (`raw_sales` table).  
2. Create a clean table (`clean_sales`) with filtered and relevant data.  
3. Perform SQL queries to aggregate data:
   - Total revenue
   - Revenue by product
   - Revenue by region
   - Monthly revenue trends
   - Best-selling products
4. Visualize the results:
   - **Bar chart**: Revenue by product  
   - **Bar chart**: Revenue by region  
   - **Line chart**: Monthly revenue trend
   - **Bar chart**: Best-selling products

## Key insights:
- MacBook Pro (M2 Ultra) generates the highest revenue
- Europe and Asia are the largest markets
- Monthly revenue reflects seasonal fluctuations in sales figures
- The highest monthly revenue occurs near late 2024, suggesting possible seasonal demand increases, such as holiday sales periods
- Apple Watch models and accessories rank among the top products by quantity sold, showing that smaller, lower-priced items can achieve high sales volume even if they generate less total revenue
