import requests
import subprocess

def evolve_llm(trigger_score, code_path, task='refactor'):
    print(f"🤖 LLM Evolution Agent Triggered: task={task}, score={trigger_score}")

    if trigger_score < 0.5:
        with open(code_path, 'r') as f:
            code = f.read()
        
        prompt = f"{task} this code based on evolution patterns:\n{code}"
        
        # Send to local LLM API (e.g., Ollama or custom server)
        response = requests.post("http://localhost:8080/llm", json={"prompt": prompt})
        result = response.json().get("output")

        if result:
            with open(code_path, 'w') as f:
                f.write(result)
            print("✅ Code successfully refactored by LLM.")

            # Auto-commit the evolved version
            subprocess.run(["git", "commit", "-am", f"LLM auto-{task}"])
            subprocess.run(["git", "push"])
            return "Evolved"

        else:
            print("⚠️ No output returned from LLM API.")
            return "No change"

    print("🛑 Evolution threshold not met. No action taken.")
    return "Skipped"
