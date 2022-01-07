from django.db import models
from django.contrib.auth.models import AbstractUser


class CoreUser(AbstractUser):

    class Meta:
        app_label = 'core_auth'
        verbose_name='Núcleo de Autenticação'
        verbose_name_plural='Núcleos de Autenticação'

    REQUIRED_FIELDS = []


class CoreStaff(CoreUser):
    class Meta:
        app_label = "core_auth"

    def save(self, *args, **kwargs):
        self.is_staff = True
        super(CoreStaff, self).save()