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


df['Left Over'] = df["Prepared"] - df["Sold"]
print(df[['Date', 'Day', 'Prepared', 'Sold', 'Selling Price', 'Cost Per Bottle', 'Revenue', 'Total Cost', 'Profit', 'Left Over']])

df.to_excel("LimeMint_with_LeftOver.xlsx", index=False)

highest_revenue_row = df.loc[df['Revenue'].idxmax()]

print("\nHighest revenue day:")
print(highest_revenue_row[['Date', 'Day', 'Revenue']])

highest_profit_row = df.loc[df['Profit'].idxmax()]
print("\nHighest profit day:")
print(highest_profit_row[['Day', 'Profit']])


lowest_profit_row = df.loc[df['Profit'].idxmin()]
print("\nLowest profit day:")
print(lowest_profit_row[['Day', 'Profit']])

total_revenue = df['Revenue'].sum()
print("\nTotal revenue:")
print(total_revenue)

total_production_cost = df['Total Cost'].sum()
print("\nTotal production cost:")
print(total_production_cost)

total_profit = df['Profit'].sum()
print("\n total profit")
print(total_profit)

total_sales = df['Sold'].sum()
print("\nTotal sales:")
print(total_sales)

total_leftover = df['Left Over'].sum()
print("\nTotal leftover:")
print(total_leftover)

highest_number_sold = df.loc[[df['Sold'].idxmax()]]
print("\nHighest number sold:")
print(highest_number_sold[['Day', 'Sold']])

most_leftover_drinks_row = df.loc[[df['Left Over'].idxmax()]]
print("\nMost leftover drinks:")
print(most_leftover_drinks_row[['Day', 'Left Over']])
# Create Sales Rate (keep it as a number)
df['Sales Rate'] = (df['Sold'] / df['Prepared']) * 100


print(df[['Date', 'Day', 'Prepared', 'Sold', 'Selling Price', 'Cost Per Bottle', 
          'Revenue', 'Total Cost', 'Profit', 'Left Over', 'Sales Rate']].to_string(
    formatters={'Sales Rate': '{:.1f}%'.format}
))

df.to_excel("LimeMint_with_SalesRate.xlsx", index=False)

highest_sales_rate_row = df.loc[df['Sales Rate'].idxmax()]

print("\nHighest sales rate day:")
print(f"Day: {highest_sales_rate_row['Day']}")
print(f"Sales Rate: {highest_sales_rate_row['Sales Rate']:.1f}%")


lowest_sales_rate_row = df.loc[df['Sales Rate'].idxmin()]
print("\nLowest sales rate day:")
print(f"Day: {lowest_sales_rate_row['Day']}")
print(f"Sales Rate: {lowest_sales_rate_row['Sales Rate']:.1f}%")


profit_greater_than_3000 = df['Profit'] > 3000
print("\nDays with profit greater than 3000:")
print(df[profit_greater_than_3000][['Day', 'Profit']])

profit_descending_to_ascending_order = df.sort_values(by='Profit', ascending=False)
print("\nDays sorted by profit (descending order):")
print(profit_descending_to_ascending_order[['Day', 'Profit']].to_string(index=False))


sales_descending_to_ascending_order = df.sort_values(by='Sold', ascending=False)
print("\nDays sorted by sales (descending order):")
print(sales_descending_to_ascending_order[['Day', 'Sold']].to_string(index=False))


top_3_days_by_profit = df.nlargest(3, 'Profit')[['Day', 'Profit']]
print("\n top 3 profitable days")
print(top_3_days_by_profit.to_string(index=False) )
