function resizeGridItem(item) {
    const grid = item.closest(".projects-masonry");
    if (!grid) return;

    const rowHeight = parseInt(getComputedStyle(grid).getPropertyValue("grid-auto-rows"), 10);
    const rowGap = parseInt(getComputedStyle(grid).getPropertyValue("gap"), 10);

    const rowSpan = Math.ceil(
        (item.getBoundingClientRect().height + rowGap) / (rowHeight + rowGap)
    );

    item.style.setProperty("--span", rowSpan);
}

function resizeGrid(grid) {
    grid.querySelectorAll(":scope > .card").forEach((item) => resizeGridItem(item));
}

function resizeAllGridItems() {
    document.querySelectorAll(".projects-masonry").forEach((grid) => resizeGrid(grid));
}

window.addEventListener("load", resizeAllGridItems);
window.addEventListener("resize", resizeAllGridItems);

document.querySelectorAll(".projects-masonry img").forEach((img) => {
    if (!img.complete) {
        img.addEventListener("load", resizeAllGridItems);
    }
});