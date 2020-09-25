from django.shortcuts import render

from mainapp.models import Product, ProductCategory


def main(request):
    products_list = Product.objects.all().order_by('?')[:4]
    trending_list = Product.objects.all().order_by('?')[:9]
    content = {
        'title': 'главная',
        'products': products_list,
        'trendingCatalog': trending_list
    }
    return render(request, 'mainapp/index.html', content)


def contact(request):
    content = {
        'title': 'контакты',
    }
    return render(request, 'mainapp/contacts.html', content)


def catalog(request, catalog_pk=None):
    links_menu = ProductCategory.objects.all()
    products = Product.objects.all()
    generalProducts = Product.objects.all()[:12]
    content = {
        'title': 'каталог',
        'list_names': links_menu,
        'catalog_products': products
    }
    return render(request, 'mainapp/catalog.html', content)


def chair(request):
    links_menu = ProductCategory.objects.all()
    content = {
        'title': 'каталог',
        'list_names': links_menu,
    }
    return render(request, 'mainapp/fishnet-chair.html', content)
