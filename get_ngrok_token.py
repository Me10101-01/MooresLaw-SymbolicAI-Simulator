import webbrowser
import time

try:
    import pyperclip
except ImportError:
    import subprocess
    subprocess.run(["pip", "install", "pyperclip"])
    import pyperclip

def main():
    print("🧠 Launching browser to ngrok dashboard...")
    url = "https://dashboard.ngrok.com/get-started/setup"
    webbrowser.open(url)

    print("\n🪄 Please log in and copy your personal authtoken.")
    print("📋 When copied, press Enter here to continue...")
    input()

    try:
        token = pyperclip.paste()
        if not token.startswith("2") or len(token) < 10:
            raise ValueError("Clipboard doesn't contain a valid ngrok token.")
    except Exception as e:
        print(f"⚠️ Couldn't auto-detect token: {e}")
        token = input("🔐 Please paste your ngrok authtoken manually: ")

    print("\n✅ Token captured:")
    print(f"\n🔑 {token.strip()}")

    save = input("\n💾 Save this token to 'ngrok_token.txt'? (y/n): ").lower()
    if save == 'y':
        with open("ngrok_token.txt", "w") as f:
            f.write(token.strip())
        print("✅ Token saved to ngrok_token.txt")

if __name__ == "__main__":
    main()
