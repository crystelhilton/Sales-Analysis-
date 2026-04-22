import pandas as pd
import io

# Sample CSV data
csv_data = """OrderID,Date,Customer,Product,Category,Quantity,Price,Region
1001,2024-01-05,John Doe,Laptop,Electronics,1,800,North
1002,2024-01-06,Jane Smith,Mouse,Electronics,2,25,South
1003,2024-01-07,Alice Brown,Keyboard,Electronics,1,45,East
1004,2024-01-08,Bob White,Desk,Furniture,1,150,West
1005,2024-01-09,Chris Green,Chair,Furniture,2,85,North
1006,2024-01-10,Emma Stone,Monitor,Electronics,1,200,South
1007,2024-01-11,Liam Scott,Table,Furniture,1,120,East
1008,2024-01-12,Olivia King,Headphones,Electronics,3,60,West
1009,2024-01-13,Noah Lee,Laptop,Electronics,1,900,North
1010,2024-01-14,Sophia Hall,Chair,Furniture,1,95,South"""

# Read CSV into DataFrame
df = pd.read_csv(io.StringIO(csv_data))

# 1. Calculate total sales (Quantity × Price)
df['Sales'] = df['Quantity'] * df['Price']

print("=" * 70)
print("SALES DATA ANALYSIS REPORT")
print("=" * 70)

# 2. Calculate total sales
total_sales = df['Sales'].sum()
print(f"\n1. TOTAL SALES: ${total_sales:,.2f}")

# 3. Find total sales by category
print("\n2. CATEGORY-WISE SALES:")
category_sales = df.groupby('Category')['Sales'].sum().sort_values(ascending=False)
for category, sales in category_sales.items():
    percentage = (sales / total_sales) * 100
    print(f"   {category}: ${sales:,.2f} ({percentage:.1f}%)")

# 4. Identify the top-selling product
print("\n3. TOP-SELLING PRODUCT:")
product_sales = df.groupby('Product')['Sales'].sum().sort_values(ascending=False)
top_product = product_sales.index[0]
top_product_sales = product_sales.iloc[0]
print(f"   Product: {top_product}")
print(f"   Total Sales: ${top_product_sales:,.2f}")

# 5. Find region-wise sales distribution
print("\n4. REGION-WISE SALES DISTRIBUTION:")
region_sales = df.groupby('Region')['Sales'].sum().sort_values(ascending=False)
for region, sales in region_sales.items():
    percentage = (sales / total_sales) * 100
    print(f"   {region}: ${sales:,.2f} ({percentage:.1f}%)")

# 6. Display orders where sales > $200
print("\n5. HIGH-VALUE ORDERS (Sales > $200):")
high_value_orders = df[df['Sales'] > 200][['OrderID', 'Customer', 'Product', 'Quantity', 'Price', 'Sales', 'Region']]
print(high_value_orders.to_string(index=False))

print("\n" + "=" * 70)