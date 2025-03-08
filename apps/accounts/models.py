from django.contrib.auth.models import AbstractUser
from django.db import models
from cloudinary.models import CloudinaryField
import os

class CustomUser(AbstractUser):
    """Custom user model with profile picture handling for local & production."""

    # Use Cloudinary for production, local storage for development
    if "DYNO" in os.environ:  # Running on Heroku (Production)
        profile_picture = CloudinaryField("profile_pictures", blank=True, null=True)
    else:  # Local development
        profile_picture = models.ImageField(upload_to="media/avatars/", blank=True, null=True)

    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(unique=True)
    chest = models.FloatField(blank=True, null=True)
    waist = models.FloatField(blank=True, null=True)
    hips = models.FloatField(blank=True, null=True)
    shoulders = models.FloatField(blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def save(self, *args, **kwargs):
        """Ensure only the first name is stored when saving."""
        if self.name and " " in self.name:
            self.name = self.name.split()[0]
        super().save(*args, **kwargs)

    def __str__(self):
        """String representation of the user."""
        return self.name or self.email
