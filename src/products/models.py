from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.core.files import File
from rest_framework.reverse import reverse
from model_utils.fields import UUIDField
from io import BytesIO
from PIL import Image, ImageOps

from core.utils.mixins.base import BaseMixin

from autoslug import AutoSlugField
from project_auth.models import Client



class Category(BaseMixin):

    id = UUIDField(primary_key=True, version=4, editable=False)
    name = models.CharField(max_length=100)
    slug = AutoSlugField(unique=True, always_update=False, populate_from ='name')    

    class Meta :         
        ordering = ("name",)
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.name


class SubCategory(BaseMixin):
    
    id = UUIDField(primary_key=True, version=4, editable=False)
    category = models.ForeignKey(Category, verbose_name="Categoria-Raiz", on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = AutoSlugField(unique=True, always_update=False, populate_from ='name')    

    class Meta :         
        ordering = ("name",)
        verbose_name = "Sub-Categoria"
        verbose_name_plural = "Sub-Categorias"

    def __str__(self):
        return self.name


class Tag(BaseMixin):

    id = UUIDField(primary_key=True, version=4, editable=False)
    name = models.CharField(verbose_name="Nome",max_length=150)
    slug = AutoSlugField(unique=True, always_update=False, populate_from ='name')
    class Meta :
        verbose_name = "Tag"
        verbose_name_plural = "Tag's"

    def __str__(self):
        return f"#{self.name}"


class Products(BaseMixin): 
    
    id = UUIDField(primary_key=True, version=4, editable=False)
    name = models.CharField("Nome",max_length=130)
    slug = AutoSlugField(unique=True, always_update=False, populate_from ='name')
    tags = models.ManyToManyField(Tag, blank=True)
    description = models.TextField(
            "Descrição",
            help_text="Fale brevemente sobre o produto e suas caracteristicas mais importantes",
            max_length=1000,blank=True)
    short_description = models.CharField(
        "Descrição Curta",
          max_length=200, blank=True)
    product_information = models.TextField(
        "Informação do Produto",
            help_text="Descreva como esta o estado do produto",
            max_length=1000,blank=True )
    stock = models.PositiveIntegerField("Quantidade em estoque", default=1)
    available = models.BooleanField("Disponível",default=True)    
    sub_category = models.ForeignKey(SubCategory, verbose_name="Sub-Categoria", on_delete=models.CASCADE, default=None)
    owner = models.ForeignKey(Client, verbose_name="Dono", on_delete=models.CASCADE, default=None) 
    search_bool = models.BooleanField(verbose_name="Procurando", 
                                    help_text="Caso o booleano estiver ativo esse produto pode entrar na lista de troca de outros, o padrão é ativo",
                                    default=True)

    class Meta: 
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"

    def __str__(self):
        return self.name

    def categoria(self):        
        return self.sub_category.category

    def dono(self):
        return self.owner.username

    def get_images(self):
        return ProductImages.objects.filter(product=self.id)

    def get_absolute_url(self):
        return reverse("products-detail-detail", kwargs={"slug":self.slug})



class Like(BaseMixin):

    id = UUIDField(primary_key=True, version=4, editable=False)
    lista = models.ManyToManyField(Products, blank=True)

    class Meta: 
        verbose_name = "Curtidos"
        verbose_name_plural = "Curtidos"

    def __str__(self):
        return f"Like {self.id}"

class Dislike(BaseMixin):

    id = UUIDField(primary_key=True, version=4, editable=False)
    lista = models.ManyToManyField(Products, blank=True)

    class Meta: 
        verbose_name = "Não Curtidos"
        verbose_name_plural = "Não Curtidos"
    
    def __str__(self):
        return f"Unlike {self.id}"


class OpenSearch(BaseMixin):
    
    own_product = models.OneToOneField(Products, blank=True, null=True, on_delete=models.CASCADE)
    like_list = models.ForeignKey(Like, on_delete=models.CASCADE)
    dislike_list = models.ForeignKey(Dislike, on_delete=models.CASCADE)

    class Meta: 
        verbose_name = "Aberto para Busca"
        verbose_name_plural = "Abertos para Busca"


    def __str__(self):
        return f"Busca|{self.own_product.owner.username}|{self.own_product.name}"


    def save(self, *args, **kwargs):
        # -- efeito "singleton", apenas uma unica configuracao ativa sempre
        if self.active:
            all_configs = OpenSearch.objects.all()
            for config in all_configs:
                config.active = False
                config.save()

        super(OpenSearch, self).save(*args, **kwargs)
    


# String de caminho do arquivo
def upload_product(instance, filename):
    return f"product_images/{instance.product.name}/{filename}"

class ProductImages(BaseMixin):

    id = UUIDField(primary_key=True, version=4, editable=False)
    product = models.ForeignKey(Products, default=None, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField("Imagem",upload_to=upload_product, blank=True)

    class Meta :
        verbose_name = "Imagem do Produto"
        verbose_name_plural = "Imagens do Produto"

    def __str__(self):        
        return f"{self.product.slug}"

    def owner(self):
        return self.product.owner
        
    def save(self, *args, **kwargs):
    
        if self.image.name != 'default_profile.jpg' :

            try :
                im = Image.open(self.image)
                im = im.convert('RGB')
                im = ImageOps.exif_transpose(im)      
                im_io = BytesIO() 
                im.save(im_io, 'JPEG', quality=95)
                self.image = File(im_io, f'{self.product.name}-{self.owner.username}')

            except Exception as e :
                print(e)
      
        super().save(*args, **kwargs)
    


@receiver(pre_save, sender = Category)
def handler(sender, *args, **kwargs):
    lista = ['Teste', 'Test', 'test', 'teste']
    instance = kwargs.get('instance')
    if instance.name in lista :
        raise NameError("Object name can generate redundancy")


@receiver(post_save, sender = Products)
def handler(sender, *args, **kwargs):

    instance = kwargs.get('instance')
    if instance.search_bool  :
        try :
            like_list = Like.objects.create()
            dislike_list = Dislike.objects.create()
            OpenSearch.objects.create(
                own_product=instance,
                like_list=like_list,
                dislike_list=dislike_list)
            print("Produto e OpenSearch Feito com sucesso!")
        except Exception :
            raise Exception("Falha ao criar o modelo de Busca")