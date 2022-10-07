from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from sistema_gestor_de_zapatillas.utils.validators import alphabetic_validator


class User(AbstractUser):
    full_name = models.CharField(
        max_length=50, validators=[alphabetic_validator], help_text="User's full name."
    )
    is_owner = models.BooleanField(default=False, help_text="Owner User.")

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})
