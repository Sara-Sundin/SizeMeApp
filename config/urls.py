"""
URL configuration for the SizeMeApp project.

This file defines the main URL patterns that route incoming requests to the appropriate views.
For more information, visit:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/

Structure:
- Function-based views: Directly maps URLs to functions in `views.py`
- Class-based views: Uses class methods to handle requests
- Includes: Allows URL routing to be modular across multiple apps
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from pages.views import custom_404

urlpatterns = [
    # Admin panel
    path('admin/', admin.site.urls),

    # User authentication (login, logout, signup) handled by Django Allauth
    path("accounts/", include("allauth.urls")),

    # Rich text editor (Django Summernote) for blog posts
    path('summernote/', include('django_summernote.urls')),

    # Homepage and general static pages handled by the 'pages' app
    path('', include('pages.urls')),

    # Blog section, including post listings, details, and comments
    path('blog/', include('blog.urls'), name='blog-urls'),

    # User dashboard where users manage measurements and avatars
    path("dashboard/", include("dashboard.urls")),

    # Newsletter subscription and related features
    path('newsletter/', include('newsletter.urls')),
]

handler404 = "pages.views.custom_404" 

# Serve media files (e.g., images, avatars) in development mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
