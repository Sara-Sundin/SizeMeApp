from django.urls import path
from .views import index, about, subscription_success 
urlpatterns = [
    path('', index, name='index'),  # Home page
    path('about/', about, name='about'),  # About page
    path('subscription-success/', subscription_success, name='subscription_success'),
]
