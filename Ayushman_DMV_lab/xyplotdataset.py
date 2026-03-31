import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = "popolazione-globale-per-paese-1950-2024.csv.xlsx"
df = pd.read_excel(file_path)

# Remove unnecessary columns (optional but cleaner)
df = df[['country', 'year', 'population']]

# Choose countries to plot
countries = ["India", "China", "United States", "Indonesia"]

# Create figure
fig, ax = plt.subplots()

# Plot data for each country
for country in countries:
    country_data = df[df['country'] == country]
    ax.plot(country_data['year'], country_data['population'], label=country)

# Labels and title
ax.set_xlabel('Year')
ax.set_ylabel('Population')
ax.set_title('Population Growth Over Years')

# Legend
ax.legend()

# Show graph
plt.show()