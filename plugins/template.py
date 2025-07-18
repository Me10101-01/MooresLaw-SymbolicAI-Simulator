import sympy as sp

# Metadata
domain = 'economic_growth'
params = {'r': 0.03, 'N0': 1000}

# Symbolic formula definition
t = sp.symbols('t')
N0 = sp.symbols('N0')
r = sp.symbols('r')
formula = N0 * sp.exp(r * t)  # Exponential growth

# Optional: Add a simulate() function for plugin-based execution
def simulate(custom_params=None):
    if custom_params:
        use_params = {**params, **custom_params}
    else:
        use_params = params
    generalized = formula.subs(use_params)
    f = sp.lambdify(t, generalized, 'numpy')
    return f
