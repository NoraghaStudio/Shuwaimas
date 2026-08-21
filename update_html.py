import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

# We need to create board.html using index.html as a template
if not os.path.exists('board.html'):
    with open('index.html', 'r', encoding='utf-8') as f:
        board_content = f.read()
    
    # Remove hero, stats, about, ceo, news, partners, contact
    # Keep header and footer
    # Replace content with Board members
    board_content = re.sub(r'<!-- Hero Section -->.*?<!-- Footer -->', 
    '''<!-- Board Section -->
  <section class="section" id="board" style="padding-top:120px; min-height:60vh;">
    <div class="container">
      <div class="section-header fade-in">
        <h2>مجلس الإدارة</h2>
        <p>أعضاء مجلس الإدارة لجمعية التنمية الأهلية بالشويمس</p>
        <div class="line"></div>
      </div>
      <div class="stats-grid" style="grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px;">
        <!-- Placeholder for board members since text file was missing -->
        <div class="stat-card fade-in">
          <i class="fas fa-user-tie"></i>
          <h3 style="margin-top:15px; color:var(--primary-dark)">نوف بنت بلال العبدالعزيز</h3>
          <span class="label">رئيس المجلس</span>
        </div>
        <div class="stat-card fade-in">
          <i class="fas fa-user-tie"></i>
          <h3 style="margin-top:15px; color:var(--primary-dark)">صباح بنت محمد بن إبراهيم شويل</h3>
          <span class="label">نائب الرئيس</span>
        </div>
        <div class="stat-card fade-in">
          <i class="fas fa-user-tie"></i>
          <h3 style="margin-top:15px; color:var(--primary-dark)">شيخة بنت ناصر بن صالح الدوسري</h3>
          <span class="label">المشرف المالي</span>
        </div>
        <div class="stat-card fade-in">
          <i class="fas fa-user"></i>
          <h3 style="margin-top:15px; color:var(--primary-dark)">عهود بنت فهد بن ناصر بن سليم</h3>
          <span class="label">عضو</span>
        </div>
        <div class="stat-card fade-in">
          <i class="fas fa-user"></i>
          <h3 style="margin-top:15px; color:var(--primary-dark)">حياة بنت حمد بن مرشد بن قاسم</h3>
          <span class="label">عضو</span>
        </div>
        <div class="stat-card fade-in">
          <i class="fas fa-user"></i>
          <h3 style="margin-top:15px; color:var(--primary-dark)">أسماء بنت مبارك بن عبدالله أبومحيميد</h3>
          <span class="label">عضو</span>
        </div>
      </div>
    </div>
  </section>
  <!-- Footer -->''', board_content, flags=re.DOTALL)
    
    board_content = board_content.replace('<title>الرئيسية', '<title>مجلس الإدارة')
    with open('board.html', 'w', encoding='utf-8') as f:
        f.write(board_content)
    html_files.append('board.html')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update Logo Size
    content = re.sub(r'style="width:\s*\d+px;\s*height:\s*\d+px;', 'style="width: 50px; height: 50px;', content)

    # 2. Add Registration Certificate Modal & Button
    # Replace link in dropdown and footer
    content = content.replace('<li><a href="#">شهادة التسجيل</a></li>', '<li><a href="#" onclick="showCert(event)">شهادة التسجيل</a></li>')
    
    if 'showCert' not in content:
        modal_html = """
  <!-- Cert Modal -->
  <div id="certModal" style="display:none; position:fixed; z-index:9999; left:0; top:0; width:100%; height:100%; background-color:rgba(0,0,0,0.8); align-items:center; justify-content:center;">
    <div style="position:relative; max-width:90%; max-height:90%;">
      <span onclick="document.getElementById('certModal').style.display='none'" style="position:absolute; top:-40px; right:0; color:#fff; font-size:30px; cursor:pointer;">&times;</span>
      <img src="images/شهادة تسجيل جمعية.jpeg" style="max-width:100%; max-height:90vh; border-radius:8px;">
    </div>
  </div>
  <script>
    function showCert(e) {
      e.preventDefault();
      document.getElementById('certModal').style.display = 'flex';
    }
  </script>
</body>"""
        content = content.replace('</body>', modal_html)

    # 3. Add License Number
    if 'رقم الترخيص' not in content:
        content = content.replace('جميع الحقوق محفوظة © ٢٠٢٦ جمعية التنمية الأهلية بالشويمس', 'جميع الحقوق محفوظة © ٢٠٢٦ جمعية التنمية الأهلية بالشويمس | رقم الترخيص: ---')

    if file == 'index.html':
        # Change About Image
        content = re.sub(r'<img src="images/WhatsApp%20Image%20.*?alt="عن الجمعية">', '<img src="images/من نحن.jpeg" alt="عن الجمعية">', content)
        # Remove CEO section
        content = re.sub(r'<!-- CEO Section -->.*?<!-- News Section -->', '<!-- News Section -->', content, flags=re.DOTALL)
        content = content.replace('<li><a href="#ceo">المدير التنفيذي</a></li>', '')
        # Remove News section
        content = re.sub(r'<!-- News Section -->.*?<!-- Partners Section -->', '<!-- Partners Section -->', content, flags=re.DOTALL)
        content = content.replace('<li><a href="#news">الأخبار</a></li>', '')
        content = content.replace('<li><a href="index.html#news">الأخبار</a></li>', '')
        
    elif file == 'gallery.html':
        # Replace gallery grid with carousel
        # We need to get all images from images folder
        images = [i for i in os.listdir('images') if i.lower().endswith(('.png', '.jpg', '.jpeg'))]
        images.sort()
        
        carousel_html = """
<style>
.carousel-container {
  position: relative;
  max-width: 800px;
  margin: 0 auto;
  overflow: hidden;
  border-radius: var(--radius);
  box-shadow: var(--shadow-lg);
}
.carousel-track {
  display: flex;
  transition: transform 0.5s ease;
}
.carousel-slide {
  min-width: 100%;
}
.carousel-slide img {
  width: 100%;
  height: 500px;
  object-fit: contain;
  background: #000;
}
.carousel-btn {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  background: rgba(255,255,255,0.7);
  border: none;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  font-size: 20px;
  cursor: pointer;
  z-index: 10;
}
.carousel-btn:hover { background: #fff; }
.prev-btn { left: 10px; }
.next-btn { right: 10px; }
</style>

<div class="carousel-container fade-in">
  <button class="carousel-btn prev-btn" onclick="moveSlide(-1)"><i class="fas fa-chevron-left"></i></button>
  <button class="carousel-btn next-btn" onclick="moveSlide(1)"><i class="fas fa-chevron-right"></i></button>
  <div class="carousel-track" id="carouselTrack">
"""
        for img in images:
            carousel_html += f'    <div class="carousel-slide"><img src="images/{img}" alt="معرض الصور"></div>\n'
            
        carousel_html += """  </div>
</div>

<script>
  let slideIndex = 0;
  const track = document.getElementById('carouselTrack');
  const slides = document.querySelectorAll('.carousel-slide');
  function moveSlide(n) {
    slideIndex += n;
    if (slideIndex >= slides.length) slideIndex = 0;
    if (slideIndex < 0) slideIndex = slides.length - 1;
    track.style.transform = `translateX(${slideIndex * 100}%)`;
  }
</script>
"""
        content = re.sub(r'<div class="gallery-grid">.*?</div>\s*</div>\s*</div>', carousel_html + '</div>\n</div>', content, flags=re.DOTALL)

    # Link to board page
    content = content.replace('<li><a href="#">مجلس الإدارة</a></li>', '<li><a href="board.html">مجلس الإدارة</a></li>')

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

# Also update style.css for hero bg
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

css = re.sub(r'background: url\(.*?\) center/cover;', "background: url('images/Hero.jpg') center/cover;", css)
with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Updates completed successfully.")
