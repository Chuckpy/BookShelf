from django.contrib.admin import ModelAdmin, site
from .models import MessageModel


class MessageModelAdmin(ModelAdmin):
    
    readonly_fields = ('registration',)
    search_fields = ('id', 'body', 'user__username', 'recipient__username')
    list_display = ('id', 'user', 'recipient', 'registration', 'characters','displayed')
    list_display_links = ('id',)
    list_filter = ('user', 'recipient')
    date_hierarchy = 'registration'


site.register(MessageModel, MessageModelAdmin)