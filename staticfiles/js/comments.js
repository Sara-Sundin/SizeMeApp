document.addEventListener("DOMContentLoaded", function () {
    // Ensure delete modal exists before initializing
    let deleteModalElement = document.getElementById("deleteModal");
    let deleteConfirm = document.getElementById("deleteConfirm");

    if (deleteModalElement) {
        let deleteModal = new bootstrap.Modal(deleteModalElement, {
            backdrop: "static", // Prevents accidental closing
            keyboard: true      // Allows closing via keyboard
        });

        document.body.addEventListener("click", function (event) {
            // Check if a delete button was clicked
            if (event.target.classList.contains("btn-delete")) {
                event.preventDefault();

                // Ensure we get the correct comment ID (handle event bubbling)
                let commentId = event.target.getAttribute("comment_id") ||
                                event.target.closest(".btn-delete").getAttribute("comment_id");

                if (commentId) {
                    deleteConfirm.href = `delete_comment/${commentId}`;
                    deleteModal.show();
                }
            }
        });
    }

    // Ensure edit functionality works properly
    let editButtons = document.getElementsByClassName("btn-edit");
    let commentText = document.getElementById("id_body");
    let commentForm = document.getElementById("commentForm");
    let submitButton = document.getElementById("submitButton");

    for (let button of editButtons) {
        button.addEventListener("click", function (event) {
            event.preventDefault();
            
            let commentId = event.target.getAttribute("comment_id") ||
                            event.target.closest(".btn-edit").getAttribute("comment_id");

            let commentContentElement = document.getElementById(`comment${commentId}`);
            if (commentContentElement && commentText) {
                commentText.value = commentContentElement.innerText.trim();
                submitButton.innerText = "Update";
                commentForm.setAttribute("action", `edit_comment/${commentId}`);
            }
        });
    }
});
