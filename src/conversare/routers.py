from django.urls import path, include
from django.contrib.auth.decorators import login_required
from rest_framework.routers import DefaultRouter
from .api import MessageModelViewSet, UserModelViewSet, ChatView, CeleryTest

router = DefaultRouter()
router.register(r'message', MessageModelViewSet, basename='message-api')
router.register(r'user', UserModelViewSet, basename='user-api')

urlpatterns = [
    path(r'api/v1/', include(router.urls)),

    path('', login_required(ChatView.as_view()), name='home'),
    path('test', CeleryTest.as_view(), name='teste'), #test api
]