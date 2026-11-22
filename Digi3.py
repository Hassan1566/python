# Import Libraries
import pandas as pd
import numpy as np

# Machine Learning Libraries
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

#import dataset
input_path = 'D:/DigiSkill/HousePricePredictionCleaned.csv'
df = pd.read_csv(input_path)

#view first 5 rows
print(df.head())

# Features (Independent Variables)
X = df.drop("SalePrice", axis=1)

# Target (Dependent Variable)
y = df["SalePrice"]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,   # Features
    y,   # Target
    test_size=0.2,   # 20% of data for testing
    random_state=42  # for reproducibility
)
print("Training Shape:", X_train.shape)
print("Testing Shape:", X_test.shape)
# Create Linear Regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

print("Model trained successfully")

# Make predictions on the test set
y_pred = model.predict(X_test)

print(y_pred[:10])

# Evaluate the model
print("Mean Absolute Error:", mean_absolute_error(y_test, y_pred))
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
print("Root Mean Squared Error:", np.sqrt(mean_squared_error(y_test, y_pred)))
print("R2 Score:", r2_score(y_test, y_pred))

