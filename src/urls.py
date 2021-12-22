
import debug_toolbar
from django.urls import include, path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('grappelli/', include('grappelli.urls')), # grappelli URLS
    path('grappelli-docs/', include('grappelli.urls_docs')), # grappelli docs URLS
    path('admin/', admin.site.urls), # admin site
    path('__debug__/', include(debug_toolbar.urls)),
    path('products/', include('src.products.routers')),
    path('project_auth/', include('src.project_auth.routers')),
    # path('', include('src.products.routers')),
    path('auth/', include('rest_framework_social_oauth2.urls')),
]


admin.site.site_header = 'Sistema de Gestão'
admin.site.index_title= 'Administração'
admin.site.site_title = 'Seja bem vindo a gestão de produtos e serviços'


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [path("__debug__/", include(debug_toolbar.urls))]