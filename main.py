import pandas as pd

df = pd.read_excel("lime_mint_sales.xlsx")

print(df.head())

print("the number of rows in the dataset is:", df.shape[0])
print("the number of columns in the dataset is:", df.shape[1])

print("the column names in the dataset are:", df.columns.tolist())

print(df.dtypes)

# statistical summary
# print("\n full info summary:")
# print(df.describe())

# Or

# avg_number_prepared = df['Prepared'].mean()
# avg_number_sold = df["Sold"].mean()

# min_number_prepared = df['Prepared'].min()
# max_number_prepared = df['Prepared'].max()

# print("\nAverage number prepared:", avg_number_prepared)
# print("Average number sold:", avg_number_sold)
# print("Minimum number prepared:", min_number_prepared)
# print("Maximum number prepared:", max_number_prepared)


summary = df[['Prepared', 'Sold']].agg(['mean', 'min', 'max'])
# print("\nSummary statistics:")
print(summary)

df['Revenue'] = df['Sold'] * df['Selling Price']
print("\nRevenue:")
print(df['Revenue'])
print(df[['Date', 'Day', 'Prepared', 'Sold', 'Selling Price', 'Cost Per Bottle', 'Revenue']])
df.to_excel("LimeMint_with_Revenue.xlsx", index=False)

df['Total Cost'] = df['Prepared'] * df['Cost Per Bottle']
print(df[['Date', 'Day', 'Prepared', 'Sold', 'Selling Price', 'Cost Per Bottle', 'Revenue', 'Total Cost']])

df.to_excel("LimeMint_with_TotalCost.xlsx", index=False)

print("File saved successfully!")

df['Profit'] = df['Revenue'] - df['Total Cost']
print(df[['Date', 'Day', 'Prepared', 'Sold', 'Selling Price', 'Cost Per Bottle', 'Revenue', 'Total Cost', 'Profit']])

df.to_excel("LimeMint_with_Profit.xlsx", index=False)


