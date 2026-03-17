import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("cleaned_dataset.xlsx")

# Keep only required columns
df = df[['year', 'population']]

# Convert to numeric (force errors → NaN)
df['year'] = pd.to_numeric(df['year'], errors='coerce')
df['population'] = pd.to_numeric(df['population'], errors='coerce')

# Drop invalid rows
df = df.dropna()

# Sort values
df = df.sort_values(by='year')

# Plot step chart
plt.figure()
plt.step(df['year'], df['population'])

plt.title("Population Growth Over Time")
plt.xlabel("Year")
plt.ylabel("Population")

plt.show()