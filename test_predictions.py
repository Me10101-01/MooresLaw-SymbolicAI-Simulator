from core.control_unit.simulation import run_simulation
import json

def test_all_baselines():
    with open("baselines.json") as f:
        baselines = json.load(f)['baselines']
    for b in baselines:
        prediction = run_simulation(b['value'])
        print(f"{b['label']}: {prediction:,.0f} transistors in 2040")

if __name__ == "__main__":
    test_all_baselines()
