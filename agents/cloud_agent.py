import torch
from fastapi import FastAPI, Request
from core.entanglement_core.map_plugins import load_and_entangle_plugins
from core.control_unit.general_simulation import run_general_sim
import uvicorn

app = FastAPI()

@app.get("/")
def root():
    return {"message": "🌐 Phase 6 Symbolic Simulation Platform Online."}

@app.post("/simulate/{domain}")
async def simulate(domain: str, request: Request):
    try:
        params = await request.json()
        ticks = torch.sin(torch.tensor(range(10)))
        print(f"⏱ Tick wave: {ticks.tolist()}")

        G = load_and_entangle_plugins()
        node = next(n for n in G.nodes if G.nodes[n]['domain'] == domain)

        formula = G.nodes[node]['formula']
        outputs = run_general_sim(formula, params)

        return {
            "domain": domain,
            "params": params,
            "outputs": outputs
        }
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
