from __future__ import absolute_import, unicode_literals
from typing import final

from core.core_auth.models import CoreUser

from celery import shared_task

import random, string

@shared_task(name='create_random_user')
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
            create_random_user.reset()
            print(e)

        finally:
            query = CoreUser.objects.filter(first_name="")
            query.delete()

        i+=1
    
    return f"Celery criou {total} usuário(s)"

    