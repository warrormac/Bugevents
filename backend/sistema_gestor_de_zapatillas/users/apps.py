from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "sistema_gestor_de_zapatillas.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import sistema_gestor_de_zapatillas.users.signals  # noqa F401
        except ImportError:
            pass
