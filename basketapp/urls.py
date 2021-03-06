from django.conf import settings
from django.contrib import admin
from django.urls import path
import basketapp.views as basketapp

app_name = 'basketapp'

urlpatterns = [
    path('', basketapp.basket, name='basket-index'),
    path('add/<pk>', basketapp.basket_add, name='add'),
    path('remove/<pk>', basketapp.basket_remove, name='remove'),
    path('edit/<int:pk>/<quantity>/', basketapp.edit, name='edit')
]
