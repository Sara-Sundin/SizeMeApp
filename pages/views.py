from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from newsletter.forms import SubscriberForm  # Import the form


def index(request):
    """
    Display the home page with a newsletter subscription form.

    If the form is submitted via POST and is valid, the user is
    subscribed to the newsletter, and a success message is shown.
    """
    if request.method == "POST":
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, "You have successfully subscribed to our newsletter!"
            )
            return redirect("subscription_success")  # Redirect after success
    else:
        form = SubscriberForm()  # Initialize form only if GET request

    return render(request, "pages/index.html", {"form": form})

def about(request):
    """
    Display the About page.
    """
    return render(request, "pages/about.html")


def contact(request):
    """
    Handle contact form submissions.

    If a POST request is received with a valid name, email,
    and message, the email is sent to the administrator. If
    an error occurs, an error message is displayed.
    """

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        if name and email and message:
            try:
                send_mail(
                    subject=f"New Contact Form Submission from {name}",
                    message=(
                        f"Name: {name}\nEmail: {email}\n\n"
                        f"Message:\n{message}"
                    ),
                    from_email="noreply@sizemeapp.se",
                    recipient_list=["sara@sizemeapp.se"],  # Your email
                    fail_silently=False,
                )
                return redirect("contact_success")  # Redirect to success page
            except BadHeaderError:
                messages.error(
                    request,
                    "Invalid header found. Please try again."
                )
            except Exception:
                messages.error(
                    request,
                    "An error occurred while sending your message. "
                    "Please try again later."
                )

    return render(request, "pages/contact.html")


def contact_success(request):
    """
    Display the Contact Success page after a successful submission.
    """
    return render(request, "pages/contact_success.html")


def subscription_success(request):
    """
    Display the Subscription Success page after successful signup.
    """
    return render(request, "pages/subscription_success.html")


def under_construction(request):
    """
    Display the Under Construction page.
    """
    return render(request, "pages/under_construction.html")

def custom_404(request, exception):
    """Render the custom 404 error page."""
    return render(request, "404.html", status=404)