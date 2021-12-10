from django.db import models

class AddressMixin(models.Model):
    class Meta:
        abstract = True
        verbose_name = "Endereço"

    city = models.CharField("Cidade",max_length=80, blank=True)
    country = models.CharField("País",max_length=80, blank=True)
    state = models.CharField("Estado",max_length=80, blank=True)
    neighborhood = models.CharField("Bairro",max_length=80, blank=True)
    street = models.CharField("Rua",max_length=80, blank=True)
