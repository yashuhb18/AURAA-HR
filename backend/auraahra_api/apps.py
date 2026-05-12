from django.apps import AppConfig


class auraahraApiConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "auraahra_api"

    def ready(self):
        """
        Initialize API documentation when the app is ready
        """
        # Import and register API documentation components
        import auraahra_api.schema  # noqa


