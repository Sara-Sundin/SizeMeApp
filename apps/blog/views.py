from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib import messages
from django.http import JsonResponse  # Ensure this import is added
from .models import Post
from .forms import CommentForm

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "blog/blog.html"
    paginate_by = 6

def post_detail(request, slug):
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.filter(approved=True).order_by("-created_on")
    comment_count = comments.count()

    comment_form = CommentForm()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()

            #  Add Success Message
            messages.success(request, "Comment submitted and awaiting approval")

            #  Return JSON response for AJAX
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
            #  Handle form errors
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
