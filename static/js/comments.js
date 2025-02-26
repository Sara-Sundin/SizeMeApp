document.addEventListener("DOMContentLoaded", function () {
    const commentForm = document.getElementById("commentForm");
    const commentText = document.getElementById("id_body");
    const submitButton = document.getElementById("submitButton");

    /**
     * Attach event listeners to edit buttons dynamically.
     */
    function attachEditListeners() {
        document.querySelectorAll(".btn-edit").forEach(button => {
            button.removeEventListener("click", handleEditClick); // Prevent duplicates
            button.addEventListener("click", handleEditClick);
        });
    }

    /**
     * Handle edit button click - Load comment into form for editing.
     */
    function handleEditClick(event) {
        let commentId = event.target.getAttribute("data-comment-id");

        // Error Handling: Ensure we have a valid comment ID
        if (!commentId) {
            console.error("Comment ID is null or undefined");
            return;
        }

        // Corrected: Select the comment body using the correct ID format
        let commentBodyElement = document.getElementById(`comment-body-${commentId}`);

        // Error Handling: Ensure the comment body exists
        if (!commentBodyElement) {
            console.error(`Comment body not found for comment ID ${commentId}`);
            return;
        }

        let commentContent = commentBodyElement.innerText.trim();

        // Set the form to edit mode
        commentText.value = commentContent;
        submitButton.innerText = "Update";
        commentForm.dataset.commentId = commentId;

        // Scroll smoothly to form
        commentText.focus();
        window.scrollTo({ top: commentForm.offsetTop - 50, behavior: "smooth" });
    }

    attachEditListeners(); // Attach listeners on page load

    /**
     * Handle comment submission (new and edited comments).
     */
    commentForm.addEventListener("submit", function (e) {
        e.preventDefault();

        let commentId = commentForm.dataset.commentId || null;
        let formData = new FormData(commentForm);
        let postSlug = document.getElementById("comments-list").dataset.postSlug;
        let actionUrl = commentId
            ? `/blog/${postSlug}/edit_comment/${commentId}/`
            : `/blog/${postSlug}/`;

        fetch(actionUrl, {
            method: "POST",
            body: formData,
            headers: {
                'X-CSRFToken': getCookie('csrftoken'),
            }
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === "success") {
                if (commentId) {
                    // Remove the previous version of the comment
                    let existingComment = document.getElementById(`comment-${commentId}`);
                    if (existingComment) {
                        existingComment.remove();
                    }

                    // Append updated comment dynamically
                    let updatedCommentHtml = `
                        <div class="p-2 comments faded" id="comment-${commentId}">
                            <p class="font-weight-bold">${data.updated_author}
                                <span class="font-weight-normal">${data.updated_created_on}</span> wrote:
                            </p>
                            <div class="comment-body" id="comment-body-${commentId}">${data.updated_body}</div>
                            <p class="approval">This comment is awaiting approval</p>
                            <button class="btn btn-edit" data-comment-id="${commentId}">Edit</button>
                        </div>
                    `;
                    document.getElementById("comments-list").insertAdjacentHTML("afterbegin", updatedCommentHtml);
                    attachEditListeners(); // Reattach listeners
                }

                // Reset form after submission
                commentForm.reset();
                submitButton.innerText = "Submit";
                delete commentForm.dataset.commentId;
            }
        })
        .catch(error => console.error("Error:", error));
    });

    /**
     * CSRF token helper function
     */
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                let cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});
