from django.contrib import admin, messages
from django.core.mail import send_mail
from django import forms
from .models import Newsletter, Subscriber

class NewsletterAdminForm(forms.ModelForm):
    """Extend the admin form to add email sending fields."""
    send_to_email = forms.EmailField(
        required=False,
        help_text="Enter an email to send to a single recipient, or leave blank to send to all subscribers.",
    )
    subject = forms.CharField(
        required=True,
        help_text="Enter the subject of the email.",
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 5}),
        required=True,
        help_text="Enter the content of the email."
    )

    class Meta:
        model = Newsletter
        fields = ["title", "content", "sent"]

class NewsletterAdmin(admin.ModelAdmin):
    form = NewsletterAdminForm
    list_display = ("title", "sent", "created_on", "send_newsletter_action")
    search_fields = ("title", "content")
    list_filter = ("sent", "created_on")

    def save_model(self, request, obj, form, change):
        """Send the newsletter email when saving the form."""
        super().save_model(request, obj, form, change)  # Save the newsletter instance

        subject = form.cleaned_data.get("subject")
        message = form.cleaned_data.get("message")
        email = form.cleaned_data.get("send_to_email")

        if email:
            recipients = [email]  # Send to a single recipient
        else:
            recipients = Subscriber.objects.values_list("email", flat=True)  # Send to all subscribers

        if recipients:
            send_mail(
                subject,
                message,
                "sara@sizemeapp.se",  # My email
                list(recipients),
                fail_silently=False,
            )
            obj.sent = True  # Mark as sent
            obj.save()
            messages.success(request, "Newsletter sent successfully!")

    def send_newsletter_action(self, obj):
        return "Click edit to send"

    send_newsletter_action.short_description = "Send Newsletter"

admin.site.register(Newsletter, NewsletterAdmin)

@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ("email", "subscribed_at")
    search_fields = ("email",)
    list_filter = ("subscribed_at",)
