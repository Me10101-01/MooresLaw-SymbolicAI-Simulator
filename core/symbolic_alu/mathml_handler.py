import sympy as sp
from sympy.printing.mathml import mathml

def safe_mathml(expr, printer='presentation'):
    mathml_str = mathml(expr, printer=printer)
    if not isinstance(mathml_str, str):
        raise TypeError("Expected str from mathml")
    return mathml_str  # Already a string; no .toxml() needed
