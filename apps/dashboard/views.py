from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from django.http import JsonResponse
from django.core.files.base import ContentFile
import base64
import os
import logging
from cloudinary.uploader import upload  # Cloudinary uploader
from apps.accounts.forms import CustomUserUpdateForm

# Setup logger
logger = logging.getLogger(__name__)

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
            logger.error(f"Form errors: {form.errors}")  # Log form validation errors

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
    user = request.user

    try:
        if request.method == "POST":
            avatar_file = request.FILES.get("avatar")  # File upload
            avatar_base64 = request.POST.get("avatar_base64")  # Base64 upload

            if avatar_file:
                logger.info("Received file upload for avatar.")

                if "DYNO" in os.environ:  # Running on Heroku, use Cloudinary
                    cloudinary_response = upload(avatar_file, folder="avatars")

                    # Extract correct Cloudinary URL
                    secure_url = cloudinary_response.get("secure_url")
                    
                    if secure_url:
                        logger.info(f"Cloudinary upload successful: {secure_url}")
                        user.profile_picture = secure_url  # Assign correct URL
                        user.save()
                        return JsonResponse({"success": True, "avatar_url": secure_url})
                    else:
                        logger.error("Cloudinary upload failed, no secure_url in response")
                        return JsonResponse({"success": False, "error": "Cloudinary upload failed"})

                else:  # Running locally, save to media directory
                    user.profile_picture.save(f"avatars/{user.id}.png", avatar_file)
                    user.save()
                    return JsonResponse({"success": True, "avatar_url": user.profile_picture.url})

            elif avatar_base64:
                logger.info("Received Base64 avatar upload.")

                # Decode Base64 image
                format, img_str = avatar_base64.split(";base64,")
                ext = format.split("/")[-1]  # Get file extension
                decoded_img = base64.b64decode(img_str)

                if "DYNO" in os.environ:  # Upload to Cloudinary
                    cloudinary_response = upload(decoded_img, folder="avatars")

                    # Extract correct Cloudinary URL
                    secure_url = cloudinary_response.get("secure_url")
                    
                    if secure_url:
                        logger.info(f"Cloudinary Base64 upload successful: {secure_url}")
                        user.profile_picture = secure_url  # Assign correct URL
                        user.save()
                        return JsonResponse({"success": True, "avatar_url": secure_url})
                    else:
                        logger.error("Cloudinary Base64 upload failed, no secure_url in response")
                        return JsonResponse({"success": False, "error": "Cloudinary upload failed"})

                else:  # Save locally
                    user.profile_picture.save(f"avatars/{user.id}.{ext}", ContentFile(decoded_img))
                    user.save()
                    return JsonResponse({"success": True, "avatar_url": user.profile_picture.url})

            else:
                return JsonResponse({"success": False, "error": "No avatar provided"})

    except Exception as e:
        logger.error(f"Error saving avatar: {str(e)}", exc_info=True)
        return JsonResponse({"success": False, "error": str(e)})

    return JsonResponse({"success": False, "error": "Invalid request"})
