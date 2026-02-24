import matplotlib.pyplot as plt
import numpy as np
categories=['Apples', 'Bananas', 'Cherries', 'Dates']
sales=[400, 350, 300, 450]
plt.bar(categories, sales)
plt.xlabel('Fruits')
plt.ylabel('Sales')
plt.title('Fruit Sales data')
plt.show()