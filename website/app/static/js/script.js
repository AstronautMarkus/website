const projectsMeta = [
  {
    slug: 'esp8266-labs',
    name: 'ESP8266 Labs',
    githubUrl: 'https://github.com/AstronautMarkus/ESP8266-Labs',
    tags: ['Arduino', 'C++']
  },
  {
    slug: 'turnomaster',
    name: 'TurnoMaster',
    tags: ['React', 'TailwindCSS', 'Laravel', 'MySQL', 'Chart.js', 'Axios']
  },
  {
    slug: 'fumoindex',
    name: 'FumoIndex',
    githubUrl: 'https://github.com/astronautmarkus/fumoindex',
    tags: ['React', 'TypeScript', 'Laravel', 'MySQL', 'Tailwind CSS']
  },
  {
    slug: 'abbybot-project',
    name: 'AbbyBot Project',
    githubUrl: 'https://github.com/AbbyBot/Discord-AbbyBot',
    tags: ['Discord.py', 'Python', 'MySQL']
  },
  {
    slug: 'blog-astronautmarkus',
    name: 'Blog AstronautMarkus',
    githubUrl: 'https://github.com/AstronautMarkus/blog.astronautmarkus.dev',
    tags: ['Laravel', 'Blade', 'Tailwind CSS', 'MySQL', 'PHP']
  },
  {
    slug: 'abbybot-project-website',
    name: 'AbbyBot Project Website',
    githubUrl: 'https://github.com/AbbyBot/AbbyBot-Website',
    tags: ['Flask', 'Python', 'Bootstrap', 'MySQL', 'Gunicorn', 'Docker']
  },
  {
    slug: 'multi-stock-sync',
    name: 'Multi Stock Sync',
    githubUrl: 'https://github.com/AstronautMarkus/Multi-Stock-Sync',
    tags: ['React', 'Node.js', 'Bootstrap', 'Chart.js', 'Axios']
  },
  {
    slug: 'multi-stock-sync-back',
    name: 'Multi Stock Sync Back',
    githubUrl: 'https://github.com/AstronautMarkus/Multi-Stock-Sync-Back',
    tags: ['Laravel', 'Sanctum', 'MySQL', 'PHP']
  },
  {
    slug: 'multi-stock-sync-api-viewer',
    name: 'Multi Stock Sync API Viewer',
    githubUrl: 'https://github.com/AstronautMarkus/Multi-Stock-API-Viewer',
    tags: ['Laravel', 'Swagger']
  },
  {
    slug: 'mofustore',
    name: 'MofuStore',
    tags: ['Python', 'Django', 'Bootstrap', 'MySQL']
  },
  {
    slug: 'camellosfood-repartidor',
    name: 'CamellosFood Repartidor',
    githubUrl: 'https://github.com/AstronautMarkus/CamellosFood-Repartidor-3.0',
    tags: ['Ionic', 'Angular', 'Django']
  },
  {
    slug: 'constru-mic',
    name: 'Constru MIC',
    githubUrl: 'https://github.com/MarcosKingsDuoc/CONSTRU_MIC',
    tags: ['Django', 'Bootstrap', 'MySQL']
  },
  {
    slug: 'mofulunches-web',
    name: 'MofuLunches Web',
    githubUrl: 'https://github.com/AstronautMarkus/MofuLunches-Web',
    tags: ['Flask', 'Bootstrap']
  },
  {
    slug: 'mofulunches-api',
    name: 'MofuLunches API',
    githubUrl: 'https://github.com/AstronautMarkus/MofuLunches-API',
    tags: ['Python', 'Flask', 'MongoDB']
  },
  {
    slug: 'mofulunches-totem',
    name: 'MofuLunches Totem',
    githubUrl: 'https://github.com/AstronautMarkus/MofuLunches-Totem',
    tags: ['Electron', 'Arduino', 'React']
  },
  {
    slug: 'mofulunches-eldimon',
    name: 'MofuLunches ElDimon',
    githubUrl: 'https://github.com/AstronautMarkus/MofuLunches-ElDimon',
    tags: ['Arduino', 'C++']
  },
  {
    slug: 'mofulunches-listener',
    name: 'MofuLunches ElDimon Listener',
    githubUrl: 'https://github.com/AstronautMarkus/MofuLunches-ElDimon_Listener',
    tags: ['Python', 'PyQt5']
  },
  {
    slug: 'reyesandfriends-app',
    name: 'ReyesAndFriends App',
    githubUrl: 'https://github.com/reyesandfriends/reyesandfriends-app',
    tags: ['React', 'Tailwind CSS', 'Flask', 'Docker', 'MySQL']
  },
  {
    slug: 'reyeshosting',
    name: 'ReyesHosting',
    tags: ['Laravel', 'Tailwind CSS', 'Livewire', 'MySQL']
  }
];

function renderProjectsList() {
  const container = document.getElementById('projects-list');
  if (!container) return;
  container.innerHTML = '';
  projectsMeta.forEach(project => {
    const card = document.createElement('div');
    card.className = 'project-card';

    const title = document.createElement('div');
    title.className = 'project-title';
    title.textContent = project.name || project.slug;
    card.appendChild(title);

    if (project.githubUrl) {
      const github = document.createElement('a');
      github.className = 'project-github';
      github.href = project.githubUrl;
      github.target = '_blank';
      github.rel = 'noopener noreferrer';
      github.textContent = 'GitHub';
      card.appendChild(github);
    }

    if (project.tags && project.tags.length) {
      const tags = document.createElement('div');
      tags.className = 'project-tags';
      project.tags.forEach(tag => {
        const tagEl = document.createElement('span');
        tagEl.className = 'project-tag';
        tagEl.textContent = tag;
        tags.appendChild(tagEl);
      });
      card.appendChild(tags);
    }

    container.appendChild(card);
  });
}

renderProjectsList();

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