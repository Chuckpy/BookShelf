from django.contrib import admin

from .models import ConfigApp

class ConfigAppAdmin(admin.ModelAdmin):
  
    fieldsets = (
        ("Principal",{
            'fields': ('name','short_name')
        }),
        ("Descrição",{
            'fields' :('favicon','subtitle')
        }),
        ("Rankeamento",{
            'fields':('default_rank',)
        })        
    )
    list_display = ('name', 'short_name', 'registration')

admin.site.register(ConfigApp, ConfigAppAdmin)