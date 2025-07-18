import os
import socket
import subprocess
import requests
from datetime import datetime
from pathlib import Path

def check_docker_running():
    print("🐳 Checking Docker container...")
    try:
        result = subprocess.run(["docker", "ps"], capture_output=True, text=True)
        if "moore-visualizer" in result.stdout:
            print("✅ Docker container is running: moore-visualizer")
            return True
        else:
            print("❌ Docker container 'moore-visualizer' not found.")
            return False
    except FileNotFoundError:
        print("❌ Docker not found.")
        return False

def is_port_open(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('localhost', port)) == 0

def check_streamlit():
    print("📊 Checking Streamlit on port 8501...")
    if is_port_open(8501):
        print("✅ Streamlit app is running.")
        return True
    else:
        print("❌ Streamlit is not running on port 8501.")
        return False

def check_ngrok_tunnel():
    print("🌐 Checking ngrok tunnel status...")
    try:
        r = requests.get("http://localhost:4040/api/tunnels")
        tunnels = r.json().get("tunnels", [])
        if not tunnels:
            print("⚠️ No active tunnels found.")
            return None
        for t in tunnels:
            if "https://" in t["public_url"]:
                print(f"✅ ngrok is live: {t['public_url']}")
                return t["public_url"]
    except requests.exceptions.ConnectionError:
        print("❌ ngrok not running or API inaccessible.")
    return None

def log_status(ngrok_url):
    log_path = Path("verify_log.txt")
    with open(log_path, "a") as f:
        f.write(f"\n=== Verification Run: {datetime.now()} ===\n")
        f.write(f"Docker: {'Yes' if check_docker_running() else 'No'}\n")
        f.write(f"Streamlit: {'Yes' if check_streamlit() else 'No'}\n")
        f.write(f"ngrok URL: {ngrok_url or 'None'}\n")
        f.write("-" * 40 + "\n")
    print(f"📁 Log saved to {log_path.absolute()}")

def main():
    print("\n🧠 AI Environment Verifier\n")
    docker_ok = check_docker_running()
    streamlit_ok = check_streamlit()
    ngrok_url = check_ngrok_tunnel()

    if docker_ok and streamlit_ok and ngrok_url:
        print("\n🎉 All systems operational!")
    else:
        print("\n⚠️ One or more systems need attention.")

    log_status(ngrok_url)

if __name__ == "__main__":
    main()
