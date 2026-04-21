import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# 1. Load the dataset (Fixed filename here)
df = pd.read_csv('new dataset.csv')

# 2. Find the headquarters of 10 companiespython 
hq_10 = df[['name', 'hq']].head(10)
print("--- Top 10 Company Headquarters ---")
print(hq_10)

# ---------------------------------------------------------
# 3. Bar Chart: Top 10 Companies by Rating
# ---------------------------------------------------------
df_rating = df.sort_values(by='ratings', ascending=False).head(10)

plt.figure(figsize=(10, 6))
plt.bar(df_rating['name'], df_rating['ratings'], color='skyblue')
plt.title('Top 10 Companies by Rating')
plt.xlabel('Company')
plt.ylabel('Rating')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# ---------------------------------------------------------
# 4. Funnel Chart: Top 10 Companies by Review Count
# ---------------------------------------------------------
# Clean the 'review_count' column strings to actual numbers
def clean_review(x):
    if pd.isna(x): return 0
    x = str(x).replace('(', '').replace(')', '').replace(' Reviews', '').strip()
    if 'k' in x.lower():
        return float(x.lower().replace('k', '')) * 1000
    return float(x)

df['review_num'] = df['review_count'].apply(clean_review)
df_review = df.sort_values(by='review_num', ascending=False).head(10)

# Plotly is the best library for drawing Funnel charts
fig = px.funnel(df_review, x='review_num', y='name', title='Top 10 Companies by Review Count')
fig.show()

# ---------------------------------------------------------
# 5. Line Chart: Top 10 Companies by Employee Count
# ---------------------------------------------------------
# Clean 'employees' strings by converting them to estimated numbers
def clean_emp(x):
    x = str(x).lower()
    if '1 lakh+' in x: return 100000
    elif '50k-1 lakh' in x: return 75000
    elif '10k-50k' in x: return 30000
    elif '5k-10k' in x: return 7500
    elif '1k-5k' in x: return 3000
    elif '500-1k' in x: return 750
    return 0

df['emp_num'] = df['employees'].apply(clean_emp)
df_emp = df.sort_values(by='emp_num', ascending=False).head(10)

plt.figure(figsize=(10, 6))
plt.plot(df_emp['name'], df_emp['emp_num'], marker='o', linestyle='-', color='purple')
plt.title('Top 10 Companies by Employee Count (Estimated)')
plt.xlabel('Company')
plt.ylabel('Estimated Employee Count')
plt.xticks(rotation=45, ha='right')
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# ---------------------------------------------------------
# 6. Pie Chart: Top 10 Companies by Rating
# ---------------------------------------------------------

df_pie = df.sort_values(by='ratings', ascending=False).head(10)

plt.figure(figsize=(8, 8))
plt.pie(
    df_pie['ratings'],
    labels=df_pie['name'],
    autopct='%1.1f%%',
    startangle=140,
    colors=plt.cm.Paired.colors
)

plt.title('Top 10 Companies by Rating (Pie Chart)')
plt.tight_layout()
plt.show()