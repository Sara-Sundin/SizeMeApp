from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from django.http import JsonResponse
from django.core.files.base import ContentFile
import base64
from cloudinary.uploader import upload  # Import Cloudinary uploader
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

# Updated View to Save Avatar to Cloudinary
@login_required
def save_avatar(request):
    """Handles saving the avatar from the frontend and uploading it to Cloudinary."""
    if request.method == "POST" and request.FILES.get("avatar"):
        user = request.user
        avatar_file = request.FILES["avatar"]

        # Upload the avatar to Cloudinary
        cloudinary_response = upload(avatar_file, folder="avatars")

        if "secure_url" in cloudinary_response:
            # Save the Cloudinary URL to the user's profile
            user.profile_picture = cloudinary_response["secure_url"]
            user.save()

            return JsonResponse({"success": True, "avatar_url": user.profile_picture})

    return JsonResponse({"success": False, "error": "Invalid request"})
