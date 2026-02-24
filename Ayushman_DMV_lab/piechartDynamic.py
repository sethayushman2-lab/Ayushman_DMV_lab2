import matplotlib.pyplot as plt
import numpy as np

labels = ['Team A', 'Team B', 'Team C', 'Team D']
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']

plt.ion() 
fig, ax = plt.subplots()

for i in range(30):
    ax.clear() 
    
    data = np.random.randint(10, 50, size=4) 
    
    ax.pie(data, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
    
    ax.set_title(f"Live Vote Count - Update {i+1}")
    
    ax.axis('equal') 
    
    plt.draw()
    plt.pause(0.5)

plt.ioff() 
plt.show()