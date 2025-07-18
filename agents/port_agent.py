import torch
import subprocess

def fix_port_conflict(port=8080):
    ticks = torch.sin(torch.tensor(range(3)))
    for tick in ticks:
        pid = subprocess.run(['lsof', '-t', f':{port}'], capture_output=True).stdout.decode().strip()
        if pid and tick > 0:
            subprocess.run(['kill', '-9', pid])
            return f"🧹 Port {port} cleared (PID {pid})"
    return "❗ Manual intervention required"
