import matplotlib.pyplot as plt
import numpy as np


plt.ion()

fig, ax = plt.subplots()

for i in range(50):
    ax.clf() 
    
    x = np.random.rand(20)
    y = np.random.rand(20)
    
    ax.scatter(x, y, color='purple', alpha=0.6)
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_title(f"Dynamic Scatter Update: {i+1}")
    
    plt.draw()
    plt.pause(0.1) 
plt.ioff()
plt.show()