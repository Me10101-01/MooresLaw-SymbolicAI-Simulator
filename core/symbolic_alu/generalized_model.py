import sympy as sp

def generalize_simulation(base_formula, params, domain='growth'):
    t, r, N0 = sp.symbols('t r N0')
    if domain == 'growth':
        formula = N0 * sp.exp(r * t)
    elif domain == 'decay':
        formula = N0 * sp.exp(-r * t)
    else:
        formula = base_formula
    generalized = formula.subs(params)
    return sp.lambdify(t, generalized, 'numpy')
