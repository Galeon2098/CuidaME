from django.apps import AppConfig


class OffersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "main.offer"

    def ready(self):
        #NO BORRAR ES NECESARIO PARA QUE FUNCIONE LA SEÑAL
        import main.offer.signals