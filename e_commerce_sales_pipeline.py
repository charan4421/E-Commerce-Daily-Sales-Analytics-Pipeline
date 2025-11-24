# e_commerce_sales_pipeline.py
# Project: E-Commerce Daily Sales Analytics Pipeline
# Author: Charan
# Date: 2025-11-24
# Description: This script calculates daily sales metrics, identifies top products, 
# and generates visualizations for an e-commerce dataset.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ----------------------------
# Step 1: Load the dataset
# ----------------------------
# Replace 'ecommerce_sales.csv' with your actual CSV file
data = pd.read_csv("ecommerce_sales.csv", parse_dates=['order_date'])

# ----------------------------
# Step 2: Basic sanity checks
# ----------------------------
print("Columns:", data.columns)
print("Missing values:\n", data.isnull().sum())
print("Sample data:\n", data.head())

# ----------------------------
# Step 3: Calculate daily sales metrics
# ----------------------------
daily_sales = data.groupby('order_date').agg(
    total_orders=('order_id', 'nunique'),
    total_revenue=('price', lambda x: (x * data.loc[x.index, 'quantity']).sum()),
    total_quantity=('quantity', 'sum')
).reset_index()

print("\nDaily Sales Summary:\n", daily_sales.head())

# ----------------------------
# Step 4: Top products by revenue
# ----------------------------
top_products = data.groupby('product_id').agg(
    total_revenue=('price', lambda x: (x * data.loc[x.index, 'quantity']).sum())
).sort_values('total_revenue', ascending=False).head(10)

print("\nTop 10 Products by Revenue:\n", top_products)

# ----------------------------
# Step 5: Visualizations
# ----------------------------
# Daily Revenue Trend
plt.figure(figsize=(10,6))
sns.lineplot(data=daily_sales, x='order_date', y='total_revenue', marker='o')
plt.title("Daily Revenue Trend")
plt.xlabel("Date")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Top Products by Revenue
plt.figure(figsize=(10,6))
sns.barplot(x=top_products.index.astype(str), y=top_products['total_revenue'])
plt.title("Top 10 Products by Revenue")
plt.xlabel("Product ID")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
