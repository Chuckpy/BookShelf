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
    )

admin.site.register(ConfigApp, ConfigAppAdmin)