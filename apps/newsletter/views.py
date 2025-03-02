from django.shortcuts import render, redirect
from .forms import SubscriberForm

def subscribe(request):
    if request.method == "POST":
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subscription_success')  # Change to your success URL
    else:
        form = SubscriberForm()
    return render(request, 'newsletter/index.html', {'form': form})
