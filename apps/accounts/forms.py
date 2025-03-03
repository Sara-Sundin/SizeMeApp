from django import forms
from django.contrib.auth.forms import UserChangeForm
from allauth.account.forms import SignupForm
from .models import CustomUser 

from django import forms
from allauth.account.forms import SignupForm
from .models import CustomUser 

class CustomSignupForm(SignupForm):
    """Custom Signup Form that requires name, email, and password, with name first."""
    
    name = forms.CharField(max_length=255, required=True, label="Name")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Reordering fields so that 'name' appears first
        self.fields = {
            "name": self.fields["name"],
            "email": self.fields["email"],
            "password1": self.fields["password1"],
            "password2": self.fields["password2"],
        }

    def save(self, request):
        user = super().save(request)  # Saves email and password
        user.name = self.cleaned_data.get("name")  # Save name
        user.save()
        return user


class CustomUserUpdateForm(UserChangeForm):
    password = None  # Hide password field in the form

    class Meta:
        model = CustomUser
        fields = ["profile_picture", "name", "email", "chest", "waist", "hips", "shoulders"]
