from django import forms
from django.contrib.auth.forms import UserChangeForm
from allauth.account.forms import SignupForm
from .models import CustomUser 

class CustomSignupForm(SignupForm):
    """Custom Signup Form that requires name, email, and password, with name first."""
    
    name = forms.CharField(
        max_length=255, 
        required=True, 
        label="Name", 
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter your full name"})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Force placeholders for all fields
        self.fields["email"].widget.attrs["placeholder"] = "Enter your email"
        self.fields["password1"].widget.attrs["placeholder"] = "Password (must be at least 8 characters)"
        self.fields["password1"].widget.attrs["class"] = "form-control"  # Ensure consistent styling

        # Reordering fields so that 'name' appears first
        self.fields = {
            "name": self.fields["name"],
            "email": self.fields["email"],
            "password1": self.fields["password1"],
        }

    def save(self, request):
        """Save user and store their name."""
        user = super().save(request)  
        user.name = self.cleaned_data.get("name")  
        user.save()
        return user


class CustomUserUpdateForm(UserChangeForm):
    """Form for updating user profile without changing password."""
    
    password = None  # Hide password field in the form

    class Meta:
        model = CustomUser
        fields = ["profile_picture", "name", "email", "chest", "waist", "hips", "shoulders"]
