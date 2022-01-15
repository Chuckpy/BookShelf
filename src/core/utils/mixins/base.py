from django.db import models

class BaseMixin(models.Model):
    class Meta:
        abstract = True

    active = models.BooleanField(verbose_name= "Ativo",default=True)
    registration = models.DateTimeField(blank=True, null=True, verbose_name="data de cadastro", auto_now_add=True)
    update = models.DateTimeField(blank=True, null=True, verbose_name="data de atualização", auto_now=True)