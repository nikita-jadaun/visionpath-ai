/* =============================================
   VisionPath AI - Interactive JavaScript
   Theme Toggle, Form Steps, Animations
   ============================================= */

// ====== Theme Toggle ======
const themeToggle = document.getElementById('themeToggle');
const themeIcon = themeToggle?.querySelector('.icon');

function setTheme(theme) {
  document.documentElement.setAttribute('data-theme', theme);
  localStorage.setItem('visionpath-theme', theme);
}

function toggleTheme() {
  const current = document.documentElement.getAttribute('data-theme');
  const newTheme = current === 'light' ? 'dark' : 'light';
  setTheme(newTheme);
}

// Load saved theme on page load
document.addEventListener('DOMContentLoaded', () => {
  const savedTheme = localStorage.getItem('visionpath-theme');
  if (savedTheme) {
    setTheme(savedTheme);
  } else {
    // Check system preference
    const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
    setTheme(prefersDark ? 'dark' : 'light');
  }
});

themeToggle?.addEventListener('click', toggleTheme);

// ====== Form Steps Navigation ======
let currentStep = 0;
const formSections = document.querySelectorAll('.form-section');
const stepCircles = document.querySelectorAll('.step-circle');
const stepLabels = document.querySelectorAll('.step-label');
const progressFill = document.querySelector('.progress-bar-fill');
const prevBtn = document.getElementById('prevBtn');
const nextBtn = document.getElementById('nextBtn');
const submitBtn = document.getElementById('submitBtn');
const mainForm = document.getElementById('mainForm');

function updateSteps() {
  const totalSteps = formSections.length;

  formSections.forEach((section, index) => {
    section.classList.toggle('active', index === currentStep);
  });

  stepCircles.forEach((circle, index) => {
    circle.classList.remove('active', 'completed');
    if (index === currentStep) {
      circle.classList.add('active');
    } else if (index < currentStep) {
      circle.classList.add('completed');
    }
  });

  stepLabels.forEach((label, index) => {
    label.classList.toggle('active', index === currentStep);
  });

  // Update progress bar
  const progress = ((currentStep + 1) / totalSteps) * 100;
  if (progressFill) {
    progressFill.style.width = `${progress}%`;
  }

  // Show/hide buttons
  if (prevBtn) prevBtn.style.display = currentStep === 0 ? 'none' : 'flex';
  if (nextBtn) {
    nextBtn.style.display = currentStep === totalSteps - 1 ? 'none' : 'flex';
  }
  if (submitBtn) {
    submitBtn.style.display = currentStep === totalSteps - 1 ? 'flex' : 'none';
  }
}

function nextStep() {
  if (currentStep < formSections.length - 1) {
    // Validate current step fields
    const currentSection = formSections[currentStep];
    const inputs = currentSection.querySelectorAll('input[required], select[required]');
    let valid = true;
    inputs.forEach(input => {
      if (!input.value) {
        input.style.borderColor = 'var(--danger)';
        valid = false;
        // Shake animation
        input.style.animation = 'shake 0.4s ease';
        setTimeout(() => { input.style.animation = ''; }, 400);
      } else {
        input.style.borderColor = '';
      }
    });
    if (!valid) return;

    currentStep++;
    updateSteps();
    // Scroll to top of form
    document.querySelector('.glass-card')?.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }
}

function prevStep() {
  if (currentStep > 0) {
    currentStep--;
    updateSteps();
    document.querySelector('.glass-card')?.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }
}

// Add shake animation
const styleSheet = document.createElement('style');
styleSheet.textContent = `
  @keyframes shake {
    0%, 100% { transform: translateX(0); }
    25% { transform: translateX(-5px); }
    50% { transform: translateX(5px); }
    75% { transform: translateX(-5px); }
  }
`;
document.head.appendChild(styleSheet);

prevBtn?.addEventListener('click', prevStep);
nextBtn?.addEventListener('click', nextStep);

// Initialize steps
updateSteps();

// ====== Skill Range Sliders ======
const skillSliders = document.querySelectorAll('.skill-slider');

skillSliders.forEach(slider => {
  const valueDisplay = slider.parentElement?.querySelector('.skill-value');
  if (valueDisplay) {
    valueDisplay.textContent = slider.value;
  }

  slider.addEventListener('input', function() {
    const display = this.parentElement?.querySelector('.skill-value');
    if (display) {
      display.textContent = this.value;
    }
    // Update slider background
    const min = this.min || 0;
    const max = this.max || 10;
    const percent = ((this.value - min) / (max - min)) * 100;
    this.style.background = `linear-gradient(to right, var(--accent-primary) ${percent}%, var(--border-color) ${percent}%)`;
  });

  // Trigger initial state
  slider.dispatchEvent(new Event('input'));
});

// ====== Form Submit Loading ======
mainForm?.addEventListener('submit', function(e) {
  const loadingSpinner = document.getElementById('loadingSpinner');
  if (loadingSpinner) {
    loadingSpinner.classList.add('show');
  }
});

// ====== Result Page: Confetti Animation ======
function launchConfetti() {
  const container = document.createElement('div');
  container.className = 'confetti-container';
  document.body.appendChild(container);

  const colors = ['#6366f1', '#22c55e', '#f59e0b', '#ef4444', '#ec4899', '#06b6d4', '#8b5cf6'];
  const shapes = ['circle', 'square', 'triangle'];

  for (let i = 0; i < 80; i++) {
    const piece = document.createElement('div');
    piece.className = 'confetti-piece';
    piece.style.left = Math.random() * 100 + '%';
    piece.style.background = colors[Math.floor(Math.random() * colors.length)];
    piece.style.width = (Math.random() * 8 + 4) + 'px';
    piece.style.height = (Math.random() * 8 + 4) + 'px';
    piece.style.borderRadius = shapes[Math.floor(Math.random() * shapes.length)] === 'circle' ? '50%' : '2px';
    piece.style.animationDuration = (Math.random() * 2 + 1.5) + 's';
    piece.style.animationDelay = (Math.random() * 1.5) + 's';
    piece.style.transform = `rotate(${Math.random() * 360}deg)`;
    container.appendChild(piece);
  }

  // Remove confetti after animation
  setTimeout(() => {
    container.remove();
  }, 4000);
}

// Check if result is Achievable and launch confetti
const resultBadge = document.querySelector('.result-badge');
if (resultBadge && resultBadge.classList.contains('achievable')) {
  setTimeout(launchConfetti, 500);
}

// ====== Typing Effect for Result Message ======
const resultMessage = document.querySelector('.result-message');
if (resultMessage) {
  const text = resultMessage.textContent;
  resultMessage.textContent = '';
  resultMessage.classList.add('typing-text');

  let charIndex = 0;
  function typeText() {
    if (charIndex < text.length) {
      resultMessage.textContent += text.charAt(charIndex);
      charIndex++;
      setTimeout(typeText, 30);
    } else {
      resultMessage.classList.remove('typing-text');
      resultMessage.style.borderRight = 'none';
    }
  }
  setTimeout(typeText, 800);
}

// ====== Animate Progress Bar on Result Page ======
const progressFillEl = document.querySelector('.result-progress .progress-fill');
if (progressFillEl) {
  setTimeout(() => {
    progressFillEl.style.width = progressFillEl.getAttribute('data-width') || '85%';
  }, 500);
}

// ====== Smooth Reveal on Scroll (for any future elements) ======
const observerOptions = {
  threshold: 0.1,
  rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('fade-in');
      observer.unobserve(entry.target);
    }
  });
}, observerOptions);

document.querySelectorAll('.animate-on-scroll').forEach(el => {
  observer.observe(el);
});
