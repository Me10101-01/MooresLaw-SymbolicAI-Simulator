import importlib
import subprocess
import requests
import os
from pathlib import Path

def check_imports():
    modules = [
        'core.symbolic_alu.mathml_handler',
        'core.symbolic_alu.generalized_model',
        'core.control_unit.general_simulation',
        'agents.mobius_simulation_agent'
    ]
    print("📦 Importing modules...")
    for mod in modules:
        try:
            importlib.import_module(mod)
            print(f"✅ {mod} imported successfully")
        except Exception as e:
            print(f"❌ Failed to import {mod}: {e}")

def test_fastapi_endpoint():
    print("\n🌐 Testing FastAPI endpoint /simulate/mobius ...")
    try:
        res = requests.post("http://localhost:8080/simulate/mobius", json={
            "start_year": 2014,
            "target_year": 2040,
            "initial_transistors": 5.56e9,
            "doubling_period": 2
        }, timeout=5)
        output = res.json()
        if "mathml" in output:
            print("✅ API responded with MathML")
        else:
            print(f"❌ API responded without MathML: {output}")
    except Exception as e:
        print(f"❌ API call failed: {e}")

def check_outputs():
    print("\n📁 Checking outputs/ directory...")
    ai_path = Path("outputs/discussion_ai_response.txt")
    xml_path = Path("outputs/discussion_equation_mathml.xml")

    if ai_path.exists() and ai_path.stat().st_size > 0:
        print("✅ AI response output exists")
    else:
        print("❌ Missing or empty: discussion_ai_response.txt")

    if xml_path.exists() and xml_path.stat().st_size > 0:
        print("✅ MathML output exists")
    else:
        print("❌ Missing or empty: discussion_equation_mathml.xml")

def scan_for_toxml():
    print("\n🔍 Scanning for deprecated .toxml() usage...")
    result = subprocess.run(["grep", "-r", ".toxml()", "."], capture_output=True, text=True)
    if result.stdout.strip():
        print("❌ Found .toxml() usage:\n" + result.stdout)
    else:
        print("✅ No .toxml() usage detected")

def check_katex_render():
    print("\n🧪 Running KaTeX test...")
    tex_input = Path("outputs/discussion_equation_mathml.xml")
    html_output = Path("outputs/katex_rendered.html")

    if not tex_input.exists():
        print("❌ MathML file not found for KaTeX")
        return

    try:
        subprocess.run([
            "npx", "katex",
            "--input", str(tex_input),
            "--output", str(html_output)
        ], check=True)
        print(f"✅ KaTeX rendered successfully: {html_output}")
    except Exception as e:
        print(f"❌ KaTeX render failed: {e}")

def main():
    print("🚀 Full Repository Verifier Started\n")
    check_imports()
    test_fastapi_endpoint()
    check_outputs()
    scan_for_toxml()
    check_katex_render()
    print("\n✅ Repo verification complete.\n")

if __name__ == "__main__":
    main()
