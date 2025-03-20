from django.db import models


class Newsletter(models.Model):
    """
    Model representing a newsletter.

    Stores the title, content, creation date, and a flag indicating
    whether the newsletter has been sent.
    """

    title = models.CharField(max_length=255)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    sent = models.BooleanField(default=False)

    def __str__(self):
        """Return the title of the newsletter."""
        return self.title


class Subscriber(models.Model):
    """
    Model representing a newsletter subscriber.

    Stores the email of the subscriber and the date they subscribed.
    """

    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return the subscriber's email."""
        return self.email
