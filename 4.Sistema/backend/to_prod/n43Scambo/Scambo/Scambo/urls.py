from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('Scambo.core.urls', namespace='core')),
    path('admin/', admin.site.urls),
    #path('catalog', include('Scambo.catalog.urls', namespace='catalog')),
    #path('chat', include('Scambo.chat.urls', namespace='chat')),
    path('perfil/', include('Scambo.perfil.urls', namespace='perfil')),
    #path('score', include('Scambo.score.urls', namespace='score')),
    #path('transaction', include('Scambo.transaction.urls', namespace='trasaction')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
