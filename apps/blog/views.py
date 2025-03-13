from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import CommentForm

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "blog/blog.html"
    paginate_by = 6

def post_detail(request, slug):
    """
    Display an individual post along with comments.
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.success(request, "Comment submitted and awaiting approval.")
            return HttpResponseRedirect(reverse("post_detail", args=[slug]) + "#message-container")

    else:
        comment_form = CommentForm()

    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )

def comment_edit(request, slug, comment_id):
    """
    View to edit comments and redirect based on action:
    - When clicking "Edit" → Redirect to #commentForm
    - When updating comment → Redirect to #message-container
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST, instance=comment)
        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False  # Require re-approval
            comment.save()
            messages.success(request, "Comment updated successfully!")

            # Redirect to #message-container after updating
            return HttpResponseRedirect(reverse("post_detail", args=[slug]) + "#message-container")
        else:
            messages.error(request, "Error updating comment!")

    # If GET request or form is invalid, redirect back to #commentForm
    return HttpResponseRedirect(reverse("post_detail", args=[slug]) + "#commentForm")

def comment_delete(request, slug, comment_id):
    """
    View to delete comment and redirect to message-container.
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.success(request, "Comment deleted!")
    else:
        messages.error(request, "You can only delete your own comments!")

    return HttpResponseRedirect(reverse("post_detail", args=[slug]) + "#message-container")
