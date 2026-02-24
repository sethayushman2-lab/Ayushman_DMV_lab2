import matplotlib.pyplot as plt

plt.subplot(1, 2, 1) 
plt.plot([1, 2, 3], [10, 20, 10])
plt.title("Line Chart")

plt.subplot(1, 2, 2) 
plt.scatter([1, 2, 3], [10, 20, 10], color='red')
plt.title("Scatter Plot")

plt.tight_layout()
plt.show()