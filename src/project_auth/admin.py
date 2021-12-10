from django.contrib import admin
from .models import BaseUser

class BaseUserAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Dados de Registro", {
            'fields':('first_name', 'last_name', 'email', 'bio', 'phone_number', 'image')
        }),
        ("Dados do Endereço", {
            'fields': ("city", "country", "state", "neighborhood", "street")
        }),        
        ("Seleção de Preferências", {
            'fields':('categories',)
        })
    )
    
    list_display = ('username', 'email', 'first_name', 'last_name')
    search_fields =('id', 'first_name', 'last_name', 'email', 'phone_number')


admin.site.register(BaseUser, BaseUserAdmin)