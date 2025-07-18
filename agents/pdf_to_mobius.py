import fitz  # PyMuPDF
import sympy as sp
from sympy import Eq, exp, symbols
from sympy.printing.mathml import mathml
from pathlib import Path
import re

def extract_text_from_pdf(pdf_path):
    text = ""
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text()
    return text

def summarize_question_answer(text):
    # Find discussion or question prompts
    match = re.search(r'Discussion.*?[\n:](.+?)\n\n', text, re.DOTALL | re.IGNORECASE)
    question = match.group(1).strip() if match else "Could not extract question."
    return question

def generate_response_from_context(context):
    return f"""Based on Moore’s Law, the number of transistors on an integrated circuit doubles roughly every two years. This exponential model explains rapid computational growth. 

In 2014, a typical chip had 5 billion transistors. Using the exponential formula:

  N(t) = N₀ * 2^(t/2)

Where:
  • N₀ = 5,000,000,000
  • t = number of years since 2014

The exponential model supports that in 2030 (t=16), N(t) ≈ 5e9 * 2^(16/2) = 5e9 * 2^8 = 5e9 * 256 = 1.28 trillion transistors.

This illustrates the power of exponential models in technological forecasting."""

def generate_mathml():
    t, N0 = symbols('t N0')
    expr = N0 * 2**(t / 2)
    mathml_str = mathml(expr, printer='presentation')
    return mathml_str

def write_outputs(context_summary, response, mathml_code):
    Path("outputs").mkdir(exist_ok=True)
    with open("outputs/discussion_response.txt", "w") as f:
        f.write(response)
    with open("outputs/context_summary.txt", "w") as f:
        f.write(context_summary)
    with open("outputs/moore_equation_mathml.xml", "w") as f:
        f.write(mathml_code)
    print("✅ Outputs saved to /outputs directory.")

def main():
    pdfs = [
        "Southern New Hampshire University - 3-1 Discussion- Moore's Law.pdf",
        "3-1 Discussion- Exponential Models - MAT-142-11108-M01 Precalculus with Limits 2.pdf"
    ]
    
    full_text = "\n\n".join([extract_text_from_pdf(pdf) for pdf in pdfs])
    summary = summarize_question_answer(full_text)
    response = generate_response_from_context(full_text)
    mathml_code = generate_mathml()

    write_outputs(summary, response, mathml_code)

if __name__ == "__main__":
    main()
