// Mobile Navigation
const hamburger = document.getElementById('hamburger');
const navWrapper = document.getElementById('navWrapper');

hamburger.addEventListener('click', () => {
  navWrapper.classList.toggle('open');
  hamburger.classList.toggle('active');
});

// Close nav on link click (mobile)
document.querySelectorAll('.main-nav a').forEach(link => {
  link.addEventListener('click', () => {
    navWrapper.classList.remove('open');
    hamburger.classList.remove('active');
  });
});

// Mobile dropdowns
document.querySelectorAll('.dropdown > a').forEach(toggle => {
  toggle.addEventListener('click', (e) => {
    if (window.innerWidth <= 992) {
      e.preventDefault();
      toggle.parentElement.classList.toggle('open');
    }
  });
});

// Scroll effects
const header = document.querySelector('.header');
const scrollTopBtn = document.getElementById('scrollTop');
const hasHero = document.querySelector('.hero') !== null;

// Initial state for pages without hero
if (!hasHero) {
  header.classList.add('scrolled');
}

window.addEventListener('scroll', () => {
  // Toggle scrolled class for header
  if (hasHero) {
    if (window.scrollY > 50) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }
  }

  // Scroll to top button visibility
  if (window.scrollY > 400) {
    scrollTopBtn.classList.add('show');
  } else {
    scrollTopBtn.classList.remove('show');
  }
});

scrollTopBtn.addEventListener('click', () => {
  window.scrollTo({ top: 0, behavior: 'smooth' });
});

// Scroll animations
const fadeElements = document.querySelectorAll('.fade-in');
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
    }
  });
}, { threshold: 0.1 });

fadeElements.forEach(el => observer.observe(el));



// Smooth scroll for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function(e) {
    const targetId = this.getAttribute('href');
    if (targetId === '#') return;
    e.preventDefault();
    const targetEl = document.querySelector(targetId);
    if (targetEl) {
      targetEl.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  });
});
// Registration Certificate Modal
function showCert(e) {
  if (e) e.preventDefault();
  const modal = document.getElementById('certModal');
  if (modal) {
    modal.style.display = 'flex';
  }
}

// Close modals when clicking outside
window.addEventListener('click', (e) => {
  const certModal = document.getElementById('certModal');
  const boardModal = document.getElementById('boardFileModal');
  if (e.target === certModal) certModal.style.display = 'none';
  if (e.target === boardModal) boardModal.style.display = 'none';
});
