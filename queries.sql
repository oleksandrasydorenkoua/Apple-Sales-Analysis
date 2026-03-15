create table clean_sales AS
select 
    product_name,
    category,
    region,
    sale_date,
    units_sold as quantity,
    unit_price_usd as price,
    revenue_usd as revenue
from raw_sales;

# total revenue
SELECT
sum(quantity*price) as total_revenue
from clean_sales;
# total revenue = 18735068.71 usd

# Revenue by product
select product_name,
sum(quantity*price) as revenue
from clean_sales
group by product_name
order by revenue desc;

# Revenue by region
select region,
sum(quantity*price) as revenue
from clean_sales
group by region
order by revenue desc;

# Monthly revenue
select 
strftime('%Y-%m', sale_date) AS month,
sum(quantity*price) as revenue
from clean_sales
group by month
order by month;

# Best-selling products
select 
product_name,
sum(quantity) as total_sold
from clean_sales
group by product_name
order by total_sold desc;