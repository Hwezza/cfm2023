#import Main

import numpy as np
import matplotlib.pyplot as plt

# Create some data for the x, y, and z axis
x = np.linspace(-5, 10, 100)
y = np.linspace(-10, 10, 100)
z = x**2 + y**2

# Create the 3D plot
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot3D(x, y, z, 'red')

# Show the plot
plt.show()
