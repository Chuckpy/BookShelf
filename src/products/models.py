from django.db import models

from autoslug import AutoSlugField
from project_auth.models import BaseUser

class Category(models.Model):

    name = models.CharField(max_length=100)
    slug = AutoSlugField(unique=True, always_update=False, populate_from ='name')    

    class Meta :         
        ordering = ("name",)
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.name

    def cat_queryset(self):
        #TODO
        pass
        

class SubCategory(models.Model):

    category = models.ForeignKey(Category, verbose_name="Categoria-Raiz", on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = AutoSlugField(unique=True, always_update=False, populate_from ='name')    

    class Meta :         
        ordering = ("name",)
        verbose_name = "Sub-Categoria"
        verbose_name_plural = "Sub-Categorias"

    def __str__(self):
        return self.name


class Products(models.Model): 

    name = models.CharField("Nome",max_length=130)
    slug = AutoSlugField(unique=True, always_update=False, populate_from ='name')
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
    owner = models.ForeignKey(BaseUser, verbose_name="Dono", on_delete=models.CASCADE, default=None) 
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

class ProductImages(models.Model):

    product = models.ForeignKey(Products, default=None, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField("Imagem",upload_to=upload_product, blank=True)

    class Meta :
        verbose_name = "Imagem do Produto"
        verbose_name_plural = "Imagens do Produto"

    def __str__(self):        
        return f"{self.product.slug}"
    
    def owner(self):
        return self.product.owner
        