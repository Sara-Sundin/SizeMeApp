from django import forms
from django.contrib.auth.forms import UserChangeForm
from apps.accounts.models import CustomUser

class CustomUserUpdateForm(UserChangeForm):
    password = None  # Hide password field in the form

    class Meta:
        model = CustomUser
        fields = ["full_name", "email", "gender", "age", "chest", "waist", "hips", "shoulders", "profile_picture"]
