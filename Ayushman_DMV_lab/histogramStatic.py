import matplotlib.pyplot as plt

data = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6, 22, 25, 22, 15, 18, 19]

plt.hist(data, bins=5, color='skyblue', edgecolor='black')

plt.xlabel('Value Ranges')
plt.ylabel('Frequency')
plt.title('Static Histogram Example')

plt.show()