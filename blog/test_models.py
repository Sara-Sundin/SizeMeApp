from django.test import TestCase
from django.contrib.auth import get_user_model
from blog.models import Post, Comment
from django.utils import timezone


class PostModelTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@example.com',
            password='pass1234'
        )
        self.post = Post.objects.create(
            title='Test Post',
            slug='test-post',
            author=self.user,
            content='This is a test post.',
            excerpt='Short summary',
            status=1
        )

    def test_post_str_returns_title_and_author(self):
        expected = f"{self.post.title} | written by {self.user}"
        self.assertEqual(str(self.post), expected)

    def test_post_total_likes_initially_zero(self):
        self.assertEqual(self.post.total_likes(), 0)

    def test_post_total_likes_after_liking(self):
        self.post.likes.add(self.user)
        self.assertEqual(self.post.total_likes(), 1)

    def test_post_ordering(self):
        second_post = Post.objects.create(
            title='Another Post',
            slug='another-post',
            author=self.user,
            content='More content',
            status=1,
        )
        posts = Post.objects.all()
        self.assertEqual(posts[0], second_post)  # Most recent first


class CommentModelTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='commenter',
            email='commenter@example.com',
            password='pass1234'
        )
        self.post = Post.objects.create(
            title='Commented Post',
            slug='commented-post',
            author=self.user,
            content='Post content',
            status=1,
        )
        self.comment = Comment.objects.create(
            post=self.post,
            author=self.user,
            body='This is a comment.'
        )

    def test_comment_str_truncates_body(self):
        expected = f"Comment This is a comment.... by {self.user}"
        self.assertEqual(str(self.comment), expected)

    def test_comment_default_approval_false(self):
        self.assertFalse(self.comment.approved)

    def test_comment_related_name(self):
        self.assertIn(self.comment, self.post.comments.all())
