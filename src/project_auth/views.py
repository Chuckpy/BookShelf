from .models import Client
from products.models import Category
from .serializers import ClientSerializer

from django.http import JsonResponse
from django.contrib.auth.hashers import make_password

from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework import generics

from .services import password_check


class Register(generics.GenericAPIView):
    
    def post(self, request):
        
        error = []

        username = request.data.get('username')
        if not username:
            error.append('Usuário necessário')
        else :
            user = Client.objects.filter(username=username)
            if user:
                error.append('Usuário já cadastrado')

        email = request.data.get('email')
        if not email :
            error.append('Email necessário')
        else :
            user_email = Client.objects.filter(email=email)
            if user_email :
                error.append('Email já cadastrado')

        raw_password = request.data.get('password')    
        if not raw_password :        
            error = ['Ao menos uma senha é necessária']        
        if password_check(raw_password, error) :        
            password = make_password(raw_password)

        first_name = request.data.get('first_name')
        if not first_name :
            error.append('Primeiro nome é necessário')

        last_name = request.data.get('last_name')
        if not last_name :
            error.append('Último nome é necessário')        

        categories = request.data.get('categories', None)
        list_cat=[]
        if categories :
            categories = list(map(int, categories.split(',')))  
            list_cat = list(Category.objects.filter(id__in=categories).values_list('id', flat=True))
        
        categories_out = []
        if list_cat :
            for el in list_cat :
                if el in categories :
                    categories_out.append(el)
                    categories.remove(el)

        if categories :
            for categ in categories :
                error.append(f'Categoria {categ} não existe')
        
        image = request.FILES.get('image')
        
        city = request.data.get('city',None)
        state = request.data.get('state',None)
        neighborhood = request.data.get('neighborhood',None)
        street = request.data.get('street',None)
                    
        if not error :

            try:
                user = Client.objects.create(
                username=username,
                password=password,
                email=email,
                first_name=first_name,
                last_name=last_name,
                city=city, 
                state=state, 
                neighborhood=neighborhood,
                street=street)

                if image :                    
                    user.image = image
                    
                if categories_out:
                    for elem in categories_out:
                        user.categories.add(Category.objects.get(id=elem))
                user.save()

                if user :
                    return JsonResponse({"success":True}, status=status.HTTP_201_CREATED)
                
            except Exception as e :

                print(e)
                user = Client.objects.filter(username=username)
                if user :
                    user.delete()
                error.append('Erro desconhecido')

        return JsonResponse({"success":False, 'errors':error}, status=status.HTTP_400_BAD_REQUEST)
