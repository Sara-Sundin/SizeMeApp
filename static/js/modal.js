document.addEventListener("DOMContentLoaded", function() {
    let modal = document.getElementById("avatar-modal");
    let openLink = document.getElementById("open-avatar-modal");
    let closeBtn = document.querySelector(".close-modal");

    // Open modal when clicking the link
    openLink.addEventListener("click", function(event) {
        event.preventDefault(); // Prevent the default anchor behavior
        modal.style.display = "block";
    });

    // Close modal when clicking the close button
    closeBtn.addEventListener("click", function() {
        modal.style.display = "none";
    });

    // Close modal when clicking outside of it
    window.addEventListener("click", function(event) {
        if (event.target === modal) {
            modal.style.display = "none";
        }
    });
});
