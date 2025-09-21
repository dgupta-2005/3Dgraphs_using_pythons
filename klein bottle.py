import numpy as np

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 1. Define the parameter space
# We create a grid for u and v values from 0 to 2pi
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, 2 * np.pi, 100)

U, V = np.meshgrid(u, v)

# 2. Define the Klein bottle equations
# Note: Python's np.cos and np.sin work on entire arrays
X = -(4 - 2 * np.cos(U)) * np.cos(V) + 6 * (np.sin(U) + 1) * np.cos(U)
Y = 16 * np.sin(U)
Z = (4 - 2 * np.cos(U)) * np.sin(V)

# 3. Create the 3D plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the surface
ax.plot_surface(X, Y, Z, cmap='viridis', rstride=1, cstride=1, antialiased=False)

# Optional: Add labels and title for clarity
ax.set_title('Klein Bottle')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.view_init(elev=20, azim=45) # Adjust the viewing angle

plt.show()