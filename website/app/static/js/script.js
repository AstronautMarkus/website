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

const quoteMarquee = document.getElementById('quote-marquee');

if (quoteMarquee) {
    const marqueeText = quoteMarquee.querySelector('.marquee-text');
    const quotesJson = quoteMarquee.dataset.quotes;

    let quotes = [];

    if (quotesJson) {
        try {
            const parsedQuotes = JSON.parse(quotesJson);
            if (Array.isArray(parsedQuotes)) {
                quotes = parsedQuotes.filter((quote) => typeof quote === 'string' && quote.trim() !== '');
            }
        } catch (error) {
            quotes = [];
        }
    }

    let lastIndex = -1;

    const getRandomQuote = () => {
        if (quotes.length === 0) {
            return '';
        }

        if (quotes.length === 1) {
            lastIndex = 0;
            return quotes[0];
        }

        let index = lastIndex;
        while (index === lastIndex) {
            index = Math.floor(Math.random() * quotes.length);
        }

        lastIndex = index;
        return quotes[index];
    };

    const playNextQuote = () => {
        if (!marqueeText || quotes.length === 0) {
            return;
        }

        const nextQuote = getRandomQuote();
        const durationInSeconds = Math.min(24, Math.max(10, nextQuote.length * 0.15));

        quoteMarquee.style.setProperty('--marquee-duration', `${durationInSeconds}s`);
        marqueeText.textContent = nextQuote;
        marqueeText.classList.remove('is-animating');

        void marqueeText.offsetWidth;

        marqueeText.classList.add('is-animating');
    };

    if (marqueeText && quotes.length > 0) {
        marqueeText.addEventListener('animationend', playNextQuote);
        playNextQuote();
    }
}

