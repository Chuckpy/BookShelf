
from django.db import models

class BaseMixin(models.Model):
    class Meta:
        abstract = True

    active = models.BooleanField(default=True)
    registration = models.DateTimeField(blank=True, null=True, verbose_name="data de cadastro no Sistema", auto_now_add=True)
    update = models.DateTimeField(blank=True, null=True, verbose_name="data de atualização no Sistema", auto_now=True)
