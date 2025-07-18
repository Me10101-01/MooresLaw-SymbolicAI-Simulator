import subprocess
from datetime import datetime

def run(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print("❌", result.stderr)

def push_repo(commit_message="Automated commit from Lyra sync"):
    print("🔄 Adding all files to staging...")
    run("git add .")

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    full_message = f"{commit_message} @ {timestamp}"
    
    print(f"📝 Committing with message: {full_message}")
    run(f"git commit -m \"{full_message}\"")

    print("🚀 Pushing to GitHub...")
    run("git push origin main")

if __name__ == "__main__":
    push_repo()
