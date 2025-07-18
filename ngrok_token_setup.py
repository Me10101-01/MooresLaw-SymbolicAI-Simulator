import os
import subprocess
from pathlib import Path

CONFIG_PATH = Path.home() / ".config" / "ngrok"
CONFIG_FILE = CONFIG_PATH / "ngrok.yml"

def write_token_to_config(token):
    CONFIG_PATH.mkdir(parents=True, exist_ok=True)
    with open(CONFIG_FILE, "w") as f:
        f.write(f"authtoken: {token.strip()}\n")
    print(f"\n✅ Token saved to {CONFIG_FILE}")

def validate_ngrok():
    print("🚀 Testing ngrok with a dry run (port 9999)...")
    try:
        subprocess.run(["ngrok", "http", "9999"], check=True)
    except subprocess.CalledProcessError:
        print("⚠️ ngrok ran but failed — likely because no service is listening on port 9999.")
    except FileNotFoundError:
        print("❌ ngrok is not installed. Please install it first.")
    finally:
        print("🎯 If you see a 'Forwarding' URL, you're good to go!")

def main():
    print("🧠 NGROK SETUP TOOL")
    if CONFIG_FILE.exists():
        with open(CONFIG_FILE) as f:
            print(f"📄 Existing config:\n{f.read()}")
        use_existing = input("Do you want to keep this token? (y/n): ").lower()
        if use_existing == 'y':
            print("👍 Using existing token.")
            return
        else:
            print("🔄 Replacing token...")
    
    token = input("🔐 Enter your ngrok Authtoken: ")
    write_token_to_config(token)
    validate_ngrok()

if __name__ == "__main__":
    main()
