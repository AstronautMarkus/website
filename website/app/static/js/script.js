const localeToggleButton = document.getElementById('locale-toggle-button');
const localeToggleImage = document.getElementById('locale-toggle-image');
const earthImage = document.querySelector('.earth-image');
const moonImage = document.querySelector('.moon-image');

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

const getLocaleToggleTargetPath = () => {
    if (isSpanish) {
        return route === '/' ? '/' : route;
    }

    return route === '/' ? '/es' : `/es${route}`;
};

const toggleButtonConfig = {
    en: {
        imagePath: localeToggleButton?.dataset.imageEn,
        imageAlt: 'Español',
        buttonLabel: 'Cambiar a español'
    },
    es: {
        imagePath: localeToggleButton?.dataset.imageEs,
        imageAlt: 'English',
        buttonLabel: 'Change to English'
    }
};

if (localeToggleButton && localeToggleImage) {
    const config = isSpanish ? toggleButtonConfig.es : toggleButtonConfig.en;
    if (config.imagePath) {
        localeToggleImage.src = config.imagePath;
    }
    localeToggleImage.alt = config.imageAlt;
    localeToggleButton.setAttribute('aria-label', config.buttonLabel);

    localeToggleButton.addEventListener('click', () => {
        const targetPath = getLocaleToggleTargetPath();
        const targetUrl = `${targetPath}${window.location.search}${window.location.hash}`;
        window.location.href = targetUrl;
    });
}

if (earthImage || moonImage) {
    const earthLeftOffset = Math.random() * 30 + 20;
    const earthBottomOffset = Math.random() * 30 + 20;

    if (earthImage) {
        earthImage.style.left = `calc(90% - ${earthLeftOffset}px)`;
        earthImage.style.bottom = `${earthBottomOffset}px`;
    }

    if (moonImage) {
        const moonDistanceX = Math.random() * 16 + 42;
        const moonDistanceY = Math.random() * 14 + 24;
        moonImage.style.left = `calc(90% - ${earthLeftOffset + moonDistanceX}px)`;
        moonImage.style.bottom = `${earthBottomOffset + moonDistanceY}px`;
    }
}