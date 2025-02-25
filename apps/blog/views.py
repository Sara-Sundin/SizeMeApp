from django.shortcuts import render
from django.views import generic
from .models import Post

class PostList(generic.ListView):
    queryset = Post.objects.all()
    template_name = "blog/blog_list.html"

def blog_list(request):
    return render(request, "blog/blog_list.html")
