from django.urls import path, include
from .views import user_dashboard
from .views import save_avatar

urlpatterns = [
    path("", user_dashboard, name="dashboard"),
    path('accounts/', include('allauth.urls')),
    path("save-avatar/", save_avatar, name="save_avatar"),
]

