import matplotlib.pyplot as plt
import numpy as np
import time

plt.ion() # Turn on interactive mode

for i in range(50):
    plt.clf() # Clear current figure
    data = np.random.random(1000)
    plt.hist(data, bins=30) # 'bi no' corrected to 'bins'
    plt.draw()
    plt.pause(0.1) # Pause to see the update

plt.ioff() # Turn off interactive mode
plt.show()