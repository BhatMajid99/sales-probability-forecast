import pandas as pd
import matplotlib.pyplot as plt

# Read Excel file
data = pd.read_excel("sales_data.xlsx")

# Show dataset
print("Sales Dataset:\n")
print(data)

# Average sales
average_sales = data["Units Sold"].mean()

# Maximum sales
max_sales = data["Units Sold"].max()

# Minimum sales
min_sales = data["Units Sold"].min()

# Highest selling product
highest_product = data.loc[data["Units Sold"].idxmax(), "Product Name"]

# Total revenue
total_revenue = data["Revenue"].sum()

# Product-wise total sales
product_sales = data.groupby("Product Name")["Units Sold"].sum()

# Probability calculation
high_sales_count = len(data[data["Units Sold"] > average_sales])

total_records = len(data)

probability = high_sales_count / total_records

# Export summary to CSV
summary = pd.DataFrame({
    "Average Sales": [round(average_sales)],
    "Maximum Sales": [max_sales],
    "Minimum Sales": [min_sales],
    "Total Revenue": [total_revenue],
    "Probability Above Average": [round(probability, 2)]
})

summary.to_csv("sales_summary.csv", index=False)

# Output section
print("\n----- Sales Analysis -----")

print("\nAverage Units Sold:", round(average_sales))

print("Maximum Units Sold:", max_sales)

print("Minimum Units Sold:", min_sales)

print("Highest Selling Product:", highest_product)

print("Total Revenue:", total_revenue)

print("\nProduct-wise Total Sales:\n")
print(product_sales)

print("\nProbability of Sales Being Above Average:",
      round(probability, 2))

print("\nPredicted Sales For Next Month:",
      round(average_sales))

print("\nSales summary exported successfully!")

# Graph Section
product_sales.plot(kind="bar")

plt.title("Product-wise Sales Analysis")

plt.xlabel("Product Name")

plt.ylabel("Units Sold")

plt.show()