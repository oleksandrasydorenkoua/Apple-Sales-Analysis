# Apple Sales Analysis

## Project Overview
This project analyzes Apple product sales using a CSV dataset from Kaggle. It demonstrates skills in **SQL**, **Python**, **pandas**, and **matplotlib** for data analysis and visualization.

## Dataset
The project uses the file `apple_sales.csv`, which contains information about:

- Sale ID
- Sale date
- Year
- Quarter
- Month
- Country
- Region
- City
- Product name
- Category
- Storage
- Color
- Unit price in USD
- Discounts in %
- Units sold
- Discounted prices in USD
- Revenue in USD
- Currency
- Exchange rate used for conversion
- Revenue in local currency
- Sales channel
- Payment method
- Customer segment
- Customer age group
- Previous OS device
- Customer rating
- Return status


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
