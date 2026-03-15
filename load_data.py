import pandas as pd
import sqlite3
import matplotlib.pyplot as plt


df = pd.read_csv("/Users/oleksandra/Desktop/privat/apple-sales-analysis/apple_sales.csv")

conn = sqlite3.connect("/Users/oleksandra/Desktop/privat/apple-sales-analysis/sales.db")

df.to_sql("raw_sales", conn, if_exists="replace", index=False)



# Revenue by product
query = """           
select product_name,
sum(quantity*price) as revenue
from clean_sales
group by product_name
order by revenue desc;
"""
df_rev_by_prod = pd.read_sql(query, conn)

print(df_rev_by_prod)



df_rev_by_prod.sort_values("revenue", ascending=False).plot(
x="product_name",
y="revenue",
kind="bar"
)
plt.title("Revenue by Apple Product")
plt.show()



# Revenue by region
query = """           
select region,
sum(quantity*price) as revenue
from clean_sales
group by region
order by revenue desc;
"""
df_rev_by_reg = pd.read_sql(query, conn)

print(df_rev_by_reg)


df_rev_by_reg.sort_values("revenue", ascending=False).plot(
x="region",
y="revenue",
kind="bar"
)
plt.title("Revenue by region")
plt.show()



# Monthly revenue
query = """           
select 
strftime('%Y-%m', sale_date) AS month,
sum(quantity*price) as revenue
from clean_sales
group by month
order by month;
"""
df_rev_month = pd.read_sql(query, conn)

print(df_rev_month)



df_rev_month.sort_values("month").plot(
x="month",
y="revenue",
kind="line"
)
plt.title("Monthly revenue")
plt.grid(True)
plt.show()



# Best-selling products
query = """           
select 
product_name,
sum(quantity) as total_sold
from clean_sales
group by product_name
order by total_sold desc;
"""
df_best_prod = pd.read_sql(query, conn)

print(df_best_prod)



df_best_prod.sort_values("total_sold", ascending=False).plot(
x="product_name",
y="total_sold",
kind="bar"
)
plt.title("Best-selling products")
plt.show()





conn.close()
