from django import forms
from django.contrib.auth.forms import UserChangeForm
from accounts.models import CustomUser


class CustomUserUpdateForm(UserChangeForm):
    """
    A form for updating user profile details.

    This form allows users to edit their profile information,
    excluding the password field to prevent unintended changes.
    """

    password = None  # Hide password field in the form

    class Meta:
        model = CustomUser
        fields = [
            "profile_picture",
            "name",
            "email",
            "chest",
            "waist",
            "hips",
            "shoulders",
        ]
