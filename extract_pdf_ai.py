import os
import glob
import fitz  # PyMuPDF

def extract_arabic_pdf(pdf_path):
    text = ""
    try:
        doc = fitz.open(pdf_path)
        for page in doc:
            # Extract text
            raw_text = page.get_text()
            if raw_text:
                text += raw_text + "\n"
        
        return text
    except Exception as e:
        print(f"Error reading {pdf_path}: {e}")
        return ""

def main():
    policies_dir = "Files"
    policy_files = glob.glob(os.path.join(policies_dir, "*.pdf"))
    
    policies_html = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>السياسات واللوائح - جمعية التنمية الأهلية بالشويمس</title>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
  <link rel="stylesheet" href="style.css">
  <style>
    .policies-container { padding: 50px 0; }
    .policy-item { margin-bottom: 20px; background: #fff; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); overflow: hidden; }
    .policy-header { padding: 20px; background: var(--primary-color, #1a4d2e); color: white; cursor: pointer; display: flex; justify-content: space-between; align-items: center; }
    .policy-header h3 { margin: 0; font-size: 1.2rem; }
    .policy-content { padding: 20px; display: none; line-height: 1.8; white-space: pre-wrap; background: #f9f9f9; max-height: 500px; overflow-y: auto; text-align: right; }
    .policy-item.active .policy-content { display: block; }
  </style>
</head>
<body>
  <header class="header" style="position: relative; background: #fff; box-shadow: 0 2px 10px rgba(0,0,0,0.1);">
    <div class="container" style="display:flex; align-items:center; justify-content:space-between; height:80px;">
      <a href="index.html" class="logo" style="text-decoration:none; color:inherit; display:flex; align-items:center; gap:10px;">
        <img src="logo.jpeg" alt="شعار الجمعية" style="width: 50px; height: 50px; object-fit: contain; border-radius: 5px;">
        <div class="logo-text"><h2 style="margin:0; font-size:1.2rem;">جمعية التنمية الأهلية بالشويمس</h2></div>
      </a>
      <a href="index.html" class="btn btn-primary">العودة للرئيسية</a>
    </div>
  </header>

  <div class="container policies-container">
    <div class="section-header" style="text-align:center; margin-bottom:40px;">
      <h2>السياسات واللوائح</h2>
      <div class="line" style="width:60px; height:3px; background:var(--secondary-color, #d4a373); margin:10px auto;"></div>
    </div>
"""

    for pf in policy_files:
        title = os.path.basename(pf).replace(".pdf", "")
        print(f"Extracting {title}...")
        content = extract_arabic_pdf(pf)
        
        # Simple HTML escape to avoid messing up the DOM
        content = content.replace("<", "&lt;").replace(">", "&gt;")
        
        policies_html += f"""
    <div class="policy-item">
      <div class="policy-header" onclick="this.parentElement.classList.toggle('active')">
        <h3>{title}</h3>
        <i class="fas fa-chevron-down"></i>
      </div>
      <div class="policy-content">{content}</div>
    </div>
"""

    policies_html += """
  </div>
</body>
</html>
"""

    with open("policies.html", "w", encoding="utf-8") as f:
        f.write(policies_html)
    
    print("policies.html has been generated successfully.")

if __name__ == "__main__":
    main()
