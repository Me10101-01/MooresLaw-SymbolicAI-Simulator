from core.symbolic_alu.compute_prediction import moores_law_prediction

def run_simulation(baseline, years=26, period=2):
    doublings = years / period
    return moores_law_prediction(baseline, doublings)
