import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + '/../'))

from fastapi import FastAPI, Request
from sympy import Float
from agents.mobius_simulation_agent import compute_prediction, generate_mathml_expr

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Mobius Reply Generator API is online 💡"}

@app.post("/simulate/mobius")
async def simulate_mobius(request: Request):
    try:
        body = await request.json()
        start = body.get("start_year", 2014)
        target = body.get("target_year", 2040)
        N0 = Float(body.get("initial_transistors", 5.56e9))
        period = body.get("doubling_period", 2)

        # Compute result + symbolic MathML
        result = compute_prediction(N0, start, target, period)
        mathml_code = generate_mathml_expr(N0, start, target, period)

        return {
            "predicted_transistors": f"{result:.2e}",
            "mathml": mathml_code,
            "explanation": f"Using Moore's Law: N(t) = N₀ × 2^(t / {period})\nEstimated value in {target}: {result:,.0f} transistors"
        }
    except Exception as e:
        return {"error": str(e)}
