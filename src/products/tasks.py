from products.models import Products, OpenSearch
import uuid
from celery import shared_task


@shared_task(name='delayed_matching')
def match_maker_delay(own_pk, instance_pk, match_list,like_list=None):    

    
    if like_list :

        try:

            products = Products.objects.filter(id__in=like_list)

            for product in products:
                open_search = OpenSearch.objects.get(own_product=product)
                likes = list(open_search.like_list.values_list('pk', flat=True))
                uuid_own_pk = uuid.UUID(own_pk)
                if uuid_own_pk in likes :
                    try :
                        open_search = OpenSearch.objects.get(pk=instance_pk)
                        open_search.match.add(product)
                        from_open_search = OpenSearch.objects.get(own_product=product)
                        from_open_search.match.add(Products.objects.get(pk=instance_pk))
                        
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
                open_search = OpenSearch.objects.get(pk=instance_pk)                
                for item in rest_matchings :
                    open_search.match.remove(Products.objects.get(id=item))        

        except Exception as e :
            print(e)

    # In case that doesn't exist likes, delete the remaining matches
    elif like_list is None :
        for el in match_list :
            OpenSearch.objects.get(pk=instance_pk).match.remove(Products.objects.get(pk=el))


    return "Done"

