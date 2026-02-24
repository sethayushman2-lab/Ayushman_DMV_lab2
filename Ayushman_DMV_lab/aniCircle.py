import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()
ax.set_aspect('equal') 
ax.axis([0, 10, 0, 10]) 

circle = plt.Circle((5, 5), 0.5, color='blue')
ax.add_patch(circle)

def init():
    """Initializes the circle position."""
    circle.set_center((0, 5))
    return circle,

def animate(i):
    """
    Updates the circle's center for each frame.
    i goes from 0 to 100 (based on frames=100)
    """
    x = i * 0.1  
    y = 5 + np.sin(i * 0.2)
    circle.set_center((x, y))
    return circle,
ani = animation.FuncAnimation(
    fig,                 
    animate,                 
    init_func=init,      
    frames=100,          
    interval=30,         
    blit=True            
)

plt.show()