from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
import mainapp.views as mainapp

urlpatterns = [
    path('', mainapp.main, name='main'),
    path('contact/', mainapp.contact, name='contact'),
    path('catalog/', include('mainapp.urls', namespace='catalog')),
    path('auth/', include('authapp.urls', namespace='auth')),
    path('basket/', include('basketapp.urls', namespace='basket')),
    path('order/', include('orderapp.urls', namespace='order')),

    # path('admin/', admin.site.urls),

    path('admin/', include('adminapp.urls', namespace='admin')),
    path('', include('social_django.urls', namespace='social'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
