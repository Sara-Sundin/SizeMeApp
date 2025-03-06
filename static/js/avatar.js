/* jshint esversion: 6 */

// Canvas layers setup
const canvases = {
    base: document.getElementById("canvas-base"),
    head: document.getElementById("canvas-head"),
    eyes: document.getElementById("canvas-eyes"),
    mouth: document.getElementById("canvas-mouth"),
    ears: document.getElementById("canvas-ears"),
    rods: document.getElementById("canvas-rods"),
};

// Contexts for each canvas layer
const contexts = Object.fromEntries(
    Object.entries(canvases).map(([key, canvas]) => [key, canvas.getContext("2d", { willReadFrequently: true })])
);

// Stores the currently selected layer images
const layers = Object.keys(canvases).reduce((acc, key) => ({ ...acc, [key]: null }), {});

// Initializes all canvases
function initializeCanvases() {
    Object.values(canvases).forEach((canvas) => {
        canvas.width = 400;
        canvas.height = 400;
    });

    // Ensure the main thumbnails are visible at start
    document.getElementById("main-thumbnails").classList.add("visible");
}

// Load and draw a single layer
function loadAndDrawLayer(layerName) {
    const ctx = contexts[layerName];
    const src = layers[layerName];
    if (!ctx) return;

    if (!src) {
        ctx.clearRect(0, 0, canvases[layerName].width, canvases[layerName].height);
        return;
    }

    const img = new Image();
    img.src = src;
    img.onload = () => {
        ctx.clearRect(0, 0, canvases[layerName].width, canvases[layerName].height);
        ctx.drawImage(img, 0, 0, canvases[layerName].width, canvases[layerName].height);
    };
}

// **Main Thumbnails Handling**
function handleThumbnailSelection() {
    document.querySelectorAll(".thumbnail-radio.main-thumbnail").forEach((radio) => {
        radio.addEventListener("change", (e) => {
            const layer = e.target.dataset.layer;
            const src = e.target.dataset.src;

            if (layer) {
                layers[layer] = src;
                loadAndDrawLayer(layer);
            }

            // Hide all additional thumbnails first
            document.querySelectorAll(".additional-thumbnails").forEach((el) => {
                el.classList.add("hidden");
            });

            // Show only the additional thumbnails for the selected layer
            const additionalThumbnails = document.getElementById(`additional-thumbnails-${layer}`);
            if (additionalThumbnails) {
                additionalThumbnails.classList.remove("hidden");

                // **Use the visible class to hide main thumbnails**
                document.getElementById("main-thumbnails").classList.remove("visible");
            } else {
                // **If no additional thumbnails exist, keep main thumbnails visible**
                document.getElementById("main-thumbnails").classList.add("visible");
            }
        });
    });
}

// **Back Button Handling**
function setupBackButtons() {
    document.querySelectorAll(".back-button").forEach((button) => {
        button.addEventListener("click", () => {
            // Hide all additional thumbnails
            document.querySelectorAll(".additional-thumbnails").forEach((el) => {
                el.classList.add("hidden");
            });

            // **Use the visible class to show main thumbnails**
            document.getElementById("main-thumbnails").classList.add("visible");
        });
    });
}

// **Reset Button Handling**
function resetCanvas() {
    Object.keys(canvases).forEach((layer) => {
        const ctx = contexts[layer];
        if (ctx) {
            ctx.clearRect(0, 0, canvases[layer].width, canvases[layer].height);
            layers[layer] = null;
        }
    });

    document.querySelectorAll(".thumbnail-radio").forEach((radio) => (radio.checked = false));

    // **Ensure main thumbnails are visible and additional ones are hidden**
    document.getElementById("main-thumbnails").classList.add("visible");
    document.querySelectorAll(".additional-thumbnails").forEach((el) => {
        el.classList.add("hidden");
    });
}

// **Event Listeners**
document.getElementById("reset-button").addEventListener("click", resetCanvas);

// **Initialize Everything**
document.addEventListener("DOMContentLoaded", () => {
    initializeCanvases();
    handleThumbnailSelection();
    setupBackButtons();
});
