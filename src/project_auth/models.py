
from django.db import models
from django.contrib.auth.models import User
from django.core.files import File
from core.utils.mixins.base import BaseMixin
from core.utils.mixins.address import AddressMixin

from io import BytesIO
from PIL import Image, ImageOps


def upload_perfil_user(instance, filename):
    return f"profile_photos/{instance.username}/{filename}"

class BaseUser(User, BaseMixin, AddressMixin):

    image = models.ImageField(verbose_name="Imagem de Perfil", default="default_profile.jpg", upload_to=upload_perfil_user)
    phone_number = models.CharField("Número de telefone",max_length=20, null=True, blank=True)
    bio = models.TextField(null=True, blank=True, max_length=2000)
    categories = models.ManyToManyField('products.Category',blank=True, verbose_name="Categorias Preferidas")


    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'


    def __str__(self):
        return f"{self.id}-{self.username}"


    def save(self, *args, **kwargs):

        if self.image.name != 'default_profile.jpg' :

            try :
                im = Image.open(self.image)
                im = im.convert('RGB')
                im = ImageOps.exif_transpose(im)      
                im_io = BytesIO() 
                im.save(im_io, 'JPEG', quality=15)
                self.image = File(im_io, f'{self.username}_profile_picture')

            except Exception as e :
                print(e)
      
        super().save(*args, **kwargs)
