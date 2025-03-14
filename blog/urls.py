from django.urls import path
from . import views  # Import all views at once

urlpatterns = [
    path('', views.PostList.as_view(), name='blog'),
    path('<slug:slug>/', views.post_detail, name="post_detail"),
    path('<slug:slug>/edit_comment/<int:comment_id>/', views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>/', views.comment_delete, name='comment_delete'),
    path('<slug:slug>/like/', views.like_post, name="like_post"),

]
