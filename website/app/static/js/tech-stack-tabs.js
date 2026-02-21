document.addEventListener('DOMContentLoaded', function () {
	const techStackTabsSection = document.querySelector('section.tabs.techstack-tabs');
	if (!techStackTabsSection) {
		return;
	}

	const tabButtons = techStackTabsSection.querySelectorAll('[role="tab"]');
	const tabPanels = techStackTabsSection.querySelectorAll('[role="tabpanel"]');

	tabButtons.forEach((button) => {
		button.addEventListener('click', function () {
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
		});
	});
});
