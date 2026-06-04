import pandas as pd
import numpy as np

def print_separator(title):
    print(f"\n{'='*30} {title} {'='*30}")

# Load dataset
input_path = 'D:/DigiSkill/HousePricePrediction.csv'
df = pd.read_csv(input_path)

print_separator("Dataset Head (10 rows)")
print(df.head(10))

print_separator("Shape of Dataset")
print(df.shape)

print_separator("Dataset Information")
print(df.info())

print_separator("Dataset Description")
print(df.describe())

print_separator("Checking Missing Values")
print(df.isnull().sum())

print_separator("Handling Missing Values")

# Fill numerical missing values with mean
num_col = df.select_dtypes(include=np.number).columns
for col in num_col:
    df[col] = df[col].fillna(df[col].mean())

# Fill categorical missing values with mode
cat_cols = df.select_dtypes(include=['object']).columns
for col in cat_cols:
    if not df[col].mode().empty:
        df[col] = df[col].fillna(df[col].mode()[0])

print("Missing values handled.")

print_separator("Handling Duplicate Rows")
duplicates = df.duplicated().sum()
print(f"Number of duplicate rows: {duplicates}")
if duplicates > 0:
    df = df.drop_duplicates()
    print("Duplicates removed.")

print_separator("Dropping Id Column")
if 'Id' in df.columns:
    df = df.drop('Id', axis=1)
    print("'Id' column dropped.")
else:
    print("'Id' column not found.")

print(df.head())

print_separator("Converting Categorical Data to Numeric")
# Convert categorical variables using one-hot encoding
df = pd.get_dummies(df, drop_first=True, dtype=int)
print("Categorical variables encoded.")
print(f"New dataframe shape: {df.shape}")

print_separator("Saving Cleaned Dataset")
output_path = 'D:/DigiSkill/HousePricePredictionCleaned.csv'
df.to_csv(output_path, index=False)
print(f"Cleaned dataset saved successfully to: {output_path}")