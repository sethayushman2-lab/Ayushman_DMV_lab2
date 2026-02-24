import matplotlib.pyplot as plt
import numpy as np
import time
plt.ion()
categories=['A', 'B', 'C', 'D', 'E']
num_categories= len(categories)
print("Displaying the dynamic bar chart for 10 iterations...")
for i in range(100):
    plt.clf()
    data= np.random.randint(1,20,size=num_categories)
    plt.bar(categories, data, color='skyblue')
    plt.title(f'Dynamic bar chart iteration{i+1}')
    plt.xlabel('Categories')
    plt.ylabel('Values')
    plt.ylim(0,25)
    plt.draw()
    plt.pause(0.5)
plt.ioff()
plt.close()