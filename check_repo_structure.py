import os

# Define expected structure
expected_structure = {
    "core/symbolic_alu": ["compute_prediction.py"],
    "core/control_unit": ["simulation.py"],
    "core/entanglement_core": ["map_baselines.py"],
    "core/register_memory": [],
    "agents/scaffolding": ["prediction_agent.py", "graph_ui_agent.py"],
    "swarm/strategickhaos_bots": [],
    ".": ["main.py", "app.py", "generate_graph.py", "baselines.json", "requirements.txt", "README.md"]
}

def check_structure():
    print("🔍 Checking repository structure...\n")
    for folder, files in expected_structure.items():
        folder_exists = os.path.isdir(folder)
        print(f"{'✅' if folder_exists else '❌'} Directory: {folder}")
        for file in files:
            path = os.path.join(folder, file)
            exists = os.path.isfile(path)
            print(f"   {'📄' if exists else '⚠️'} {file}")
        print()

if __name__ == "__main__":
    check_structure()
