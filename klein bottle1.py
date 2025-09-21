import numpy as np
import plotly.graph_objects as go
import plotly.io as pio

# Set the renderer for PyCharm
pio.renderers.default = "browser"


# 1. Define the parameter space
# We create a grid for u and v values from 0 to 2pi
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, 2 * np.pi, 100)
U, V = np.meshgrid(u, v)

# 2. Define the Klein bottle equations
X = -(4 - 2 * np.cos(U)) * np.cos(V) + 6 * (np.sin(U) + 1) * np.cos(U)
Y = 16 * np.sin(U)
Z = (4 - 2 * np.cos(U)) * np.sin(V)

# 3. Create the 3D plot with Plotly
fig = go.Figure(data=[go.Surface(z=Z, x=X, y=Y, colorscale='Viridis')])

# Optional: Add labels and title for clarity
fig.update_layout(
    title='Interactive Klein Bottle',
    autosize=True,
    scene=dict(
        xaxis_title='X-axis',
        yaxis_title='Y-axis',
        zaxis_title='Z-axis',
        camera_eye=dict(x=1.8, y=1.8, z=0.8) # Adjust initial camera view
    ),
    width=800,
    height=800
)

fig.show()