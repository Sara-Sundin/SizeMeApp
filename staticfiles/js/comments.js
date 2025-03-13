document.addEventListener("DOMContentLoaded", function () {
    // Ensure delete modal exists before initializing
    let deleteModalElement = document.getElementById("deleteModal");
    let deleteConfirm = document.getElementById("deleteConfirm");

    if (deleteModalElement) {
        let deleteModal = new bootstrap.Modal(deleteModalElement, {
            backdrop: "static",
            keyboard: true
        });

        document.body.addEventListener("click", function (event) {
            if (event.target.classList.contains("btn-delete")) {
                event.preventDefault();
                let commentId = event.target.getAttribute("comment_id") ||
                                event.target.closest(".btn-delete").getAttribute("comment_id");

                if (commentId) {
                    deleteConfirm.href = `delete_comment/${commentId}`;
                    deleteModal.show();
                }
            }
        });
    }

    // Handle comment editing with smooth scroll
    let editButtons = document.querySelectorAll(".btn-edit");
    let commentText = document.getElementById("id_body");
    let commentForm = document.getElementById("commentForm");
    let submitButton = document.getElementById("submitButton");

    editButtons.forEach(button => {
        button.addEventListener("click", function (event) {
            event.preventDefault();

            let commentId = button.getAttribute("comment_id");
            let commentContentElement = document.getElementById(`comment${commentId}`);

            if (commentContentElement && commentText) {
                // Populate the form with the comment text
                commentText.value = commentContentElement.innerText.trim();
                submitButton.innerText = "Update";
                commentForm.setAttribute("action", `edit_comment/${commentId}`);

                // Smoothly scroll to the comment form
                let commentFormElement = document.getElementById("commentForm");
                if (commentFormElement) {
                    commentFormElement.scrollIntoView({ behavior: "smooth", block: "center" });
                }
            }
        });
    });
});
