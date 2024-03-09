from django.apps import AppConfig


class ChatConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main.chat'

    # si se borra este import, no funcioa    
    def ready(self):
        import main.chat.signals
