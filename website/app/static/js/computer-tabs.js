document.addEventListener('DOMContentLoaded', function () {
    const computerTabsSection = document.querySelector('section.computer-tabs');
    if (!computerTabsSection) {
        return;
    }

    const tabButtons = computerTabsSection.querySelectorAll('[role="tab"]');
    const tabPanels = computerTabsSection.querySelectorAll('[role="tabpanel"]');

    const setActiveTab = function (button) {
        tabButtons.forEach((btn) => {
            btn.setAttribute('aria-selected', 'false');
        });

        tabPanels.forEach((panel) => {
            panel.setAttribute('hidden', 'true');
        });

        button.setAttribute('aria-selected', 'true');

        const panelId = button.getAttribute('aria-controls');
        const panel = document.getElementById(panelId);
        if (panel) {
            panel.removeAttribute('hidden');
        }
    };

    const defaultTabButton = computerTabsSection.querySelector('[aria-controls="computer-tab-9"]');
    if (defaultTabButton) {
        setActiveTab(defaultTabButton);
    }

    tabButtons.forEach((button) => {
        button.addEventListener('click', function () {
            setActiveTab(button);
        });
    });
});
