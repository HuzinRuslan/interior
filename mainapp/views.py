from django.shortcuts import render, get_object_or_404
import random
from authapp.models import ShopUser
from basketapp.models import Basket
from mainapp.models import Product, ProductCategory, Contact


def get_basket(user):
    if user.is_authenticated:
        basket = Basket.objects.filter(user=user)
        return basket
    return []


def get_hot_product():
    product_list = Product.objects.all()
    return random.sample(list(product_list), 1)[0]


def get_same_products(product):
    same_products = Product.objects.filter(category_id=product.category_id).exclude(pk=product.pk)[:3]
    return same_products


def main(request):
    products_list = Product.objects.all().order_by('?')[:4]
    trending_list = Product.objects.all().order_by('?')[:9]
    content = {
        'title': 'главная',
        'products': products_list,
        'trendingCatalog': trending_list,
        'basket': get_basket(request.user)
    }
    return render(request, 'mainapp/index.html', content)


def contact(request):
    contacts = Contact.objects.all()[:3]
    products_list = Product.objects.all().order_by('?')[:4]
    content = {
        'title': 'контакты',
        'contacts': contacts,
        'basket': get_basket(request.user),
        'products': products_list,
    }
    return render(request, 'mainapp/contacts.html', content)


def catalog(request, pk=None):
    links_menu = ProductCategory.objects.all()
    products = Product.objects.all()
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
            'basket': get_basket(request.user),
        }
        return render(request, 'mainapp/catalog.html', content)

    content = {
        'title': 'каталог',
        'list_names': links_menu,
        'catalog_products': products,
        'basket': get_basket(request.user),
    }
    return render(request, 'mainapp/catalog.html', content)


def product(request, pk=None):
    product_item = get_object_or_404(Product, pk=pk)
    title = product_item.name
    links_menu = ProductCategory.objects.all()
    same_products = get_same_products(product_item)
    content = {
        'title': title,
        'list_names': links_menu,
        'product': product_item,
        'same_products': same_products,
        'basket': get_basket(request.user)
    }
    return render(request, 'mainapp/product.html', content)
