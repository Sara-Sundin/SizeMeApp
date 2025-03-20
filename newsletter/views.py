from django.shortcuts import render, redirect
from .forms import SubscriberForm


def subscribe(request):
    """
    Handle newsletter subscriptions.

    If the request method is POST, validate the form and save
    the subscriber's email. Redirect to a success page upon
    successful submission. Otherwise, display the form.
    """
    if request.method == "POST":
        form = SubscriberForm(request.POST)
    if form.is_valid():
        form.save()
        # Change to your success URL
        return redirect("subscription_success")

    else:
        form = SubscriberForm()

    return render(
        request, "newsletter/index.html", {"form": form}
    )
