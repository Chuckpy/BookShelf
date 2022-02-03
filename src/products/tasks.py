from products.models import Products, OpenSearch
from celery import shared_task


@shared_task(name='delayed_matching')
def match_maker_delay(like_list, own_pk, instance_pk, match_list):    

    try:
        for el in like_list:
            prod = Products.objects.get(id=el)
            open_search = OpenSearch.objects.get(own_product=prod)
            likes = list(open_search.like_list.values_list('pk', flat=True))    

            if own_pk in likes :
                try :
                    OpenSearch.objects.get(pk=instance_pk).match.add(prod)
                except Exception :
                    pass     

        # Cleaning matching list after adding new item 
        # If match list have a different element to the like_list, remove it
        rest_matchings = match_list
        if like_list:
            for item in like_list:
                if item in rest_matchings:
                    rest_matchings.remove(item)

        if rest_matchings :
            for item in rest_matchings :
                OpenSearch.objects.get(pk=instance_pk).match.remove(Products.objects.get(id=item))        

    except Exception as e :
        print(e)

    return("Done")
    
