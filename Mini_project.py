import pandas as pd

df = pd.read_csv('retail_sales.csv')

print("========Dataset Info========")
print(f"dataset dimension: {df.shape[0]} rows and {df.shape[1]} columns")

print("\n========Data Types and Columns========")
print(df.dtypes)

print("\n========Missing Values=========")
print(df.isnull().sum())


# datatype cleaning and conversion


# statistical summary