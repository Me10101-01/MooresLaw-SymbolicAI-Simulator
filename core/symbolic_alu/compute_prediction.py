import sympy as sp

def moores_law_prediction(baseline, doublings):
    N0, exp = sp.symbols('N0 exp')
    formula = N0 * (2 ** exp)
    result = formula.subs({N0: baseline, exp: doublings})
    return sp.N(result)  # Numerical evaluation
