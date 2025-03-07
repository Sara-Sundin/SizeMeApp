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

// Filter out null values (elements that do not exist in the DOM)
Object.keys(canvases).forEach((key) => {
    if (!canvases[key]) {
        console.warn(`Canvas element not found for layer: ${key}`);
        delete canvases[key]; // Remove missing elements from the object
    }
});

// Contexts for each canvas layer (only for existing canvases)
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

// **Randomize Avatar**
function randomizeAvatar() {
    Object.keys(canvases).forEach((layer) => {
        const availableThumbnails = document.querySelectorAll(`.thumbnail-radio[data-layer="${layer}"]`);
        
        if (availableThumbnails.length > 0) {
            // Pick a random thumbnail for this layer
            const randomIndex = Math.floor(Math.random() * availableThumbnails.length);
            const randomThumbnail = availableThumbnails[randomIndex];

            // Update layer image and draw it
            layers[layer] = randomThumbnail.dataset.src;
            loadAndDrawLayer(layer);

            // Check the corresponding radio button
            randomThumbnail.checked = true;
        }
    });

    // Hide all additional thumbnails and show main thumbnails
    document.querySelectorAll(".additional-thumbnails").forEach((el) => el.classList.add("hidden"));
    const mainThumbnails = document.getElementById("main-thumbnails");
    if (mainThumbnails) {
        mainThumbnails.style.display = "flex";
    }
}

// **Handle Thumbnail Selection** (Main and Additional)
function handleThumbnailSelection() {
    document.querySelectorAll(".thumbnail-radio").forEach((radio) => {
        radio.addEventListener("change", (e) => {
            const layer = e.target.dataset.layer;
            const src = e.target.dataset.src;
            const isMainThumbnail = e.target.classList.contains("main-thumbnail");

            if (layer) {
                if (isMainThumbnail) {
                    if (layer === "base" || layer === "skin") {
                        layers[layer] = src;
                        loadAndDrawLayer(layer);
                    } else {
                        document.querySelectorAll(".additional-thumbnails").forEach((el) => el.classList.add("hidden"));

                        const additionalThumbnailsId = `additional-thumbnails-${layer}`;
                        const additionalThumbnails = document.getElementById(additionalThumbnailsId);
                        
                        if (additionalThumbnails) {
                            additionalThumbnails.classList.remove("hidden");
                            document.getElementById("main-thumbnails").style.display = "none"; // Hide main thumbnails
                        }
                    }
                } else {
                    layers[layer] = src;
                    loadAndDrawLayer(layer);
                }
            }
        });
    });
}

// **Apply Color to Active Layer**
function applyColorToActiveLayer() {
    document.querySelectorAll(".swatch").forEach((swatch) => {
        swatch.addEventListener("click", (e) => {
            const color = e.target.dataset.color;
            if (!color) return;
            const [r, g, b] = color.match(/\d+/g).map(Number);
            updateColor([r, g, b]);
        });
    });
}

// **Update selected avatar layer with chosen RGB color**
function updateColor(rgb) {
    const activeRadio = document.querySelector(".thumbnail-radio:checked");
    if (!activeRadio) return;

    const layer = activeRadio.dataset.layer;
    if (!layer || !layers[layer]) return;

    const ctx = contexts[layer];
    const canvas = canvases[layer];

    if (!ctx || !canvas) return;

    const img = new Image();
    img.src = layers[layer];

    img.onload = () => {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        ctx.drawImage(img, 0, 0, canvas.width, canvas.height);

        const imageData = ctx.getImageData(0, 0, canvas.width, canvas.height);
        const data = imageData.data;

        const whiteThreshold = 200; // Adjust sensitivity to change near-white colors
        for (let i = 0; i < data.length; i += 4) {
            if (data[i] > whiteThreshold && data[i + 1] > whiteThreshold && data[i + 2] > whiteThreshold) {
                [data[i], data[i + 1], data[i + 2]] = rgb;
            }
        }
        ctx.putImageData(imageData, 0, 0);
    };
}

// **Back Button Handling**
function setupBackButtons() {
    document.querySelectorAll(".back-button").forEach((button) => {
        button.addEventListener("click", () => {
            // Hide all additional thumbnails
            document.querySelectorAll(".additional-thumbnails").forEach((el) => el.classList.add("hidden"));

            // Ensure main thumbnails reappear
            const mainThumbnails = document.getElementById("main-thumbnails");
            if (mainThumbnails) {
                mainThumbnails.style.display = "flex"; // Show main thumbnails again
            }
        });
    });
}

// **Reset Button Handling**
function resetCanvas() {
    // Clear all canvas layers
    Object.keys(canvases).forEach((layer) => {
        const ctx = contexts[layer];
        if (ctx) {
            ctx.clearRect(0, 0, canvases[layer].width, canvases[layer].height);
            layers[layer] = null;
        }
    });

    // Uncheck all thumbnail selections
    document.querySelectorAll(".thumbnail-radio").forEach((radio) => (radio.checked = false));

    // Hide all additional thumbnails
    document.querySelectorAll(".additional-thumbnails").forEach((el) => el.classList.add("hidden"));

    // Ensure main thumbnails always reappear
    const mainThumbnails = document.getElementById("main-thumbnails");
    if (mainThumbnails) {
        mainThumbnails.style.display = "flex"; // Show main thumbnails
    }
}

// **Event Listeners**
document.getElementById("reset-button").addEventListener("click", resetCanvas);
document.getElementById("randomize-button").addEventListener("click", randomizeAvatar); // Add randomize event listener

// **Initialize Everything**
document.addEventListener("DOMContentLoaded", () => {
    initializeCanvases();
    handleThumbnailSelection();
    applyColorToActiveLayer();
    setupBackButtons();
});
