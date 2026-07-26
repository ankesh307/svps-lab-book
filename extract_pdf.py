# -*- coding: utf-8 -*-
import pdfplumber
import sys

output_file = r"C:\Users\ankes\.gemini\antigravity\scratch\curriculum_app\pdf_content.txt"

with pdfplumber.open(r"C:\Users\ankes\Downloads\curriculum lab.pdf") as pdf:
    with open(output_file, "w", encoding="utf-8") as out:
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text:
                out.write(f"\n=== PAGE {i+1} ===\n")
                out.write(text)
                out.write("\n")

print("Done! Saved to pdf_content.txt")
