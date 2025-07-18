from pathlib import Path

app_code = """
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
"""

app_path = Path("app.py")
app_path.write_text(app_code.strip() + "\n")

print("✅ app.py has been restored successfully.")

restart = input("🔁 Restart Docker container? (y/n): ").strip().lower()
if restart == 'y':
    import subprocess
    subprocess.run(["docker", "stop", "epic_pascal"], stderr=subprocess.DEVNULL)
    subprocess.run(["docker", "rm", "epic_pascal"], stderr=subprocess.DEVNULL)
    subprocess.run(["docker", "build", "-t", "moore-visualizer", "."], check=True)
    subprocess.run(["docker", "run", "-p", "8501:8501", "moore-visualizer"])
    print("🚀 Docker container restarted.")
else:
    print("🧘 No restart performed. You're ready to run it when you want.")
