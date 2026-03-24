import numpy as np
import matplotlib.pyplot as plt

num_points = 50
np.random.seed(42) 
x = np.random.rand(num_points)
y = -x + np.random.normal(0, 0.1, num_points)

outlier_x = 0.2
outlier_y = 2.0
x = np.append(x, outlier_x)
y = np.append(y, outlier_y)


plt.figure(figsize=(10, 6)) 
plt.scatter(x, y, color='blue', alpha=0.7, label='Data Points') 
plt.scatter(outlier_x, outlier_y, color='red', marker='X', s=200, label='Added Outlier')

plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.title('Scatter Plot Showing Negative Correlation and Explicit Outlier')
plt.legend() 
plt.grid(True, linestyle='--', alpha=0.5) 
plt.show()