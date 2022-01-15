from django.db import models
from django.core.files import File
from django.core.validators  import MaxValueValidator, MinValueValidator
from core.utils.mixins.address import AddressMixin
from core.utils.mixins.base import BaseMixin
from core.core_auth.models import CoreUser

from io import BytesIO
from PIL import Image, ImageOps




def upload_perfil_user(instance, filename):
    return f"profile_photos/{instance.username}/{filename}"


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


DEFAULT_RANK_ID=1

class Client(CoreUser, AddressMixin):

    image = models.ImageField(verbose_name="Imagem de Perfil", default="default_profile.jpeg", upload_to=upload_perfil_user)
    phone_number = models.CharField("Número de telefone",max_length=20, null=True, blank=True)
    bio = models.TextField(null=True, blank=True, max_length=2000)
    categories = models.ManyToManyField('products.Category',blank=True, verbose_name="Categorias Preferidas")
    rank = models.ForeignKey(Rank, related_name="rank_of", on_delete=models.CASCADE, default=DEFAULT_RANK_ID)
    experience = models.IntegerField(default=0, blank=False,
                                    validators=[
                                    MaxValueValidator(9999999999999999, message="Você extrapolou o limite positivamente"),
                                    MinValueValidator(limit_value=-10000, message="Você extrapolou o limite negativamente")])

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'


    def __str__(self):
        return f"{self.id}-{self.username}"


    def save(self, *args, **kwargs):

        if self.image.name != 'default_profile.jpeg' :

            try :
                im = Image.open(self.image)
                im = im.convert('RGB')
                im = ImageOps.exif_transpose(im)      
                im_io = BytesIO() 
                im.save(im_io, 'JPEG', quality=15)
                self.image = File(im_io, f'{self.username}_profile_picture')

            except Exception as e :
                print(e)        
            
        # TODO change of rank based in the experience

        super().save(*args, **kwargs)


