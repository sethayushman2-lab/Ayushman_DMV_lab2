import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("cleaned_dataset.xlsx")

df = df[['country', 'population']]
df = df.head(5)  # Pie chart works best with few values

plt.figure()
plt.pie(df['population'], labels=df['country'], autopct='%1.1f%%')

plt.title("Population Distribution")
plt.show()