from django.apps import AppConfig


class BlogConfig(AppConfig):
    """
    Configuration class for the Blog app.

    This class sets the default auto field type and registers
    the 'blog' application within the Django project.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
