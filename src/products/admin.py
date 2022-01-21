from django.contrib import admin
from rangefilter.filters import DateRangeFilter

from .models import (
    Category, 
    SubCategory,
    Products, 
    ProductImages,
    Tag,
    Like,
    Dislike,
    OpenSearch
    )



class OpenSearchAdmin(admin.ModelAdmin):
    readonly_fields = ['own_product', 'active']
    pass


class LikeAdmin(admin.ModelAdmin):
    pass


class DislikeAdmin(admin.ModelAdmin):
    pass



# Imagem do Produto Inline
class ImageInLine(admin.TabularInline):   
    fields = ('image',) 
    model = ProductImages


class TagAdmin(admin.ModelAdmin):
    fields=("name",)
    list_display = ('name','registration')
    list_filter=('registration', 'update')


class ProductsAdmin(admin.ModelAdmin):
    
    fieldsets = (
        ("Principal",{            
            'fields': ('name','short_description')
        }),
        ("Definição",{
            'fields' :('sub_category','tags')
        }),
        ("Sobre", {
            'fields': ('description', 'product_information', 'stock', 'owner','search_bool')
        }),        
    )
    list_display= ('name', 'dono','categoria','sub_category','registration')
    list_filter = (
        ('registration', DateRangeFilter), ('update', DateRangeFilter), 'sub_category', 'sub_category__category'
    )
    search_fields=('name','owner__first_name','owner_username')

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
admin.site.register(Tag, TagAdmin)
admin.site.register(Like, LikeAdmin)
admin.site.register(Dislike, DislikeAdmin)
admin.site.register(OpenSearch, OpenSearchAdmin)