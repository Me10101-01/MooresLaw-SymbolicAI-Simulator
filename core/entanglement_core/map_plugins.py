import networkx as nx
import mpmath
import os
import importlib.util

def load_and_entangle_plugins(plugin_dir='plugins/'):
    G = nx.Graph()
    for file in os.listdir(plugin_dir):
        if file.endswith('.py'):
            spec = importlib.util.spec_from_file_location(file[:-3], os.path.join(plugin_dir, file))
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            G.add_node(file, formula=module.formula, domain=module.domain, params=module.params)
    
    nodes = list(G.nodes())
    for i in range(len(nodes)):
        for j in range(i+1, len(nodes)):
            param_diff = len(set(G.nodes[nodes[i]]['params']) ^ set(G.nodes[nodes[j]]['params']))
            wave = mpmath.sin(mpmath.pi * param_diff)
            G.add_edge(nodes[i], nodes[j], weight=float(wave))
    
    return G

def tag_branch_from_model(G, branch_name):
    domain = max(G.nodes(data='domain'), key=lambda n: G.degree(n))
    return f"{branch_name}-{domain}"
