from __future__ import absolute_import, unicode_literals

from core.core_auth.models import CoreUser

from celery import shared_task

import random, string

@shared_task
def create_random_user(total):

    S=25
    for i in range(total):

        user = ''.join(random.choices(string.ascii_letters, k = S))  
        passw = ''.join(random.choices(string.digits + string.digits, k = S)) 
        try :
            usuario = CoreUser.objects.create(username=user,password=passw)
            usuario.save()

            print(f'{i+1} Usuario \"{usuario.username}\" cadastrado com sucesso !')
            
        except Exception as e :
            print(e)

        i+=1
    
    return f"Celery criou {total} de usuários"