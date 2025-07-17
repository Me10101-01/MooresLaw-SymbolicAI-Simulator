import torch
from core.symbolic_alu.compute_prediction import moores_law_prediction

def simulate_predictions(baseline, years=26, period=2):
    doublings = years / period
    # Neural tick clock for cycles
    ticks = torch.sin(torch.linspace(0, 2 * torch.pi * doublings, int(doublings) + 1))
    prediction = moores_law_prediction(baseline, doublings)
    # Swarm bot chaos: Perturb with sin wave
    chaos = torch.sin(torch.rand(1) * 2 * torch.pi) * 0.1  # 10% variance
    return prediction * (1 + chaos.item())

# Example: print(simulate_predictions(2600000000))
