from cloudinary.models import CloudinaryField
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    """Custom user model with profile picture stored in Cloudinary."""

    profile_picture = CloudinaryField("profile_pictures", blank=True, null=True)

    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(unique=True)
    chest = models.FloatField(blank=True, null=True)
    waist = models.FloatField(blank=True, null=True)
    hips = models.FloatField(blank=True, null=True)
    shoulders = models.FloatField(blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.name or self.email
