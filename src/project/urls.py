import debug_toolbar
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)),
    path('auth/', include('rest_framework_social_oauth2.urls')),    
    path('products/', include('products.routers')),
    path('project_auth/', include('project_auth.routers')),

    path('chat/', include('conversare.routers')),

    path('logout/', auth_views.LogoutView.as_view(), {'next_page': '/'},
         name='logout')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [path("__debug__/", include(debug_toolbar.urls))]