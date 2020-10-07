from django.conf import settings
from django.contrib import admin
from django.urls import path
import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.catalog, name='index'),
    path('<int:pk>/', mainapp.catalog, name='category'),
    path('product/<int:pk>/', mainapp.product, name='product'),

]
