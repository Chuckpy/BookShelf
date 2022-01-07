from django.contrib import admin
from .models import CoreUser

class CoreUserAdmin(admin.ModelAdmin):

    fieldsets = (
        ("Dados de Cadastro" , {
            'fields': ('username', 'password','email'),
        }),
        ("Dados de Registro", {
            'fields':('first_name', 'last_name',)
        }),
    )
    search_fields = ('first_name', 'username')

admin.site.register(CoreUser, CoreUserAdmin)