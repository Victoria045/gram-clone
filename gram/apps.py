from django.apps import AppConfig


class GramConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'gram'

    # def ready(self):
    #     import users.signals