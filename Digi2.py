import pandas as pd
import numpy as np

df = pd.read_csv('D:/DigiSkill/HousePricePrediction.csv')

print(df.head(10))

print("____________________________________________________________________________________________________")

print("Shape of dataset")
print(df.shape)

print("____________________________________________________________________________________________________")

print("Info of dataset")
print(df.dtypes)

print("____________________________________________________________________________________________________")

print("Describe of dataset")
print(df.describe())

print("____________________________________________________________________________________________________") 

print("Checking Missing Values")
print(df.isnull().sum()) 

print("____________________________________________________________________________________________________") 

print("Handling Missing Values")

num_col = df.select_dtypes(include=np.number).columns
for col in num_col:
    df[col] = df[col].fillna(df[col].mean())

cat_cols = df.select_dtypes(include='str').columns

for col in cat_cols:
    df[col] = df[col].fillna(df[col].mode()[0])

print("____________________________________________________________________________________________________") 

print("Duplicate Rows")
print(df.duplicated().sum())

df = df.drop_duplicates()
print("____________________________________________________________________________________________________") 

print("Dropping Id Column")
if 'Id' in df.columns:
    df = df.drop('Id', axis=1)

print(df.head())

print("____________________________________________________________________________________________________") 

print("Convert Categorical Data to Numeric")

df = pd.get_dummies(df, drop_first=True)
print(df.head())

print("____________________________________________________________________________________________________") 

print("Saving Cleaned Dataset")
df.to_csv('D:/DigiSkill/HousePricePredictionCleaned.csv', index=False)
print("Cleaned dataset saved successfully!")