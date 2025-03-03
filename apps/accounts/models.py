from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    profile_picture = models.ImageField(upload_to="avatars/", blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)  # Renamed field
    email = models.EmailField(unique=True)
    chest = models.FloatField(blank=True, null=True)
    waist = models.FloatField(blank=True, null=True)
    hips = models.FloatField(blank=True, null=True)
    shoulders = models.FloatField(blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]  # Keep 'username' if AbstractUser requires it
