from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.files import File

from core.utils.mixins.base import BaseMixin

from autoslug import AutoSlugField
from project_auth.models import Client

from io import BytesIO
from PIL import Image, ImageOps

class Category(BaseMixin):

    name = models.CharField(max_length=100)
    slug = AutoSlugField(unique=True, always_update=False, populate_from ='name')    

    class Meta :         
        ordering = ("name",)
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.name


class SubCategory(BaseMixin):

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
    name = models.CharField(verbose_name="Nome",max_length=150)
    slug = AutoSlugField(unique=True, always_update=False, populate_from ='name')
    class Meta :
        verbose_name = "Tag"
        verbose_name_plural = "Tag's"

    def __str__(self):
        return f"#{self.name}"


class Products(BaseMixin): 

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
    created = models.DateTimeField("Data criação",auto_now_add=True)
    updated = models.DateTimeField("Atualização",auto_now=True)

    class Meta: 
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"

    def __str__(self):
        return self.name

    def get_category(self):        
        return self.sub_category.category

    def get_images(self):
        return ProductImages.objects.filter(product=self.id)


# String de caminho do arquivo
def upload_product(instance, filename):
    return f"product_images/{instance.product.name}/{filename}"

class ProductImages(BaseMixin):

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