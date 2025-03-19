from cloudinary.models import CloudinaryField
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """Custom user model with profile picture stored in Cloudinary."""

    profile_picture = CloudinaryField(
        "profile_pictures", blank=True, null=True
    )

    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(unique=True)
    chest = models.FloatField(blank=True, null=True)
    waist = models.FloatField(blank=True, null=True)
    hips = models.FloatField(blank=True, null=True)
    shoulders = models.FloatField(blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def get_full_name(self):
        """Return the user's full name or email if name is missing."""
        return self.name if self.name else self.email

    def get_short_name(self):
        """Return the first word of the user's name or fallback to email."""
        return self.name.split()[0] if self.name else self.email

    def __str__(self):
        """Use the short name for display."""
        return self.get_short_name()
