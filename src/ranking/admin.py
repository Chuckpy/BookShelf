from django.contrib import admin
from .models import Rank

class RankAdmin(admin.ModelAdmin):
    list_display = ('name', 'registration')


admin.site.register(Rank, RankAdmin)