from django.apps import AppConfig


class DashboardConfig(AppConfig):
    """
    Configuration class for the Dashboard app.

    This class registers the 'dashboard' application within Django
    and defines the default auto field type.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dashboard'
