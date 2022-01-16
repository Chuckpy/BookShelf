from django.db import models
from core.utils.mixins.base import BaseMixin


def upload_rank_images(instance,filename):
    return f"rank_images/{filename}"


class Rank(BaseMixin):

    name = models.CharField(max_length=100)
    image = models.ImageField(verbose_name="Imagem do Rank", upload_to=upload_rank_images,
    help_text="É importante que a imagem seja em PNG")

    class Meta:
        verbose_name = 'Rank'
        verbose_name_plural = 'Ranks'

    def __str__(self):
        return f"{self.name}"
