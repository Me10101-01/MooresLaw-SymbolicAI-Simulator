import sympy as sp
from pathlib import Path
from core.symbolic_alu.mathml_handler import safe_mathml

student_data = {
    "student_name": "Domenic Garza",
    "year_start": 1972,
    "transistors_start": 4000,
    "target_year": 2040,
    "transistors_2014": 5.56e9,
    "doubling_period": 2,
    "discussion_context": "Using Moore's Law to predict exponential growth in transistor count",
    "question": "Estimate the number of transistors per IC in 2040 using a 2014 baseline of 5.56 billion, assuming doubling every 2 years."
}

def compute_prediction(N0, start, end, period):
    t = end - start
    doublings = t / period
    return N0 * 2 ** doublings

def generate_mathml_expr(N0, start, end, period):
    t = sp.symbols('t')
    expr = N0 * 2 ** (t / period)
    return safe_mathml(expr.subs(t, end - start))  # Return string

def generate_response(data):
    predicted = compute_prediction(
        data["transistors_2014"],
        2014,
        data["target_year"],
        data["doubling_period"]
    )
    return f"""
**Student:** {data['student_name']}
**Year Start:** 2014
**Target Year:** {data['target_year']}
**Doubling Period:** {data['doubling_period']} years
**Initial Transistors:** {data['transistors_2014']:,}

Using Moore’s Law:  
N(t) = N₀ × 2^(t / {data['doubling_period']})  
N(2040) = {data['transistors_2014']:,} × 2^({data['target_year'] - 2014}/{data['doubling_period']})  
→ ≈ {predicted:,.0f} transistors

**Conclusion:** Based on Moore’s Law, the estimated number of transistors per IC in 2040 is approximately {predicted/1e12:.2f} trillion.
"""

def write_outputs():
    response = generate_response(student_data)
    mathml_code = generate_mathml_expr(
        sp.Float(student_data["transistors_2014"]),
        2014,
        student_data["target_year"],
        student_data["doubling_period"]
    )

    Path("outputs").mkdir(exist_ok=True)
    with open("outputs/discussion_ai_response.txt", "w") as f:
        f.write(response)
    with open("outputs/discussion_equation_mathml.xml", "w") as f:
        f.write(mathml_code)

    print("✅ AI discussion reply and MathML saved in /outputs")

if __name__ == "__main__":
    write_outputs()
