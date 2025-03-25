/* jshint esversion: 9 */

// Wait until the entire DOM is loaded before running the script
document.addEventListener("DOMContentLoaded", function() {

    // Get the button that toggles the measurements section
    const toggleButton = document.getElementById("toggle-measurements");

    // Get the section that contains the measurement inputs or data
    const measurementsSection = document.getElementById("measurements-section");

    // Add a click event listener to the toggle button
    toggleButton.addEventListener("click", function() {

        // Check if the measurements section is hidden (either via style or CSS class)
        if (measurementsSection.style.display === "none" || measurementsSection.classList.contains("hidden")) {
            
            // If hidden, show the section
            measurementsSection.style.display = "block";
            measurementsSection.classList.remove("hidden");

            // Change button text to indicate user can hide it
            toggleButton.textContent = "Hide Measurements";

        } else {
            // If visible, hide the section
            measurementsSection.style.display = "none";

            // Change button text to indicate user can show it
            toggleButton.textContent = "Show Measurements";
        }
    });
});
