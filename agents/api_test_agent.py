import requests
import subprocess

def test_api(endpoint='http://localhost:8080/simulate/mobius', data={
    "start_year": 2014,
    "target_year": 2040,
    "initial_transistors": 5.56e9,
    "doubling_period": 2
}):
    try:
        response = requests.post(endpoint, json=data)
        output = response.json()

        if 'error' in output and 'toxml' in output['error']:
            print("❌ .toxml() error detected — triggering auto fix...")
            subprocess.run(['sed', '-i', 's/.toxml()//g', 'agents/cloud_agent.py'])
            subprocess.run(['pkill', '-f', 'uvicorn'])  # Kill old API
            subprocess.Popen(['PYTHONPATH=.', 'python', 'agents/cloud_agent.py'])
            return "🔁 Fix applied, API restarted. Re-run test in 3 seconds..."
        elif 'mathml' in output:
            return f"✅ MathML OK:\n{output['mathml']}"
        else:
            return f"⚠️ Unexpected response:\n{output}"

    except Exception as e:
        return f"❌ Exception during test: {e}"

if __name__ == "__main__":
    print(test_api())
