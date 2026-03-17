import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("dataset.csv")

print("===== DATA PREVIEW =====")
print(df.head())

# -----------------------------
# 1. DETECT MISSING VALUES
# -----------------------------
print("\n===== MISSING VALUES =====")
missing = df.isnull().sum()
print(missing)

# -----------------------------
# 2. HANDLE MISSING VALUES
# -----------------------------
# Option 1: Fill numerical columns with mean
for col in df.select_dtypes(include=np.number).columns:
    df[col].fillna(df[col].mean(), inplace=True)

# Option 2: Fill categorical columns with mode
for col in df.select_dtypes(include='object').columns:
    df[col].fillna(df[col].mode()[0], inplace=True)

print("\n===== AFTER HANDLING MISSING VALUES =====")
print(df.isnull().sum())
missing = df.isnull().sum()

plt.figure()
missing.plot(kind='bar')
plt.title("Missing Values per Column")
plt.xlabel("Columns")
plt.ylabel("Number of Missing Values")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# -----------------------------
# 3. DETECT OUTLIERS (IQR METHOD)
# -----------------------------
print("\n===== OUTLIERS DETECTION =====")

outliers_dict = {}

for col in df.select_dtypes(include=np.number).columns:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
    
    outliers_dict[col] = len(outliers)
    print(f"{col}: {len(outliers)} outliers")

# -----------------------------
# 4. HANDLE OUTLIERS
# -----------------------------
# Option: Cap (Winsorization)
for col in df.select_dtypes(include=np.number).columns:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    df[col] = np.where(df[col] < lower_bound, lower_bound,
                       np.where(df[col] > upper_bound, upper_bound, df[col]))

print("\n===== DATA AFTER OUTLIER HANDLING =====")
print(df.describe())
plt.figure()
plt.bar(outliers_dict.keys(), outliers_dict.values())
plt.title("Outliers per Column")
plt.xlabel("Columns")
plt.ylabel("Number of Outliers")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Save cleaned dataset
df.to_csv("cleaned_dataset.csv", index=False)