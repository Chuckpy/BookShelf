from django.db import models
from django.core.files import File
from django.core.validators  import MaxValueValidator, MinValueValidator
from core.utils.mixins.address import AddressMixin
from core.core_auth.models import CoreUser
from core.utils.config import get_config
from model_utils.fields import UUIDField

from io import BytesIO
from PIL import Image, ImageOps

from ranking.models import Rank


def upload_perfil_user(instance, filename):
    return f"profile_photos/{instance.username}/{filename}"

DEFAULT_RANK=None
level_rank=None

class Client(CoreUser, AddressMixin):

    uuid = UUIDField(primary_key=True, version=4, editable=False)
    image = models.ImageField(verbose_name="Imagem de Perfil", default="default_profile.jpeg", upload_to=upload_perfil_user)
    phone_number = models.CharField("Número de telefone",max_length=20, null=True, blank=True)
    bio = models.TextField(null=True, blank=True, max_length=2000)
    categories = models.ManyToManyField('products.Category',blank=True, verbose_name="Categorias Preferidas")
    rank = models.ForeignKey(Rank, related_name="rank_of", on_delete=models.CASCADE, default=DEFAULT_RANK, blank=True, null=True)
    experience = models.IntegerField(default=0, blank=False,
                                    validators=[
                                    MaxValueValidator(9999999999999999, message="Você extrapolou o limite positivamente"),
                                    MinValueValidator(limit_value=-10000, message="Você extrapolou o limite negativamente")])

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'


    def __str__(self):
        return f"{self.username}"


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

        if self.rank :                
            try:
                '''
                    Ranking rule
                Initial setup required to start the project tuple 
                containing the value between which exp number is the rank of each user
                eg : (
                    ( (1,2), Rank.object.get(id=1) ),
                    ( (2,3), Rank.object.get(id=2) )
                )
                '''
                config = get_config()
                if config :
                    DEFAULT_RANK=config.default_rank.id

                    level_rank = (
                        ( (0,1000), DEFAULT_RANK),
                        # ( (1000,2000) , DEFAULT_RANK+1),
                    )
                
                if level_rank :                    
                    for el in level_rank :
                        if (self.experience >= el[0][0]) and (self.experience < el[0][1]):
                            self.rank = Rank.objects.get(id=el[1])

            except Exception as e :
                print("Initial config required \n "+e)            

        super().save(*args, **kwargs)


