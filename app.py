import streamlit as st
import json
from core.control_unit.simulation import run_simulation
from generate_graph import generate_graph_plotly

st.set_page_config(page_title="Moore's Law Visualizer", layout="centered")

st.title("📈 Moore’s Law Symbolic AI Visualizer")
st.write("Select a 2014 transistor baseline and see Moore’s Law predictions up to 2040.")

# Load baseline values
with open("baselines.json", "r") as f:
    baselines = json.load(f)['baselines']

selected = st.selectbox("Select 2014 Baseline", [b['label'] for b in baselines])
base_value = next(b['value'] for b in baselines if b['label'] == selected)

log_scale = st.checkbox("Logarithmic Y-Axis")

prediction = run_simulation(base_value)
fig = generate_graph_plotly(base_value, prediction, log_scale)

st.plotly_chart(fig)
st.success(f"📊 Projected transistor count in 2040: {prediction:,.0f}")
