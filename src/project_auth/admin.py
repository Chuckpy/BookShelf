from django.contrib import admin
from .models import Client

class ClientAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Dados de Cadastro" , {
            'fields': ('username', 'password','email'),
        }),
        ("Dados de Registro", {
            'fields':('first_name', 'last_name',  'bio', 'phone_number', 'image')
        }),
        ("Dados do Endereço", {
            'fields': ("city", "country", "state", "neighborhood", "street")
        }),        
        ("Seleção de Preferências", {
            'fields':('categories',)
        }),
        ("Rank", {
            'fields':('rank', 'experience')
        })
    )
    readonly_fields = [ "rank"] # "experience"
    list_display = ('username', 'email', 'first_name', 'phone_number')
    search_fields =('id', 'first_name', 'last_name', 'email')


class RankAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Principal", {
            'fields': ("name", "image")
        }),
    )
    list_display = ('name', 'registration', 'active')
    

admin.site.register(Client, ClientAdmin)