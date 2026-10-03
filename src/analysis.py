import pandas as pd

# Load the retail sales dataset
data = pd.read_csv("data/retail_sales_dataset.csv")

# Display basic information
print("Retail Sales Analysis")
print("---------------------")
print(f"Number of transactions: {len(data)}")
print(f"Number of columns: {len(data.columns)}")

# Data validation
print("\nData Validation")
print("---------------")

duplicate_count = data["Transaction ID"].duplicated().sum()
invalid_quantity = (data["Quantity"] <= 0).sum()
invalid_price = (data["Price per Unit"] <= 0).sum()
invalid_amount = (data["Total Amount"] <= 0).sum()

print(f"Duplicate transactions: {duplicate_count}")
print(f"Invalid quantities: {invalid_quantity}")
print(f"Invalid prices: {invalid_price}")
print(f"Invalid total amounts: {invalid_amount}")

# Check for missing values
print("\nMissing values:")
print(data.isnull().sum())

# Calculate total sales
total_sales = data["Total Amount"].sum()

print(f"\nTotal sales: {total_sales}")

# Sales by product category
category_sales = data.groupby("Product Category")["Total Amount"].sum()

print("\nSales by Product Category:")
print(category_sales)

# Save the results
category_sales.to_csv("output/category_sales.csv")

print("\nAnalysis completed successfully.")