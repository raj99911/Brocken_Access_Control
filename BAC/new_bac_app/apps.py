from django.apps import AppConfig


class NewBacAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'new_bac_app'

    def ready(self):
        print("lala")
        import new_bac_app.signals