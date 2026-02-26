const earthImage = document.querySelector('.earth-image');
const moonImage = document.querySelector('.moon-image');

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