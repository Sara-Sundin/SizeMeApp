from django import forms
from django.contrib.auth.forms import UserChangeForm
from accounts.models import CustomUser

class CustomUserUpdateForm(UserChangeForm):
    password = None  # Hide password field in the form

    class Meta:
        model = CustomUser
        fields = ["profile_picture", "name", "email", "chest", "waist", "hips", "shoulders"]
