from django.shortcuts import render, get_object_or_404

from authapp.models import ShopUser
from basketapp.models import Basket
from mainapp.models import Product, ProductCategory, Contact


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
    contacts = Contact.objects.all()[:3]
    content = {
        'title': 'контакты',
        'contacts': contacts
    }
    return render(request, 'mainapp/contacts.html', content)


def catalog(request, pk=None):
    links_menu = ProductCategory.objects.all()
    products = Product.objects.all()
    basket = Basket.objects.filter(user=request.user)
    # basket = sum(list(Basket.objects.filter(user=request.user).values_list('quantity',flat=True)))
    if pk is not None:
        if pk == "0":
            products = Product.objects.all()
            category = {'name': 'все'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category_id=pk).order_by('-price')

        content = {
            'title': 'каталог',
            'list_names': links_menu,
            'catalog_products': products,
            'category': category,
            'basket': basket,
        }
        return render(request, 'mainapp/catalog.html', content)
    content = {
        'title': 'каталог',
        'list_names': links_menu,
        'catalog_products': products,
        'basket': basket,
    }
    return render(request, 'mainapp/catalog.html', content)


def chair(request):
    links_menu = ProductCategory.objects.all()
    content = {
        'title': 'каталог',
        'list_names': links_menu,
    }
    return render(request, 'mainapp/fishnet-chair.html', content)
