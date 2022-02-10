from products.models import Products, OpenSearch
import uuid
from celery import shared_task


@shared_task(name='delayed_matching')
def match_maker_delay(own_product_id, instance_pk, match_list,like_list):

    try:

        products = Products.objects.filter(id__in=like_list)

        for product in products:
            open_search = OpenSearch.objects.get(own_product=product)
            likes = list(open_search.like_list.values_list('pk', flat=True))
            uuid_own_product_id = uuid.UUID(own_product_id)

            if uuid_own_product_id in likes :
                try :
                    own_open_search = OpenSearch.objects.get(pk=instance_pk)
                    own_open_search.match.add(product)
                    # # insert in the product matcher as well                    
                    open_search.match.add(Products.objects.get(pk=own_product_id))
                    
                except Exception as e  :
                    print(f"Erro ao adicionar {e}")
                    pass     
        
        # Cleaning matching list after adding new item ( Put it here for remaining matches or flaw calls)
        
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

    return "Done"

