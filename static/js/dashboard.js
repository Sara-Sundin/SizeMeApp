/* jshint esversion: 9 */

document.addEventListener("DOMContentLoaded", function() {
    const toggleButton = document.getElementById("toggle-measurements");
    const measurementsSection = document.getElementById("measurements-section");

    toggleButton.addEventListener("click", function() {
        if (measurementsSection.style.display === "none" || measurementsSection.classList.contains("hidden")) {
            measurementsSection.style.display = "block";
            measurementsSection.classList.remove("hidden");
            toggleButton.textContent = "Hide Measurements";
        } else {
            measurementsSection.style.display = "none";
            toggleButton.textContent = "Show Measurements";
        }
    });
});