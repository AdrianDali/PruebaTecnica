from django.apps import AppConfig


class AutosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'autos'

class MarcaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'marcas'
