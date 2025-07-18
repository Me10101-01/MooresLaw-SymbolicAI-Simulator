import os
import socket
import requests
from pathlib import Path
import subprocess

def is_port_open(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('localhost', port)) == 0

def check_ngrok_installed():
    print("🔍 Checking if ngrok is installed...")
    result = subprocess.run(['which', 'ngrok'], capture_output=True, text=True)
    if result.stdout.strip():
        print("✅ ngrok is installed.")
        return True
    else:
        print("❌ ngrok is NOT installed.")
        return False

def check_ngrok_config():
    config_path = Path.home() / ".config" / "ngrok" / "ngrok.yml"
    if config_path.exists():
        with open(config_path) as f:
            content = f.read()
        if "authtoken" in content and "version:" in content:
            print("✅ ngrok config looks valid.")
            return True
        else:
            print("⚠️ ngrok config exists but may be missing version or authtoken.")
    else:
        print("❌ ngrok config file not found.")
    return False

def check_ngrok_tunnel():
    try:
        response = requests.get("http://localhost:4040/api/tunnels")
        tunnels = response.json().get("tunnels", [])
        if not tunnels:
            print("⚠️ No active ngrok tunnels found.")
            return None
        for t in tunnels:
            if "https" in t["public_url"]:
                print(f"🌐 Active public tunnel: {t['public_url']}")
                return t["public_url"]
    except Exception as e:
        print("❌ Could not connect to ngrok API (is it running?)")
    return None

def main():
    print("🚀 Running full diagnostic...\n")

    ngrok_ok = check_ngrok_installed()
    config_ok = check_ngrok_config()

    streamlit_ok = is_port_open(8501)
    if streamlit_ok:
        print("✅ Streamlit app is running on port 8501.")
    else:
        print("❌ Streamlit app is NOT running on port 8501.")

    tunnel_url = check_ngrok_tunnel()
    if tunnel_url:
        print(f"\n✅ Your app is LIVE at: {tunnel_url}")
    else:
        print("\n❌ App is not exposed publicly via ngrok.")

    print("\n📦 Done.")

if __name__ == "__main__":
    main()
