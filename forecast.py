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

# Predicted future sales
predicted_sales = round(average_sales)

print("\nAverage Units Sold:", average_sales)

print("Maximum Units Sold:", max_sales)

print("Minimum Units Sold:", min_sales)

print("\nPredicted Sales For Next Month:", predicted_sales)