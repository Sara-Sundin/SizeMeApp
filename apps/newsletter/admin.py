from django.contrib import admin
from .models import Newsletter, Subscriber

@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('title', 'sent', 'created_on')
    search_fields = ('title', 'content')
    list_filter = ('sent', 'created_on')

@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscribed_at')
    search_fields = ('email',)
    list_filter = ('subscribed_at',)
