from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from newsletter.forms import SubscriberForm  # Import the form

def index(request):
    form = SubscriberForm()  # Initialize form

    if request.method == "POST":
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You have successfully subscribed to our newsletter!")
            return redirect('subscription_success')  # Redirect after successful subscription

    return render(request, 'pages/index.html', {'form': form})

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        if name and email and message:
            try:
                send_mail(
                    subject=f"New Contact Form Submission from {name}",
                    message=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}",
                    from_email="noreply@sizemeapp.se",
                    recipient_list=['sara@sizemeapp.se'],  # Your email
                    fail_silently=False,
                )
                return redirect('contact_success')  # Redirect to success page
            except BadHeaderError:
                messages.error(request, "Invalid header found. Please try again.")
            except Exception as e:
                messages.error(request, "An error occurred while sending your message. Please try again later.")

    return render(request, "pages/contact.html")

def contact_success(request):
    """ This function renders the contact success page """
    return render(request, "pages/contact_success.html")  # Ensure this template exists

def subscription_success(request):
    return render(request, 'pages/subscription_success.html')

def under_construction(request):
    return render(request, "pages/under_construction.html")
