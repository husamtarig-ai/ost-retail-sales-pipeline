import pandas as pd

# Load the retail sales dataset
data = pd.read_csv("data/retail_sales_dataset.csv")

# Display basic information
print("Retail Sales Analysis")
print("---------------------")
print(f"Number of transactions: {len(data)}")
print(f"Number of columns: {len(data.columns)}")

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