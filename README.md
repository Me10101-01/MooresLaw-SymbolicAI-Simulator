# 🧠 Moore’s Law Symbolic AI Visualizer

**QuantumSymbolicAI-Emulator** is a symbolic AI simulator that models exponential growth under Moore’s Law using interactive computation and graphing.

It allows users to **toggle different 2014 transistor baselines** (e.g., 2.6B, 5.56B, 8B) and see how predictions scale to 2040 through 13 doublings. Designed to resolve discrepancies in charts like the famous **Wikipedia transistor count plot**.

---

## 📊 Example Output

| 2014 Baseline | Chip Type                        | 2040 Estimate         |
|---------------|----------------------------------|------------------------|
| 2.6B          | Intel Core i7-5960X (Consumer)   | 21.3 Trillion          |
| 5.56B         | Intel Xeon E7 v3 (Server)        | 45.55 Trillion         |
| 8B            | Hypothetical High-End            | 65.53 Trillion         |

---

## 🚀 Features

- 📈 Plotly graphs with toggleable log/linear scale
- 🧮 Symbolic math engine via SymPy
- �� Neural-inspired tick clocks (PyTorch)
- 🌐 Streamlit web app UI
- 🐳 Docker-ready
- ✅ Fully tested
- 🎓 Built for educational explanation of chart misreads

---

## 🧪 Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py

## 🌐 Public Access
[Launch Visualizer](https://4e376c216008.ngrok-free.app)
