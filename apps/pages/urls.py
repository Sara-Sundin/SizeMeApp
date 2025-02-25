from django.urls import path
from .views import index, about

urlpatterns = [
    path('', index, name='index'),  # Home page
    path('about/', about, name='about'),  # About page
]
