import streamlit as st
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio

# Set the Plotly renderer for Streamlit
pio.renderers.default = "browser"


def plot_parametric_surface(x_eq, y_eq, z_eq, u_range, v_range):
    """Generates and displays an interactive 3D plot from user-defined equations."""

    # Define the parameter space using the user's constraints
    try:
        u = np.linspace(u_range[0], u_range[1], 100)
        v = np.linspace(v_range[0], v_range[1], 100)
        U, V = np.meshgrid(u, v)

        # Safely evaluate the user-provided equations
        # WARNING: Using eval() can be a security risk with untrusted input.
        # For a more robust app, a safer math parser like SymPy would be used.
        X = eval(x_eq)
        Y = eval(y_eq)
        Z = eval(z_eq)

        # Create the Plotly figure
        fig = go.Figure(data=[go.Surface(z=Z, x=X, y=Y, colorscale='Viridis')])

        # Update the layout for a clean, interactive view
        fig.update_layout(
            title='Interactive Parametric 3D Plot',
            autosize=True,
            scene=dict(
                xaxis_title='X-axis',
                yaxis_title='Y-axis',
                zaxis_title='Z-axis',
            )
        )

        # Display the plot in the Streamlit app
        st.plotly_chart(fig, use_container_width=True)

    except Exception as e:
        st.error(f"Error plotting the equation: {e}")


# --- Streamlit UI ---
st.title("Dynamic 3D Parametric Grapher 🚀")

st.markdown("""
Enter your 3D parametric equations below. Use `u` and `v` as variables.
You can use standard NumPy functions like `np.cos`, `np.sin`, `np.pi`, etc.
""")

col1, col2 = st.columns(2)

with col1:
    x_eq = st.text_input("X Equation", value="-(4 - 2 * np.cos(u)) * np.cos(v) + 6 * (np.sin(u) + 1) * np.cos(u)")
    y_eq = st.text_input("Y Equation", value="16 * np.sin(u)")
    z_eq = st.text_input("Z Equation", value="(4 - 2 * np.cos(u)) * np.sin(v)")

with col2:
    st.markdown("### Constraints")
    u_min, u_max = st.slider("u range", min_value=0.0, max_value=2 * np.pi, value=(0.0, 2 * np.pi))
    v_min, v_max = st.slider("v range", min_value=0.0, max_value=2 * np.pi, value=(0.0, 2 * np.pi))

if st.button("Plot Graph"):
    plot_parametric_surface(x_eq, y_eq, z_eq, (u_min, u_max), (v_min, v_max))