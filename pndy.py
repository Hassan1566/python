import pandas as pd
import matplotlib.pyplot as plt



df = pd.read_csv("ecommerce_sales_analytics_5000.csv", parse_dates=['order_date'])

df = df.sample(n = 1000)


monthly_revenue = (df.set_index('order_date')["revenue"].resample('ME').sum())

fig, ax = plt.subplots(figsize=(8,6))

ax.plot(monthly_revenue.index, monthly_revenue.values, linewidth=2, marker='o')
ax.set_title("Monthly Revenue")
ax.set_xlabel("Date")
ax.set_ylabel("Revenue")


category_revenue = df.groupby('product_category')['revenue'].sum()

fig, ax = plt.subplots(figsize=(8,6))

ax.bar(category_revenue.index, category_revenue.values)
ax.set_title("Revenue by Category")
ax.set_xlabel("Category")
ax.set_ylabel("Revenue")


grouped = df.groupby(['product_category', 'region'])['revenue'].sum().unstack()

fig, ax = plt.subplots(figsize=(10,6))
grouped.plot(kind='bar', ax=ax)
ax.set_title("Revenue by Category and Region")
ax.set_xlabel("Category")
ax.set_ylabel("Revenue")


fig, ax = plt.subplots(figsize=(8,6))
df['revenue'].plot(kind='hist', bins=20, ax=ax, density=True)
ax.set_title("Revenue Distribution")
ax.set_xlabel("Revenue")
ax.set_ylabel("Density")
plt.show()