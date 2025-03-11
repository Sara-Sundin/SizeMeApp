from django.urls import path
from .views import index, about, contact, subscription_success, contact_success, under_construction


urlpatterns = [
    path('', index, name='index'),  # Home page
    path('about/', about, name='about'),  # About page
    path('contact/', contact, name='contact'),  # Contact page
    path('subscription-success/', subscription_success, name='subscription_success'),
    path('contact/success/', contact_success, name='contact_success'),
    path("under-construction/", under_construction, name="under_construction"),
]


