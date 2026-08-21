import os
import glob
import urllib.parse
import re

with open("index.html", "r", encoding="utf-8") as f:
    index_content = f.read()

# Extract header part (up to the end of <header class="header">)
header_match = re.search(r'(.*?)</header>', index_content, re.DOTALL)
header_part = header_match.group(1) + "</header>"

# Extract footer part (from <!-- Footer --> to the end)
footer_match = re.search(r'(<!-- Footer -->.*)', index_content, re.DOTALL)
footer_part = footer_match.group(1)

# Generate policies.html
policies_dir = "Files"
policy_files = glob.glob(os.path.join(policies_dir, "*.pdf"))

policies_html = header_part + """
  <style>
    .policies-container { padding: 80px 0; background-color: var(--light); }
    .policies-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
      gap: 30px;
      padding: 20px 0;
    }
    .policy-card {
      background: var(--white);
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      padding: 30px 20px;
      text-align: center;
      transition: var(--transition);
      display: flex;
      flex-direction: column;
      align-items: center;
      border: 1px solid var(--gray-light);
      height: 100%;
    }
    .policy-card:hover {
      transform: translateY(-5px);
      box-shadow: var(--shadow-lg);
    }
    .policy-icon {
      width: 80px;
      height: 80px;
      background: linear-gradient(135deg, var(--primary), var(--primary-light));
      border-radius: 50%;
      display: flex;
      justify-content: center;
      align-items: center;
      margin-bottom: 20px;
      color: var(--white);
      font-size: 35px;
    }
    .policy-title {
      font-size: 1.1rem;
      color: var(--dark);
      margin-bottom: 25px;
      font-weight: 700;
      flex-grow: 1;
      display: flex;
      align-items: center;
      justify-content: center;
      line-height: 1.5;
    }
    .btn-download {
      display: inline-block;
      padding: 10px 35px;
      background: linear-gradient(135deg, var(--primary), var(--primary-light));
      color: var(--white);
      text-decoration: none;
      border-radius: 25px;
      font-weight: 600;
      transition: var(--transition);
      border: none;
    }
    .btn-download:hover {
      transform: translateY(-3px);
      box-shadow: 0 8px 25px rgba(26,107,60,0.4);
      color: var(--white);
    }
  </style>

  <div class="policies-container">
    <div class="container">
        <div class="section-header fade-in">
          <h2>السياسات واللوائح والقرارات</h2>
          <p>مكتبة السياسات واللوائح الخاصة بجمعية التنمية الأهلية بالشويمس</p>
          <div class="line"></div>
        </div>
        
        <div class="policies-grid">
"""

for pf in policy_files:
    title = os.path.basename(pf).replace(".pdf", "")
    title = title.replace("_", " ").replace("-", " ")
    title = re.sub(r'[0-9()]+', '', title)
    title = re.sub(r'\s+', ' ', title).strip()
    url_file = urllib.parse.quote(pf)
    
    policies_html += f"""
          <div class="policy-card fade-in">
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
  </div>
""" + footer_part

# Fix title for policies page
policies_html = policies_html.replace("<title>الرئيسية - جمعية التنمية الأهلية بالشويمس</title>", "<title>السياسات واللوائح والتعاميم - جمعية التنمية الأهلية بالشويمس</title>")

# Make nav active class correct
policies_html = policies_html.replace('<li><a href="#" class="active">الرئيسية</a></li>', '<li><a href="index.html">الرئيسية</a></li>')
policies_html = policies_html.replace('<li><a href="policies.html">السياسات واللوائح</a></li>', '<li><a href="policies.html" class="active">السياسات واللوائح</a></li>')

# Fix links in dropdowns so they go to index.html#section
policies_html = policies_html.replace('href="#about"', 'href="index.html#about"')
policies_html = policies_html.replace('href="#news"', 'href="index.html#news"')
policies_html = policies_html.replace('href="#partners"', 'href="index.html#partners"')
policies_html = policies_html.replace('href="#contact"', 'href="index.html#contact"')
policies_html = policies_html.replace('href="#ceo"', 'href="index.html#ceo"')

with open("policies.html", "w", encoding="utf-8") as f:
    f.write(policies_html)

print("policies.html updated to match index.html styling.")

# Do the same for gallery.html if possible
images_dir = "images"
def is_valid_gallery_file(f):
    name = os.path.splitext(os.path.basename(f))[0]
    return bool(re.match(r'^[A-Za-z]\d*$', name))

image_files = [f for f in glob.glob(os.path.join(images_dir, "*")) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')) and is_valid_gallery_file(f)]
video_files = [f for f in glob.glob(os.path.join(images_dir, "*")) if f.lower().endswith(('.mp4', '.mov')) and is_valid_gallery_file(f)]

gallery_html = header_part + """
  <style>
    .gallery-container { padding: 150px 0 80px; background-color: var(--light); }
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
    .carousel-slide img, .carousel-slide video {
      width: 100%;
      height: 500px;
      object-fit: contain;
      background: #000;
      display: block;
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

  <div class="gallery-container">
    <div class="container">
        <div class="section-header fade-in">
          <h2>معرض الصور والمرئيات</h2>
          <p>جانب من أعمال وأنشطة جمعية التنمية الأهلية بالشويمس</p>
          <div class="line"></div>
        </div>
        
        <div class="carousel-container fade-in">
          <button class="carousel-btn prev-btn" onclick="moveSlide(-1)"><i class="fas fa-chevron-left"></i></button>
          <button class="carousel-btn next-btn" onclick="moveSlide(1)"><i class="fas fa-chevron-right"></i></button>
          <div class="carousel-track" id="carouselTrack">
"""

all_files = image_files + video_files
for f in all_files:
    url_f = urllib.parse.quote(f)
    if f.lower().endswith(('.mp4', '.mov')):
        gallery_html += f'            <div class="carousel-slide"><video src="{url_f}" controls preload="metadata"></video></div>\n'
    else:
        gallery_html += f'            <div class="carousel-slide"><img src="{url_f}" alt="معرض الصور"></div>\n'

gallery_html += """          </div>
        </div>
    </div>
  </div>

<script>
  const track = document.getElementById('carouselTrack');
  if (track && track.children.length > 0) {
      const slides = Array.from(track.children);
      const firstClone = slides[0].cloneNode(true);
      const lastClone = slides[slides.length - 1].cloneNode(true);
      track.appendChild(firstClone);
      track.insertBefore(lastClone, slides[0]);
      const allSlides = Array.from(track.children);
      let slideIndex = 1;
      let isTransitioning = false;
      track.style.transform = `translateX(${slideIndex * 100}%)`;

      window.moveSlide = function(n) {
        if (isTransitioning) return;
        isTransitioning = true;
        slideIndex += n;
        track.style.transition = "transform 0.5s ease";
        track.style.transform = `translateX(${slideIndex * 100}%)`;
      }

      track.addEventListener('transitionend', () => {
        isTransitioning = false;
        if (allSlides[slideIndex] === firstClone) {
          track.style.transition = "none";
          slideIndex = 1;
          track.style.transform = `translateX(${slideIndex * 100}%)`;
        }
        if (allSlides[slideIndex] === lastClone) {
          track.style.transition = "none";
          slideIndex = allSlides.length - 2;
          track.style.transform = `translateX(${slideIndex * 100}%)`;
        }
      });

      let touchStartX = 0;
      let touchEndX = 0;
      track.addEventListener('touchstart', e => { touchStartX = e.changedTouches[0].screenX; }, {passive: true});
      track.addEventListener('touchend', e => { touchEndX = e.changedTouches[0].screenX; handleSwipe(); }, {passive: true});
      function handleSwipe() {
        const swipeThreshold = 50;
        if (touchEndX < touchStartX - swipeThreshold) moveSlide(-1);
        if (touchEndX > touchStartX + swipeThreshold) moveSlide(1);
      }
  }
</script>
""" + footer_part

gallery_html = gallery_html.replace("<title>الرئيسية - جمعية التنمية الأهلية بالشويمس</title>", "<title>معرض الصور والمرئيات - جمعية التنمية الأهلية بالشويمس</title>")
gallery_html = gallery_html.replace('<li><a href="#" class="active">الرئيسية</a></li>', '<li><a href="index.html">الرئيسية</a></li>')
gallery_html = gallery_html.replace('<li><a href="gallery.html">المعرض</a></li>', '<li><a href="gallery.html" class="active">المعرض</a></li>')
gallery_html = gallery_html.replace('href="#about"', 'href="index.html#about"')
gallery_html = gallery_html.replace('href="#news"', 'href="index.html#news"')
gallery_html = gallery_html.replace('href="#partners"', 'href="index.html#partners"')
gallery_html = gallery_html.replace('href="#contact"', 'href="index.html#contact"')
gallery_html = gallery_html.replace('href="#ceo"', 'href="index.html#ceo"')

with open("gallery.html", "w", encoding="utf-8") as f:
    f.write(gallery_html)

print("gallery.html updated to match index.html styling.")

