from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from blog.models import Post, Comment  # Replace 'blog' with your app name


class BlogViewTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpass123',
            email='test@example.com'
        )
        self.post = Post.objects.create(
            title='Test Post',
            slug='test-post',
            content='Test content',
            author=self.user,
            status=1
        )

    def test_post_list_view_status_code(self):
        response = self.client.get(reverse("post_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Post")

    def test_post_detail_view(self):
        response = self.client.get(reverse("post_detail", args=[self.post.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.post.title)

    def test_like_post_authenticated_user(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse("like_post", args=[self.post.slug]))
        self.assertRedirects(response, reverse("post_detail", args=[self.post.slug]) + "#like-button")
        self.assertTrue(self.post.likes.filter(id=self.user.id).exists())

    def test_like_post_unauthenticated_user(self):
        response = self.client.get(reverse("like_post", args=[self.post.slug]))
        self.assertRedirects(response, reverse("post_detail", args=[self.post.slug]) + "#like-button")
        self.assertFalse(self.post.likes.exists())


class CommentViewTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="commenter",
            password="testpass123",
            email="commenter@example.com"
        )
        self.post = Post.objects.create(
            title='Comment Post',
            slug='comment-post',
            content='Some content',
            author=self.user,
            status=1
        )
        self.comment = Comment.objects.create(
            post=self.post,
            author=self.user,
            body='Test comment',
            approved=True
        )

    def test_comment_submission(self):
        self.client.login(username="commenter", password="testpass123")
        response = self.client.post(
            reverse("post_detail", args=[self.post.slug]),
            {"body": "A new comment"}
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Comment.objects.count(), 2)

    def test_comment_edit_by_author(self):
        self.client.login(username="commenter", password="testpass123")
        response = self.client.post(
            reverse("comment_edit", args=[self.post.slug, self.comment.id]),
            {"body": "Updated comment"}
        )
        self.comment.refresh_from_db()
        self.assertEqual(self.comment.body, "Updated comment")
        self.assertFalse(self.comment.approved)

    def test_comment_delete_by_author(self):
        self.client.login(username="commenter", password="testpass123")
        response = self.client.post(
            reverse("comment_delete", args=[self.post.slug, self.comment.id])
        )
        self.assertFalse(Comment.objects.filter(id=self.comment.id).exists())
