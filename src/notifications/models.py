from django.db import models
from core.utils.mixins.base import BaseMixin
from django.conf import settings


NOTIFICATION_STATUS = (
    ('read','Lido'),
    ('unread','Não Lido'),
    ('sended', 'Enviado'),
    ('unsended','Não Enviado !')
)

class Notifications(BaseMixin):
    #TODO retirar possibilidade de variaveis nulas 
    user_sender=models.ForeignKey(settings.AUTH_USER_MODEL,null=True,blank=True,related_name='user_sender',on_delete=models.CASCADE)
    user_receiver=models.ForeignKey(settings.AUTH_USER_MODEL,null=True,blank=True,related_name='user_revoker',on_delete=models.CASCADE)
    status=models.CharField(max_length=264,null=True,blank=True, choices=NOTIFICATION_STATUS, default="unread")
    type_of_notification=models.CharField(max_length=264,null=True,blank=True)

    class Meta:
        verbose_name="Notificação"
        verbose_name_plural="Notificações"        


