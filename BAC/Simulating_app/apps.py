from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Simulating_app'

    def ready(self):
        print("lala")
        import Simulating_app.signals
