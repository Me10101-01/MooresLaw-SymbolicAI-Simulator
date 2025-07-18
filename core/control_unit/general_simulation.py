import torch
from core.symbolic_alu.generalized_model import generalize_simulation

def run_general_sim(formula, params, cycles=20):
    ticks = torch.sin(torch.linspace(0, 2 * torch.pi, cycles))
    model = generalize_simulation(formula, params)
    outputs = [model(tick.item()) for tick in ticks]
    return outputs
