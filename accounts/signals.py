from django.dispatch import receiver
from allauth.account.signals import user_signed_up


@receiver(user_signed_up)
def set_just_signed_up_session(request, user, **kwargs):
    """
    Signal receiver that runs when a new user signs up.

    This function listens for the `user_signed_up` signal from `allauth`
    and sets a session variable `just_signed_up` to `True`.
    Used to trigger onboarding steps.

    Args:
        request (HttpRequest): The request instance during signup.
        user (CustomUser): The newly registered user instance.
        **kwargs: Additional arguments passed by the signal.
    """
    request.session['just_signed_up'] = True  # Flag as newly signed up
