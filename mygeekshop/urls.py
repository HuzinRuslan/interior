from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
import mainapp.views as mainapp

urlpatterns = [
    path('', mainapp.main, name='main'),
    path('contact/', mainapp.contact, name='contact'),
    path('fishnet-chair/', mainapp.chair, name='fishnet-chair'),
    path('catalog/', include('mainapp.urls', namespace='catalog')),


    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
