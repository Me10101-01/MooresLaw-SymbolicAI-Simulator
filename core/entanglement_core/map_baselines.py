import json
import networkx as nx
import mpmath

def load_baselines():
    with open('baselines.json', 'r') as f:
        return json.load(f)['baselines']

def entangle_baselines(baselines):
    G = nx.Graph()
    for base in baselines:
        G.add_node(base['label'], value=base['value'])
    # Simulate interference with trig waves
    for i in range(len(baselines)):
        for j in range(i + 1, len(baselines)):
            diff = abs(baselines[i]['value'] - baselines[j]['value'])
            wave_inter = mpmath.sin(mpmath.pi * (diff / 1e9))  # Normalize to billions
            G.add_edge(baselines[i]['label'], baselines[j]['label'], weight=float(wave_inter))
    return G

# Example use:
# G = entangle_baselines(load_baselines())
# print(G.edges(data=True))
