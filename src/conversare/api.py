from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView

from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import SessionAuthentication
from rest_framework import generics
from django.http import JsonResponse
from rest_framework import status


from django.conf import settings

from core.core_auth.models import CoreUser
from .serializers import MessageModelSerializer, UserModelSerializer
from .models import MessageModel
from .tasks import test_chat


class CsrfExemptSessionAuthentication(SessionAuthentication):
    """
    SessionAuthentication scheme used by DRF. DRF's SessionAuthentication uses
    Django's session framework for authentication which requires CSRF to be
    checked. In this case we are going to disable CSRF tokens for the API.
    """

    def enforce_csrf(self, request):
        return


class MessagePagination(PageNumberPagination):
    """
    Limit message prefetch to one page.
    """
    page_size = settings.MESSAGES_TO_LOAD


class MessageModelViewSet(ModelViewSet):
    queryset = MessageModel.objects.all()
    serializer_class = MessageModelSerializer
    allowed_methods = ('GET', 'POST', 'HEAD', 'OPTIONS')
    authentication_classes = (CsrfExemptSessionAuthentication,)
    pagination_class = MessagePagination

    def list(self, request, *args, **kwargs):
        self.queryset = self.queryset.filter(Q(recipient=request.user) |
                                             Q(user=request.user))        
        target = self.request.query_params.get('target', None)
        if target :
            self.queryset = self.queryset.filter(
                Q(recipient=request.user, user__username=target) |
                Q(recipient__username=target, user=request.user))
            # displaying all queryset
            self.queryset.update(displayed=True)
        return super(MessageModelViewSet, self).list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        msg = get_object_or_404(
            self.queryset.filter(Q(recipient=request.user) |
                                 Q(user=request.user),
                                 Q(pk=kwargs['pk'])))
        serializer = self.get_serializer(msg)
        return Response(serializer.data)


class UserModelViewSet(ModelViewSet):
    queryset = CoreUser.objects.all()
    serializer_class = UserModelSerializer
    allowed_methods = ('GET', 'HEAD', 'OPTIONS')
    pagination_class = None  # Get all user

    def list(self, request, *args, **kwargs):
        # Get all users except yourself
        self.queryset = self.queryset.exclude(id=request.user.id)
        # Get all users that have matched
        # still didn't have a match model
        return super(UserModelViewSet, self).list(request, *args, **kwargs)


class ChatView(TemplateView):
    
    template_name="conversare/core/chat.html"


class CeleryTest(generics.GenericAPIView):
    def post(self, request):

        user = request.data.get('user')
        recipient = request.data.get('recipient')
        content = request.data.get('content')

        try :
            test_chat.delay(user, recipient, content)
            return JsonResponse({'success': True, 'message': content}, status=status.HTTP_201_CREATED)
        
        except Exception as e :
            print(e)
        
        return JsonResponse({"success":False}, status=status.HTTP_400_BAD_REQUEST)


