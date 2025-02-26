from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse
from .models import Post, Comment
from .forms import CommentForm

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "blog/blog.html"
    paginate_by = 6

def post_detail(request, slug):
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    # Fetch both approved comments + pending comments for the logged-in author without Q()
    if request.user.is_authenticated:
        comments = post.comments.filter(approved=True) | post.comments.filter(author=request.user)
    else:
        comments = post.comments.filter(approved=True)

    comments = comments.order_by("-created_on")
    comment_count = comments.count()
    comment_form = CommentForm()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()

            # Success message
            messages.success(request, "Comment submitted and awaiting approval")

            # Return JSON response for AJAX
            return JsonResponse({
                "status": "success",
                "message": "Comment submitted and awaiting approval",
                "new_comment": {
                    "author": comment.author.username,
                    "created_on": comment.created_on.strftime("%b. %d, %Y, %I:%M %p").lstrip("0"),
                    "body": comment.body,
                    "approved": comment.approved,
                }
            })

        else:
            # Handle form errors
            return JsonResponse({
                "status": "error",
                "message": "Form validation failed. Please try again.",
                "errors": comment_form.errors,
            }, status=400)

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
    View to edit comments
    """
    if request.method == "POST":
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)

        if comment.author != request.user:
            messages.error(request, "You can only edit your own comments!")
            return HttpResponseRedirect(reverse('post_detail', args=[slug]))

        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False  # Reset approval after edit
            comment.save()
            messages.success(request, "Comment updated and awaiting approval!")

            return JsonResponse({
                "status": "success",
                "message": "Comment updated and awaiting approval",
                "updated_comment_id": comment.id
            })
        else:
            return JsonResponse({
                "status": "error",
                "message": "Error updating comment",
                "errors": comment_form.errors
            }, status=400)

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))
