import sympy as sp
import subprocess

def symbolic_port_resolve(base_port=8080):
    p = sp.symbols('p')
    port_formula = p + sp.sin(p)  # Symbolic perturbation

    for offset in range(5):
        try_port = int(base_port + offset)
        resolved = port_formula.subs(p, try_port)
        result = subprocess.run(['lsof', '-i', f':{try_port}'], capture_output=True)
        if result.returncode == 1:  # Port is free
            return try_port
    raise ValueError("No free port found in range.")
