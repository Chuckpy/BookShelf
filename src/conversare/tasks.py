from .models import MessageModel
from celery import shared_task
from core.core_auth.models import CoreUser


@shared_task(name="conversare_message")
def test_chat(user, recipient, content):    
    
    try : 
        
        mensagem = MessageModel.objects.create(
            user = CoreUser.objects.get(username = str(user)),
            recipient = CoreUser.objects.get(username = str(recipient)),
            body = content
        )
        mensagem.save()

    except Exception as e :
        print(e)
    
