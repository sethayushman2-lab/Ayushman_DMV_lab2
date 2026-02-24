import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
fig, ax = plt.subplots()
ax.axis([0, 10, -1, 1]) 
line, = ax.plot([], [], color='k')
def init():
    """Initializes the background for the animation."""
    line.set_data([], [])
    return line,
def animate(i):
    """
    Updates the line data for each frame.
    'i' is the current frame number, automatically passed by FuncAnimation.
    """
    x = np.linspace(0, 10, 100)
    y = np.sin(x + i * 0.1) 
    line.set_data(x[:i], y[:i]) 
    return line,
ani = animation.FuncAnimation(
    fig,                 
    animate,                 
    init_func=init,      
    frames=100,          
    interval=50,         
    blit=True            
)
plt.show()