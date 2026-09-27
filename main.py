import pandas as pd

df = pd.read_excel("lime_mint_sales.xlsx")

print(df.head())

print("the number of rows in the dataset is:", df.shape[0])
print("the number of columns in the dataset is:", df.shape[1])

print("the column names in the dataset are:", df.columns.tolist())

print(df.dtypes)

print("\n full info summary:")
df.info()