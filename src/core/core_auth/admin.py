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
    list_display = ('username', 'first_name', 'email' , 'is_staff')
    search_fields = ('first_name', 'username')

admin.site.register(CoreUser, CoreUserAdmin)