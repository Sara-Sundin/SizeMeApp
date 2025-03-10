import logging
import os
import base64
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from cloudinary.uploader import upload
from django.core.files.base import ContentFile

# Setup logger
logger = logging.getLogger(__name__)

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
