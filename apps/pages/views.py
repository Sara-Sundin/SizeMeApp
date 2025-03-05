from django.shortcuts import render, redirect
from apps.newsletter.forms import SubscriberForm  # Import the form

def index(request):
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    return render(request, 'pages/contact.html')

def index(request):
    form = SubscriberForm()  # Ensure form is initialized

    if request.method == "POST":
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subscription_success')  # Redirect after successful subscription

    return render(request, 'pages/index.html', {'form': form})

def subscription_success(request):
    return render(request, 'pages/subscription_success.html')

