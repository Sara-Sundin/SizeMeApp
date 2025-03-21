from django import forms
from django.contrib.auth.forms import UserChangeForm
from allauth.account.forms import SignupForm
from .models import CustomUser


class CustomSignupForm(SignupForm):
    """
    Custom Signup Form that requires name, email,
    and password, with name first and styled inputs.
    """

    name = forms.CharField(
        max_length=255,
        required=True,
        label="Name",
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter your full name",
        }),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Add styling and placeholders
        self.fields["email"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Enter your email"
        })

        self.fields["password1"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Password (must be at least 8 characters)"
        })

        self.fields["password2"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Confirm your password"
        })

        # Reorder the fields to show 'name' first
        self.order_fields(["name", "email", "password1", "password2"])

    def save(self, request):
        """Save user and store their name."""
        user = super().save(request)
        user.name = self.cleaned_data.get("name")
        user.save()
        return user


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
        widgets = {
            "profile_picture": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "chest": forms.NumberInput(attrs={"class": "form-control"}),
            "waist": forms.NumberInput(attrs={"class": "form-control"}),
            "hips": forms.NumberInput(attrs={"class": "form-control"}),
            "shoulders": forms.NumberInput(attrs={"class": "form-control"}),
        }
