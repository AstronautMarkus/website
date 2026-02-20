document.addEventListener('DOMContentLoaded', function () {
    const tabButtons = document.querySelectorAll('section.tabs [role="tab"]');
    const tabPanels = document.querySelectorAll('section.tabs [role="tabpanel"]');

    tabButtons.forEach((button, idx) => {
        button.addEventListener('click', function () {

            tabButtons.forEach(btn => {
                btn.setAttribute('aria-selected', 'false');
            });

            tabPanels.forEach(panel => {
                panel.setAttribute('hidden', 'true');
            });

            button.setAttribute('aria-selected', 'true');

            const panelId = button.getAttribute('aria-controls');
            const panel = document.getElementById(panelId);
            if (panel) {
                panel.removeAttribute('hidden');
            }
        });
    });
});
