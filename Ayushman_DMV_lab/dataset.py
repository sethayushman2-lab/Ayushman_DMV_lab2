import pandas as pd

# Load dataset
df = pd.read_excel("DATASET.xlsx")

# -----------------------------
# 1. DETECT MISSING VALUES
# -----------------------------
print("\nMissing Values in Each Column:")
print(df.isnull().sum())

print("\nTotal Missing Values:")
print(df.isnull().sum().sum())

# Optional: percentage of missing values
print("\nPercentage of Missing Values:")
print((df.isnull().sum() / len(df)) * 100)

# -----------------------------
# 2. HANDLE MISSING VALUES
# -----------------------------

# Separate numerical and categorical columns
num_cols = df.select_dtypes(include=['int64', 'float64']).columns
cat_cols = df.select_dtypes(include=['object']).columns

# Fill numerical columns with MEAN
for col in num_cols:
    df[col] = df[col].fillna(df[col].mean())

# Fill categorical columns with MODE
for col in cat_cols:
    df[col] = df[col].fillna(df[col].mode()[0])

# -----------------------------
# 3. VERIFY AGAIN
# -----------------------------
print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# -----------------------------
# 4. SAVE CLEAN DATASET
# -----------------------------
df.to_excel("cleaned_dataset.xlsx", index=False)

print("\nDataset cleaned and saved successfully!")