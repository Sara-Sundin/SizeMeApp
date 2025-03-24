from django.test import TestCase
from django.contrib.admin.sites import site
from django.contrib.auth import get_user_model
from .models import Post, Comment
from .admin import PostAdmin, CommentAdmin


class AdminRegistrationTests(TestCase):
    def test_post_admin_is_registered(self):
        self.assertIn(Post, site._registry)
        self.assertIsInstance(site._registry[Post], PostAdmin)

    def test_comment_admin_is_registered(self):
        self.assertIn(Comment, site._registry)
        self.assertIsInstance(site._registry[Comment], CommentAdmin)


class AdminViewTests(TestCase):
    def setUp(self):
        self.User = get_user_model()
        self.admin_user = self.User.objects.create_superuser(
            username="admin", password="pass1234", email="admin@example.com"
        )
        self.client.login(username="admin", password="pass1234")

        self.post = Post.objects.create(
            title="Test Post",
            slug="test-post",
            content="Some content",
            status=1
        )




