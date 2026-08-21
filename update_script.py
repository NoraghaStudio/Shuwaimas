import os
import glob
import urllib.parse

# Generate policies.html with grid of PDF cards
policies_dir = "Files"
policy_files = glob.glob(os.path.join(policies_dir, "*.pdf"))

policies_html = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>السياسات واللوائح والتعاميم - جمعية التنمية الأهلية بالشويمس</title>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
  <link rel="stylesheet" href="style.css">
  <style>
    .policies-container { padding: 50px 0; background-color: #fcfcfc; }
    .policies-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
      gap: 30px;
      padding: 20px;
    }
    .policy-card {
      background: #fff;
      border-radius: 12px;
      box-shadow: 0 4px 15px rgba(0,0,0,0.05);
      padding: 30px 20px;
      text-align: center;
      transition: transform 0.3s;
      display: flex;
      flex-direction: column;
      align-items: center;
      border: 1px solid #f0f0f0;
      height: 100%;
    }
    .policy-card:hover {
      transform: translateY(-5px);
      box-shadow: 0 8px 25px rgba(0,0,0,0.1);
    }
    .policy-icon {
      width: 80px;
      height: 80px;
      background-color: #3884c9;
      border-radius: 50%;
      display: flex;
      justify-content: center;
      align-items: center;
      margin-bottom: 20px;
    }
    .policy-icon i {
      font-size: 35px;
      color: white;
    }
    .policy-title {
      font-size: 1.1rem;
      color: #333;
      margin-bottom: 25px;
      font-weight: bold;
      flex-grow: 1;
      display: flex;
      align-items: center;
      justify-content: center;
      line-height: 1.5;
    }
    .btn-download {
      display: inline-block;
      padding: 10px 35px;
      background-color: #3884c9;
      color: white;
      text-decoration: none;
      border-radius: 25px;
      font-weight: bold;
      transition: background-color 0.3s;
    }
    .btn-download:hover {
      background-color: #2a69a4;
    }
    
    /* Header logo styling */
    .header-logo-container {
      display: flex;
      align-items: center;
      gap: 15px;
      text-decoration: none;
      color: inherit;
    }
    .header-logo-container img {
      width: 50px;
      height: 50px;
      object-fit: contain;
      border-radius: 5px;
    }
  </style>
</head>
<body style="background-color: #fcfcfc;">
  <header class="header" style="position: relative; background: #fff; box-shadow: 0 2px 10px rgba(0,0,0,0.1);">
    <div class="container" style="display:flex; align-items:center; justify-content:space-between; height:80px;">
      <a href="index.html" class="header-logo-container">
        <img src="logo.jpeg" alt="شعار الجمعية">
        <div class="logo-text"><h2 style="margin:0; font-size:1.2rem;">جمعية التنمية الأهلية بالشويمس</h2></div>
      </a>
      <a href="index.html" class="btn btn-primary" style="background-color: #3884c9;">العودة للرئيسية</a>
    </div>
  </header>

  <div class="container policies-container">
    <div class="section-header" style="text-align:center; margin-bottom:40px;">
      <h2>السياسات واللوائح والقرارات</h2>
      <div class="line" style="width:60px; height:3px; background:#3884c9; margin:10px auto;"></div>
    </div>
    
    <div class="policies-grid">
"""

for pf in policy_files:
    title = os.path.basename(pf).replace(".pdf", "")
    url_file = urllib.parse.quote(pf)
    
    policies_html += f"""
      <div class="policy-card">
        <div class="policy-icon">
          <i class="fas fa-file-contract"></i>
        </div>
        <div class="policy-title">{title}</div>
        <a href="{url_file}" target="_blank" class="btn-download">تحميل</a>
      </div>
    """

policies_html += """
    </div>
  </div>
</body>
</html>
"""

with open("policies.html", "w", encoding="utf-8") as f:
    f.write(policies_html)

print("policies.html generated successfully.")
