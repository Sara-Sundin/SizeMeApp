from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from apps.accounts.forms import CustomUserUpdateForm

@login_required
def user_dashboard(request):
    user = request.user
    
    # Retrieve & remove `just_signed_up` flag after first page load
    just_signed_up = request.session.pop('just_signed_up', False)

    if request.method == "POST":
        form = CustomUserUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect("dashboard")  # Ensure "dashboard" URL exists
    else:
        form = CustomUserUpdateForm(instance=user)

    context = {
        "form": form,
        "user": user,
        "just_signed_up": just_signed_up,  # This will be `True` only for new signups
        "signup_url": reverse('account_signup'), 
    }

    return render(request, "dashboard/dashboard.html", context)
