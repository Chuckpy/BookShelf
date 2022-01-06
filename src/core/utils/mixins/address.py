from django.db import models

class AddressMixin(models.Model):
    class Meta:
        abstract = True
        verbose_name = "Endereço"

    city = models.CharField("Cidade",max_length=80, blank=True, null=True)
    country = models.CharField("País",max_length=80, blank=True, null=True)
    state = models.CharField("Estado",max_length=80, blank=True, null=True)
    neighborhood = models.CharField("Bairro",max_length=80, blank=True, null=True)
    street = models.CharField("Rua",max_length=80, blank=True, null=True)