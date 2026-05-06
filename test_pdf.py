import fitz
doc = fitz.open("Files/سياسة ادارة المتطوعيين التنمية.pdf")
text = doc[0].get_text()
print("RAW TEXT:")
print(repr(text[:100]))
