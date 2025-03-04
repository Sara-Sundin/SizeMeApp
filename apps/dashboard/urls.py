from django.urls import path, include
from .views import user_dashboard

urlpatterns = [
    path("", user_dashboard, name="dashboard"),
    path('accounts/', include('allauth.urls')),
]
