import pandas as pd

# Read Excel file
data = pd.read_excel("sales_data.xlsx")

# Show complete data
print("Sales Data:\n")
print(data)

# Find average sales
average = data["Units Sold"].mean()

# Show average
print("\nAverage Units Sold:", average)

# Predict next month sales
print("\nPredicted Sales for Next Month:", round(average))