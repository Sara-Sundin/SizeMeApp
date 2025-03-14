from django.dispatch import receiver
from allauth.account.signals import user_signed_up

@receiver(user_signed_up)
def set_just_signed_up_session(request, user, **kwargs):
    request.session['just_signed_up'] = True  # Set for new users only
