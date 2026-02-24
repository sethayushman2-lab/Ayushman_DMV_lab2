import numpy as np
import matplotlib.pyplot as plt

x_data = np.array([1, 2, 3, 4])
y_data = np.array([2, 3, 5, 7])

plt.plot(x_data, y_data)
plt.title("Simple X vs Y Plot")
plt.xlabel("X Axis Label")
plt.ylabel("Y Axis Label")
plt.grid(True)
plt.show()