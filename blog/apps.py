from django.apps import AppConfig

class YourAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'your_app'

    def ready(self):
        import blog.signals  # Import the signals module to connect signal handlers


class BlogConfig(AppConfig):
    name = 'blog'

