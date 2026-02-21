document.addEventListener('DOMContentLoaded', function () {
    const loreTabsSection = document.querySelector('section.tabs.lore-tabs');
    if (!loreTabsSection) {
        return;
    }

    const tabButtons = loreTabsSection.querySelectorAll('[role="tab"]');
    const tabPanels = loreTabsSection.querySelectorAll('[role="tabpanel"]');

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
