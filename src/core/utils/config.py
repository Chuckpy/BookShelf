from core.core_config.models import ConfigApp


'''
Retorna ultimo modelo de configuração ou None
'''
def get_config():

    try :

        conf = ConfigApp.objects.filter(active=True).last()

    except Exception :
        
        conf = None
       
    return(conf)