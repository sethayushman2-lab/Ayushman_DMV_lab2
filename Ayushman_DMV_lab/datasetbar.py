import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("popolazione-globale-per-paese-1950-2024.csv.xlsx")

# Remove unwanted columns
df = df[['country', 'population']]

# Take first 10 rows (for better visualization)
df = df.head(10)

plt.figure()
plt.bar(df['country'], df['population'])

plt.title("Population by Country")
plt.xlabel("Country")
plt.ylabel("Population")

plt.xticks(rotation=45)
plt.show()