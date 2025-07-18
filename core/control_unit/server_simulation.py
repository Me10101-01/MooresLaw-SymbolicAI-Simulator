import os
import torch
import uvicorn
from core.symbolic_alu.port_resolver import symbolic_port_resolve

def start_server(app, host="0.0.0.0"):
    ticks = torch.sin(torch.linspace(0, 2 * torch.pi, 3))  # Neural tick clock

    for tick in ticks:
        try:
            port = symbolic_port_resolve()
            os.environ['API_PORT'] = str(port)
            print(f"🚀 Launching on port {port}")
            uvicorn.run(app, host=host, port=port)
            return f"✅ Server on port {port}"
        except OSError as e:
            if 'address already in use' in str(e) and tick > 0:
                subprocess.run(['fuser', '-k', f'{port}/tcp'])
                continue
    return "❌ Escalate to symbolic agent"
