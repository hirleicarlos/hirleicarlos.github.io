// Masonry via CSS Grid row-span
(function () {
    function layoutMasonry(container) {
        if (!container) return;

        const rowHeight = parseFloat(getComputedStyle(document.documentElement).getPropertyValue('--masonryRow')) || 10;
        const gap = parseFloat(getComputedStyle(container).gap) || 14;

        const items = container.querySelectorAll('.card, article.card');
        items.forEach((item) => {
            // reset antes de medir
            item.style.setProperty('--masonrySpan', 1);

            // altura real do item
            const h = item.getBoundingClientRect().height;

            // span = (altura + gap) / (rowHeight + gapUnit)
            const span = Math.ceil((h + gap) / (rowHeight + gap));
            item.style.setProperty('--masonrySpan', span);
        });
    }

    function relayoutAll() {
        document.querySelectorAll('[data-masonry]').forEach(layoutMasonry);
    }

    // 1) no load
    window.addEventListener('load', relayoutAll);

    // 2) no resize (leve debounce)
    let t = null;
    window.addEventListener('resize', () => {
        clearTimeout(t);
        t = setTimeout(relayoutAll, 120);
    });

    // 3) quando imagens carregarem (importante!)
    document.addEventListener('DOMContentLoaded', () => {
        document.querySelectorAll('[data-masonry] img').forEach((img) => {
            if (img.complete) return;
            img.addEventListener('load', relayoutAll, { once: true });
            img.addEventListener('error', relayoutAll, { once: true });
        });
    });
})();