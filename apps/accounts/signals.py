from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.contrib.sessions.models import Session

@receiver(user_logged_in)
def set_just_signed_up_session(sender, request, user, **kwargs):
    if not request.session.get('just_signed_up', False):  # Avoid overriding if already set
        request.session['just_signed_up'] = True
