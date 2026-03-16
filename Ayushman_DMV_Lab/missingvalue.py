import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'],
    'Age': [25, 30, np.nan, 35, 40, np.nan],
    'Salary': [50000, np.nan, 70000, 80000, np.nan, 60000],
    'City': ['New York', 'London', 'London', np.nan, 'New York', 'Paris']
}
df = pd.DataFrame(data)

print("--- Original Data with Missing Values ---")
print(df)
print("\nMissing Count per Column:")
print(df.isnull().sum())

plt.figure(figsize=(8, 4))
sns.heatmap(df.isnull(), yticklabels=False, cbar=False, cmap='viridis')
plt.title("Missing Data Heatmap (Yellow = Missing)")
plt.show()

df['Age'] = df['Age'].fillna(df['Age'].mean())

df['Salary'] = df['Salary'].fillna(df['Salary'].median())

df['City'] = df['City'].fillna(df['City'].mode()[0])

print("\n--- Cleaned Data ---")
print(df)

print("\nFinal Missing Count:")
print(df.isnull().sum())
