from django import forms
from newsletter.models import Subscriber


class SubscriberForm(forms.ModelForm):
    """
    Form for newsletter subscription.

    Allows users to enter their email to subscribe to the newsletter.
    Uses a styled email input field for better user experience.
    """

    class Meta:
        model = Subscriber
        fields = ["email"]
        widgets = {
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter your email"
                }
            ),
        }
