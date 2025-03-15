from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from django.http import JsonResponse
from django.core.files.base import ContentFile
import base64
import tempfile
from cloudinary.uploader import upload  # Cloudinary uploader
from accounts.forms import CustomUserUpdateForm

@login_required
def user_dashboard(request):
    """Handles user profile updates."""
    user = request.user
    just_signed_up = request.session.pop("just_signed_up", False)  # Retrieve flag

    if request.method == "POST":
        form = CustomUserUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Measurements updated!", extra_tags="profile")
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

from django.contrib import messages

@login_required
def save_avatar(request):
    """Handles avatar uploads for Cloudinary storage."""
    user = request.user

    # Clear previous messages to prevent them from persisting
    storage = messages.get_messages(request)
    list(storage)  # This will iterate over messages and clear them

    if request.method != "POST":
        return JsonResponse({"success": False, "error": "Invalid request method"})

    avatar_file = request.FILES.get("avatar")
    avatar_base64 = request.POST.get("avatar_base64")

    try:
        if avatar_file:
            cloudinary_response = upload(avatar_file, folder="avatars")
            secure_url = cloudinary_response.get("secure_url")

            if secure_url:
                user.profile_picture = secure_url
                user.save()

                messages.success(request, "Avatar updated!", extra_tags="avatar")
                return JsonResponse({"success": True, "avatar_url": secure_url})
            else:
                return JsonResponse({"success": False, "error": "Cloudinary upload failed"})

        elif avatar_base64:
            if ";base64," not in avatar_base64:
                return JsonResponse({"success": False, "error": "Invalid Base64 format"})

            format, img_str = avatar_base64.split(";base64,")
            ext = format.split("/")[-1]
            decoded_img = base64.b64decode(img_str)

            with tempfile.NamedTemporaryFile(delete=True, suffix=f".{ext}") as temp_file:
                temp_file.write(decoded_img)
                temp_file.flush()

                cloudinary_response = upload(temp_file.name, folder="avatars")
                secure_url = cloudinary_response.get("secure_url")

                if secure_url:
                    user.profile_picture = secure_url
                    user.save()

                    messages.success(request, "Avatar updated!", extra_tags="avatar")
                    return JsonResponse({"success": True, "avatar_url": secure_url})
                else:
                    return JsonResponse({"success": False, "error": "Cloudinary upload failed"})

        else:
            return JsonResponse({"success": False, "error": "No avatar provided"})

    except Exception as e:
        return JsonResponse({"success": False, "error": str(e)})