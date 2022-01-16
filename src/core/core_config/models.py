from django.db import models

from core.utils.mixins.base import BaseMixin
from ranking.models import Rank
class ConfigApp(BaseMixin):

    class Meta :
        verbose_name = "Configuração"
        verbose_name_plural = "Configurações"

    name = models.CharField(
        verbose_name="Nome do Projeto",
        help_text="Coloque o nome do seu projeto ou empresa.",
        max_length=50,
        blank=True
    )
    short_name = models.CharField(
        verbose_name="Nome Curto",
        help_text="Coloque uma sigla de até 3 caracteres.",
        max_length=3,
        blank=True,
    )
    subtitle = models.CharField(
        verbose_name="Subtítulo",
        help_text="Subtítulo ou descrição utilizada no site.",
        max_length=50, blank=True,
    )
    favicon = models.ImageField(
        verbose_name="Ícone",
        help_text=("Ícone pequeno utilizado na aba dos navegadores "
                   "(Resolução 32x32 px em formato .png)"),
        null=True, blank=True, upload_to="uploads/config/img/"
    )
    default_rank = models.ForeignKey(Rank, verbose_name="Ranking Inicial",
                                    help_text="O cliente recebe esse ranking no cadastro (Importante existir)",
                                    on_delete=models.CASCADE, blank=True, null=True)


    def __str__(self):
        return self.name

    
    def save(self, *args, **kwargs):
        # -- efeito "singleton", apenas uma unica configuracao ativa sempre
        if self.active:
            all_configs = ConfigApp.objects.all()
            for config in all_configs:
                config.active = False
                config.save()
        
        super(ConfigApp, self).save(*args, **kwargs)