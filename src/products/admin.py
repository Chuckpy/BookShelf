from django.contrib import admin

from .models import (
    Category, 
    SubCategory,
    Products, 
    ProductImages,
    )

# Imagem do Produto Inline
class ImageInLine(admin.TabularInline):
    model = ProductImages


class ProductsAdmin(admin.ModelAdmin):

    fieldsets = (
        ("Principal",{
            'fields': ('name','short_description')
        }),
        ("Definição",{
            'fields' :('sub_category',)
        }),
        ("Sobre", {
            'fields': ('description', 'product_information', 'stock', 'owner')
        }),        
    )
    list_display= ('name', 'owner','get_category','sub_category','created')
    list_filter=('created','sub_category')
    search_fields=('id','name','owner')

    inlines = [   
        ImageInLine,
        ]

class ProductImagesAdmin(admin.ModelAdmin):
    list_display= ('product', 'owner')
    search_fields=('id','owner','product')

class CategoryAdmin(admin.ModelAdmin):
    fields = ('name',)
    list_display = ('name', 'slug')
    search_fields = ('name','id')

class SubCategoryAdmin(admin.ModelAdmin):
    fields = ('name','category')
    list_display = ('name','category', 'slug')
    list_filter = ('category',)
    search_fields = ('name','id')

admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Products, ProductsAdmin)
admin.site.register(ProductImages, ProductImagesAdmin)