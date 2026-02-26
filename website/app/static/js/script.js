const localeToggleButton = document.getElementById('locale-toggle-button');
const localeToggleImage = document.getElementById('locale-toggle-image');

const normalizePath = (path) => {
    if (!path) {
        return '/';
    }

    if (path.length > 1 && path.endsWith('/')) {
        return path.slice(0, -1);
    }

    return path;
};

const currentPath = normalizePath(window.location.pathname);
const isSpanish = currentPath === '/es' || currentPath.startsWith('/es/');
const route = isSpanish ? normalizePath(currentPath.slice(3) || '/') : currentPath;

const getLocaleTargetPath = () => {
    if (isSpanish) {
        return route === '/' ? '/' : route;
    }

    return route === '/' ? '/es' : `/es${route}`;
};

if (localeToggleButton && localeToggleImage) {
    const imagePath = isSpanish
        ? localeToggleButton.dataset.imageEs
        : localeToggleButton.dataset.imageEn;
    const imageAlt = isSpanish ? 'English' : 'Español';
    const buttonLabel = isSpanish ? 'Change to English' : 'Cambiar a español';

    if (imagePath) {
        localeToggleImage.src = imagePath;
    }
    localeToggleImage.alt = imageAlt;
    localeToggleButton.setAttribute('aria-label', buttonLabel);

    localeToggleButton.addEventListener('click', () => {
        const targetPath = getLocaleTargetPath();
        const targetUrl = `${targetPath}${window.location.search}${window.location.hash}`;
        window.location.href = targetUrl;
    });
}

