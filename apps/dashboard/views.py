from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from apps.accounts.forms import CustomUserUpdateForm  # Ensure correct import

@login_required
def user_dashboard(request):
    user = request.user  # Get logged-in user

    if request.method == "POST":
        form = CustomUserUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect("dashboard")  # Ensure "dashboard" URL exists
    else:
        form = CustomUserUpdateForm(instance=user)

    return render(request, "dashboard/dashboard.html", {"form": form, "user": user})
