from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from django.http import JsonResponse
from django.core.files.base import ContentFile
import base64
import os
from cloudinary.uploader import upload  # Cloudinary uploader
from apps.accounts.forms import CustomUserUpdateForm

@login_required
def user_dashboard(request):
    """Handles user profile updates."""
    user = request.user
    just_signed_up = request.session.pop("just_signed_up", False)  # Retrieve flag

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
        "just_signed_up": just_signed_up,  # This is `True` only for new signups
        "signup_url": reverse("account_signup"),
    }

    return render(request, "dashboard/dashboard.html", context)


@login_required
def save_avatar(request):
    """Handles avatar uploads for both local and Cloudinary storage."""
    if request.method == "POST" and request.FILES.get("avatar"):
        user = request.user
        avatar_file = request.FILES["avatar"]

        if "DYNO" in os.environ:  # Running on Heroku, use Cloudinary
            cloudinary_response = upload(avatar_file, folder="avatars")

            if "secure_url" in cloudinary_response:
                user.profile_picture = cloudinary_response["secure_url"]
                user.save()
                return JsonResponse({"success": True, "avatar_url": user.profile_picture})

        else:  # Running locally, save to media directory
            user.profile_picture.save(f"avatars/{user.id}.png", avatar_file)
            user.save()
            return JsonResponse({"success": True, "avatar_url": user.profile_picture.url})

    return JsonResponse({"success": False, "error": "Invalid request"})
