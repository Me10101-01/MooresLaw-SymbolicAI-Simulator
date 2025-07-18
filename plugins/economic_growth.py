import sympy as sp

domain = 'economic_growth'
formula = sp.symbols('N0') * sp.exp(sp.symbols('r') * sp.symbols('t'))
params = {'r': 0.03, 'N0': 1000}
