from django.urls import path
from .views import PostList, blog_list

urlpatterns = [
    path("", PostList.as_view(), name="blog_list"), 
]
