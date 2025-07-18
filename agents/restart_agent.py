import subprocess
from agents.port_agent import fix_port_conflict

def restart_api():
    print(fix_port_conflict(8080))
    subprocess.Popen(['PYTHONPATH=.', 'python', 'agents/cloud_agent.py'])
    return "🔁 FastAPI restarted on port 8080"
