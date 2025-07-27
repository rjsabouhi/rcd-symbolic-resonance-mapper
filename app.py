
import streamlit as st
import numpy as np
import plotly.express as px

st.set_page_config(page_title="Symbolic Resonance Mapper", layout="wide")
st.title("🔮 Symbolic Resonance Mapper")

st.markdown("""
This tool visualizes symbolic resonance patterns across dynamic systems of identity and influence.
It maps out recursive alignment fields and perturbations using configurable symbolic gradient controls.
""")

# Sidebar controls
st.sidebar.header("Resonance Controls")
frequency = st.sidebar.slider("Base Resonance Frequency", 0.1, 5.0, 1.0)
amplitude = st.sidebar.slider("Amplitude Modifier", 0.1, 3.0, 1.0)
noise = st.sidebar.slider("Symbolic Noise Level", 0.0, 1.0, 0.2)

# Simulate resonance pattern
x = np.linspace(0, 10, 500)
y = amplitude * np.sin(frequency * x) + np.random.normal(0, noise, len(x))
data = {'x': x, 'Resonance': y}

# Plot
fig = px.line(data, x='x', y='Resonance', title="Symbolic Resonance Pattern")
st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
st.markdown("Use this pattern map to explore alignment coherence and symbolic interference.")
