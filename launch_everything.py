import os
import subprocess
import time
import requests
from pathlib import Path
from datetime import datetime

def build_docker_image():
    print("🔨 Building Docker image...")
    subprocess.run(["docker", "build", "-t", "moore-visualizer", "."], check=True)

def run_docker_container():
    print("🐳 Starting Docker container...")
    subprocess.Popen(["docker", "run", "-p", "8501:8501", "moore-visualizer"])

def start_ngrok():
    print("🌐 Launching ngrok tunnel...")
    subprocess.Popen(["ngrok", "http", "8501"])
    time.sleep(5)  # Wait for ngrok to initialize

def get_public_url():
    try:
        r = requests.get("http://localhost:4040/api/tunnels")
        tunnels = r.json().get("tunnels", [])
        for t in tunnels:
            if "https://" in t["public_url"]:
                return t["public_url"]
    except:
        return None

def update_readme(public_url):
    tag = "## 🌐 Public Access"
    readme = Path("README.md")
    content = readme.read_text() if readme.exists() else ""
    lines = content.splitlines()
    new_lines = [line for line in lines if tag not in line]
    new_lines.append(f"\n{tag}\n[Launch Visualizer]({public_url})\n")
    readme.write_text("\n".join(new_lines))
    print("📄 README.md updated with live link.")

def main():
    print("🚀 Launching Full AI Stack\n")

    # Optional: Uncomment to always rebuild
    # build_docker_image()

    run_docker_container()
    start_ngrok()

    print("⏳ Waiting for services to stabilize...\n")
    time.sleep(5)

    public_url = get_public_url()

    if public_url:
        print(f"\n✅ Your AI App is LIVE at: {public_url}\n")
        update_readme(public_url)
    else:
        print("❌ Could not retrieve ngrok public URL. Is it running?")

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("launch_log.txt", "a") as f:
        f.write(f"[{timestamp}] AI stack launched at: {public_url or 'ERROR'}\n")

    print("📦 Logged launch to launch_log.txt\n")

if __name__ == "__main__":
    main()
