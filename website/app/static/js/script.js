function setupGalleryModal() {
  const thumbs = document.querySelectorAll('.gallery-thumb');
  const modal = document.getElementById('gallery-modal');
  const modalImg = document.getElementById('gallery-modal-img');
  const modalBg = document.getElementById('gallery-modal-bg');
  const modalClose = document.getElementById('gallery-modal-close');
  if (!modal || !modalImg || !modalBg || !modalClose) return;

  let fadeTimeout = null;

  function openModal(src, alt) {
    clearTimeout(fadeTimeout);
    modalImg.src = src;
    modalImg.alt = alt || '';
    modal.classList.add('is-active');
    modal.style.display = 'flex';
    document.body.style.overflow = 'hidden';
  }

  function closeModal() {
    modal.classList.remove('is-active');
    document.body.style.overflow = '';

    fadeTimeout = setTimeout(() => {
      modal.style.display = 'none';
      modalImg.src = '';
    }, 350);
  }

  thumbs.forEach(thumb => {
    thumb.addEventListener('click', () => {
      openModal(thumb.dataset.full || thumb.src, thumb.alt);
    });
  });
  modalBg.addEventListener('click', closeModal);
  modalClose.addEventListener('click', closeModal);
  document.addEventListener('keydown', (e) => {
    if (modal.classList.contains('is-active') && (e.key === 'Escape' || e.key === 'Esc')) {
      closeModal();
    }
  });

  modal.style.display = 'none';
}

setupGalleryModal();
const counter = document.querySelector(".counter");

if (counter) {
  const target = Number(counter.dataset.count || 0);
  let current = 0;
  const increment = Math.max(1, Math.floor(target / 120));

  const tick = () => {
    current = Math.min(target, current + increment);
    counter.textContent = String(current).padStart(5, "0");

    if (current < target) {
      requestAnimationFrame(tick);
    }
  };

  tick();
}

const sidebarToggle = document.querySelector(".sidebar-toggle");
const sidebarOverlay = document.querySelector(".sidebar-overlay");
const sidebarLinks = document.querySelectorAll(".sidebar-link");

const setActiveLink = () => {
  const currentHash = window.location.hash || "#top";

  sidebarLinks.forEach((link) => {
    if (link.hash === currentHash) {
      link.classList.add("is-active");
    } else {
      link.classList.remove("is-active");
    }
  });
};

const closeSidebar = () => {
  document.body.classList.remove("sidebar-open");
  if (sidebarToggle) {
    sidebarToggle.setAttribute("aria-expanded", "false");
  }
};

if (sidebarToggle) {
  sidebarToggle.addEventListener("click", () => {
    const isOpen = document.body.classList.toggle("sidebar-open");
    sidebarToggle.setAttribute("aria-expanded", String(isOpen));
  });
}

if (sidebarOverlay) {
  sidebarOverlay.addEventListener("click", closeSidebar);
}

window.addEventListener("hashchange", setActiveLink);
setActiveLink();

async function fetchAndRenderBlogPosts() {
  const blogSection = document.querySelector('#blog .list');
  if (!blogSection) return;
  try {
    const res = await fetch('https://blog.astronautmarkus.dev/data/posts');
    if (!res.ok) throw new Error('No se pudo obtener los posts');
    const posts = await res.json();
    blogSection.innerHTML = '';
    posts.forEach(post => {
      const li = document.createElement('li');
      const a = document.createElement('a');
      a.href = post.url;
      a.target = '_blank';
      a.rel = 'noopener noreferrer';
      a.textContent = post.title;
      const meta = document.createElement('span');
      meta.className = 'meta';
      meta.textContent = new Date(post.publishDate).toLocaleDateString();
      li.appendChild(a);
      li.appendChild(document.createTextNode(' '));
      li.appendChild(meta);
      blogSection.appendChild(li);
    });
  } catch (e) {
    blogSection.innerHTML = '<li>No se pudieron cargar los posts.</li>';
  }
}

fetchAndRenderBlogPosts();