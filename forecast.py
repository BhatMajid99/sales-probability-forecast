import pandas as pd

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

# Product with highest sales
highest_product = data.loc[data["Units Sold"].idxmax(), "Product Name"]

# Probability calculation
high_sales_count = len(data[data["Units Sold"] > average_sales])

total_records = len(data)

probability = high_sales_count / total_records

# Display results
print("\n----- Sales Analysis -----")

print("\nAverage Units Sold:", round(average_sales))

print("Maximum Units Sold:", max_sales)

print("Minimum Units Sold:", min_sales)

print("Highest Selling Product:", highest_product)

print("\nProbability of Sales Being Above Average:",
      round(probability, 2))

print("\nPredicted Sales For Next Month:",
      round(average_sales))