from django.apps import AppConfig


class AccountsConfig(AppConfig):
    """
    Configuration class for the 'accounts' Django app.

    Sets the default auto field and ensures that signal handlers
    in accounts.signals are imported when the app is ready.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

    def ready(self):
        # Import signals to connect them when the app is loaded
        import accounts.signals

