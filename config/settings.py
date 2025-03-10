"""
Django settings for config project.
"""

import os
import dj_database_url
from decouple import config
from pathlib import Path
import cloudinary
import cloudinary.uploader
import cloudinary.api

# === BASE DIRECTORY === #
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")

# === SECURITY === #
SECRET_KEY = config("SECRET_KEY")
DEBUG = False
ALLOWED_HOSTS = [".herokuapp.com", "localhost", "127.0.0.1"]

# === INSTALLED APPS === #
INSTALLED_APPS = [
    # Django Core Apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",

    # Third-party Apps
    "cloudinary",
    "cloudinary_storage",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "crispy_forms",
    "crispy_bootstrap5",
    "django_summernote",
    "rest_framework",

    # Local Apps
    "apps.pages",
    "apps.blog",
    "apps.accounts",
    "apps.dashboard",
    "apps.newsletter",
]

# === AUTHENTICATION & USER MANAGEMENT === #
SITE_ID = 1
AUTH_USER_MODEL = "accounts.CustomUser"
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"
ACCOUNT_SIGNUP_REDIRECT_URL = "/dashboard/"
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "optional"
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_FORMS = {"signup": "apps.accounts.forms.CustomSignupForm"}

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",  # Default authentication backend
    "allauth.account.auth_backends.AuthenticationBackend",  # Django-Allauth authentication
]

# === MIDDLEWARE === #
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",
]

# Root URL configuration
ROOT_URLCONF = "config.urls"

# WSGI application
WSGI_APPLICATION = "config.wsgi.application"

# === TEMPLATES === #
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [TEMPLATES_DIR],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# === DATABASE === #
DATABASES = {
    "default": dj_database_url.parse(config("DATABASE_URL"))
}

# === STATIC FILES === #
STATIC_URL = "/static/"
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

# Use different static storage for local & production
if "DYNO" in os.environ:  # Running on Heroku
    STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
else:
    STATICFILES_STORAGE = "django.contrib.staticfiles.storage.StaticFilesStorage"

# === MEDIA FILE STORAGE (Profile Pictures) === #
USE_CLOUDINARY = "DYNO" in os.environ  # Running on Heroku?

if USE_CLOUDINARY:
    CLOUDINARY_STORAGE = {
        "CLOUD_NAME": config("CLOUDINARY_CLOUD_NAME", default=""),
        "API_KEY": config("CLOUDINARY_API_KEY", default=""),
        "API_SECRET": config("CLOUDINARY_API_SECRET", default=""),
    }
    DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"
    MEDIA_URL = f"https://res.cloudinary.com/{config('CLOUDINARY_CLOUD_NAME', default='')}/"
else:
    DEFAULT_FILE_STORAGE = "django.core.files.storage.FileSystemStorage"
    MEDIA_URL = "/media/"
    MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# === EMAIL CONFIGURATION === #
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "mail.inleed.com"
EMAIL_PORT = 465
EMAIL_USE_SSL = True
EMAIL_USE_TLS = False
EMAIL_HOST_USER = config("EMAIL_HOST_USER", default="")
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD", default="")

# === PASSWORD VALIDATION === #
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# === SECURITY SETTINGS === #
CSRF_TRUSTED_ORIGINS = [
    "https://*.codeinstitute-ide.net/",
    "https://*.herokuapp.com",
]
CSRF_USE_SESSIONS = True  # Ensures CSRF tokens match session authentication

# === INTERNATIONALIZATION === #
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# === DEFAULT AUTO FIELD === #
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
