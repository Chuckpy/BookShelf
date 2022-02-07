from django.db import models
from core.utils.mixins.base import BaseMixin
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.conf import settings
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


NOTIFICATION_STATUS = (
    ('read','Lido'),
    ('unread','Não Lido'),
    ('sended', 'Enviado'),
    ('unsended','Não Enviado !')
)

class Notification(BaseMixin):
    #TODO retirar possibilidade de variaveis nulas 
    user_receiver=models.ForeignKey(settings.AUTH_USER_MODEL,null=True,blank=True,related_name='user_revoker',on_delete=models.CASCADE, verbose_name="Usuário Recebedor")
    status=models.CharField(max_length=264,null=True,blank=True, choices=NOTIFICATION_STATUS, default="unread")
    message=models.TextField(max_length=2000, null=True,blank=True, verbose_name="Mensagem")
    type_of_notification=models.CharField(max_length=264,null=True,blank=True,verbose_name="Tipos de Notificações")


    def __str__(self):
        return(f"{self.user_receiver.username}-{self.id}")


    class Meta:
        verbose_name="Notificação"
        verbose_name_plural="Notificações"

    def notify_ws_client(self):
        '''
        Inform client there is a new notification
        '''
        notification = {
            'type': 'recieve_group_notification',
            'message': f'{self.id}'
        }

        channel_layer = get_channel_layer()

        async_to_sync(channel_layer.group_send)(f"{self.user.id}", notification)        
        async_to_sync(channel_layer.group_send)(f"{self.recipient.id}", notification)



@receiver(pre_save, sender=Notification)
def handler(sender, *args, **kwargs):

    instance = kwargs.get('instance')    
    if instance.id :
        instance.notify_ws_clients()