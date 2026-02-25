const footerText = document.getElementById('footer-text');
const routePathContainer = document.getElementById('route-path');
const currentYear = new Date().getFullYear();
footerText.textContent = `© 2003 / ${currentYear} Marcos Reyes / Lain Iwakura. All rights reserved.`;

const normalizePath = (path) => {
    if (!path) {
        return '/';
    }

    if (path.length > 1 && path.endsWith('/')) {
        return path.slice(0, -1);
    }

    return path;
};

const getRouteContext = (pathname) => {
    const normalizedPath = normalizePath(pathname);

    if (normalizedPath === '/es') {
        return {
            locale: 'es',
            localePrefix: '/es',
            route: '/'
        };
    }

    if (normalizedPath.startsWith('/es/')) {
        const routeWithoutPrefix = normalizedPath.slice(3) || '/';

        return {
            locale: 'es',
            localePrefix: '/es',
            route: normalizePath(routeWithoutPrefix)
        };
    }

    return {
        locale: 'en',
        localePrefix: '',
        route: normalizedPath
    };
};

const routeContext = getRouteContext(window.location.pathname);
const route = routeContext.route;
const isSpanish = routeContext.locale === 'es';

const texts = {
    availableRoutes: isSpanish ? 'Rutas disponibles' : 'Available routes',
    backHome: isSpanish ? 'Volver al inicio' : 'Back Home'
};

const staticRoutes = [
    {
        path: '/about',
        label: isSpanish ? 'Acerca del sitio web' : 'About Website'
    },
    {
        path: '/markus-tech-stack',
        label: isSpanish ? 'Tech Stack de Markus' : 'Markus Tech Stack'
    },
    {
        path: '/portfolio',
        label: isSpanish ? 'Portafolio' : 'Portfolio'
    }
];

const normalizedStaticRoutes = staticRoutes.map((item) => ({
    ...item,
    path: normalizePath(item.path)
}));

const buildLocalizedPath = (path) => {
    const normalizedTarget = normalizePath(path);

    if (!routeContext.localePrefix) {
        return normalizedTarget;
    }

    if (normalizedTarget === '/') {
        return routeContext.localePrefix;
    }

    return `${routeContext.localePrefix}${normalizedTarget}`;
};

const buttonsWrapper = document.createElement('div');

if (route === '/') {
    const routesTitle = document.createElement('h4');
    routesTitle.textContent = texts.availableRoutes;
    buttonsWrapper.appendChild(routesTitle);

    normalizedStaticRoutes.forEach((item) => {
        const link = document.createElement('a');
        link.href = buildLocalizedPath(item.path);
        link.textContent = item.label;
        link.className = 'route-button';
        buttonsWrapper.appendChild(link);
    });
} else {
    const homeLink = document.createElement('a');
    homeLink.href = buildLocalizedPath('/');
    homeLink.textContent = texts.backHome;
    homeLink.className = 'route-button';
    buttonsWrapper.appendChild(homeLink);
}

if (routePathContainer) {
    routePathContainer.appendChild(buttonsWrapper);
}