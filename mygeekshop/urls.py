"""mygeekshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import mainapp.views as mainapp

urlpatterns = [
    path('', mainapp.main, name='main'),
    path('contact/', mainapp.contact, name='contact'),
    path('catalog/', mainapp.catalog, name='catalog'),
    path('fishnet-chair/', mainapp.chair, name='fishnet-chair'),

    path('catalog/product_all/', mainapp.catalog, name='product_all'),
    path('catalog/product_home/', mainapp.catalog, name='product_home'),
    path('catalog/product_office/', mainapp.catalog, name='product_office'),
    path('catalog/product_furniture/', mainapp.catalog, name='product_furniture'),
    path('catalog/product_modern/', mainapp.catalog, name='product_modern'),
    path('catalog/product_classic/', mainapp.catalog, name='product_classic'),

    path('admin/', admin.site.urls),
]
