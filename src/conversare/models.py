from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save
from django.dispatch import receiver

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

from model_utils.fields import UUIDField
from core.utils.mixins.base import BaseMixin


class MessageModel(BaseMixin):
    '''
    This class represents a message
    '''
    id = UUIDField(primary_key=True, version=4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Usuário',
                      related_name='from_user', db_index=True)
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Destino',
                           related_name='to_user', db_index=True)
    body = models.TextField(max_length=5000, verbose_name='Texto')

    '''
    if displayed to the user  it turns to true
    '''
    # displayed = models.BooleanField(default=False) 


    def __str__(self):
        return str(self.id)

    def characters(self):
        return len(self.body)

    def notify_ws_clients(self):
        """
        Inform client there is a new message.
        """
        notification = {
            'type': 'recieve_group_message',
            'message': f'{self.id}'
        }

        channel_layer = get_channel_layer()
        # print(f"user.id {self.user.id}")
        # print(f"user.id {self.recipient.id}")' 

        async_to_sync(channel_layer.group_send)(f"{self.user.id}", notification)        
        async_to_sync(channel_layer.group_send)(f"{self.recipient.id}", notification)


    # Meta
    class Meta:
        
        verbose_name = 'Mensagem'
        verbose_name_plural = 'Mensagens'
        ordering = ('-registration',)


@receiver(pre_save, sender=MessageModel)
def handler(sender, *args, **kwargs):

    instance = kwargs.get('instance')    
    if instance.id :
        instance.body = instance.body.strip()
        instance.notify_ws_clients()