import torch
from core.entanglement_core.map_plugins import load_and_entangle_plugins, tag_branch_from_model
from core.control_unit.general_simulation import run_general_sim
from agents.llm_evolution_agent import evolve_llm
import numpy as np

def phase6_evolve(domain='economic_growth', formula=None, params=None):
    print(f"🧠 Phase 6: Evolving simulation for domain: {domain}")
    
    # Load all plugin metadata into entangled graph
    G = load_and_entangle_plugins()

    # Run symbolic simulation
    results = run_general_sim(formula, params, cycles=10)
    
    # Strategickhaos perturbation
    chaos = torch.randn(len(results)) * 0.05
    perturbed = np.array(results) + chaos.numpy()

    # Auto-tag branch based on entangled domain
    tag = tag_branch_from_model(G, 'phase6')
    print(f"🔖 Proposed Git branch tag: {tag}")

    # Trigger LLM refactor if drift is high
    drift_score = np.std(chaos.numpy())
    print(f"📉 Chaos drift score: {drift_score:.4f}")
    if drift_score > 0.02:
        evolve_llm(trigger_score=0.4, code_path='app.py', task='refactor')
    
    # Log for visibility
    print(f"✅ Evolved outputs:\n{perturbed.tolist()}")
    return perturbed.tolist(), tag
