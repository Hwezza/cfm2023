import Main

import numpy as np
import matplotlib.pyplot as plt

'''
# Create some data for the x, y, and z axis
x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
z = x**2 + y**2

# Create the 3D plot
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot3D(x, y, z, 'red')

# Show the plot
plt.show()
'''

#2d graphing

'''
# importing libraries
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

# defining surface and axes
x = np.outer(np.linspace(-2, 2, 10), np.ones(10))
y = x.copy().T
z = np.cos(x ** 2 + y ** 3)

fig = plt.figure()

# syntax for 3-D plotting
ax = plt.axes(projection ='3d')

# syntax for plotting
ax.plot_surface(x, y, z, cmap ='viridis', edgecolor ='green')
ax.set_title('Surface plot geeks for geeks')
plt.show()
'''