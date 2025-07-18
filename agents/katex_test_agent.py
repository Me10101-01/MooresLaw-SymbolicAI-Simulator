import subprocess
from pathlib import Path

def check_katex_installed():
    try:
        subprocess.run(["npx", "katex", "--version"], capture_output=True, check=True)
        return True
    except Exception:
        return False

def find_math_files():
    tex_files = list(Path("outputs").rglob("*.tex"))
    xml_files = list(Path("outputs").rglob("*.xml"))
    return tex_files + xml_files

def convert_with_katex(file_path, output_path):
    try:
        subprocess.run([
            "npx", "katex",
            "--input", str(file_path),
            "--output", str(output_path)
        ], check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ KaTeX error: {e}")
        return False

def main():
    print("🔍 Running KaTeX rendering test...")

    if not check_katex_installed():
        print("❌ KaTeX is not installed. Run: npm install -g katex")
        return

    math_files = find_math_files()
    if not math_files:
        print("❌ No .tex or .xml math files found in /outputs")
        return

    output_html = Path("outputs/katex_rendered.html")
    if convert_with_katex(math_files[0], output_html):
        print(f"✅ Rendered successfully: {output_html}")
    else:
        print("❌ Rendering failed.")

if __name__ == "__main__":
    main()
