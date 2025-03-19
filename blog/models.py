from django.db import models
from django.conf import settings
from cloudinary.models import CloudinaryField  # Import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    """
    Model representing a blog post.

    Attributes:
        title (str): The title of the post (unique).
        slug (str): URL-friendly identifier (unique).
        author (User): The user who wrote the post.
        content (str): The main body of the post.
        featured_image (CloudinaryField): Optional image for the post.
        created_on (datetime): Timestamp when post was created.
        updated_on (datetime): Timestamp when post was last updated.
        excerpt (str): Short summary of the post.
        status (int): Draft (0) or Published (1).
        likes (ManyToManyField): Users who liked the post.
    """

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # Use CustomUser dynamically
        on_delete=models.CASCADE,
        related_name="blog_posts"
    )
    content = models.TextField()
    featured_image = CloudinaryField(
        "blog_images", blank=True, null=True
    )  # Cloudinary field for images
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    excerpt = models.TextField(blank=True)
    status = models.IntegerField(choices=STATUS, default=0)

    # Likes Feature
    likes = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="post_likes", blank=True
    )

    class Meta:
        ordering = ["-created_on"]

    def total_likes(self):
        """Return the total number of likes for the post."""
        return self.likes.count()

    def __str__(self):
        """Return a readable representation of the post."""
        return f"{self.title} | written by {self.author}"


class Comment(models.Model):
    """
    Model representing a comment on a blog post.

    Attributes:
        post (Post): The blog post the comment belongs to.
        author (User): The user who wrote the comment.
        body (str): The text content of the comment.
        created_on (datetime): Timestamp when comment was created.
        approved (bool): Whether the comment is approved for display.
    """

    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments"
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name="commenter"
    )
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        """Return a readable representation of the comment."""
        return f"Comment {self.body[:30]}... by {self.author}"
