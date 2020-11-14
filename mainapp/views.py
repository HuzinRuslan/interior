from django.core.cache import cache
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
import random

from django.views.decorators.cache import cache_page, never_cache

from authapp.models import ShopUser
from basketapp.models import Basket
from mainapp.models import Product, ProductCategory, Contact
from mygeekshop import settings


def get_links_menu():
    if settings.LOW_CACHE:
        key = 'links_menu'
        links_menu = cache.get(key)
        if links_menu is None:
            links_menu = ProductCategory.objects.filter(is_active=True)
            cache.set(key, links_menu)
        return links_menu
    else:
        return ProductCategory.objects.filter(is_active=True)


def get_category(pk):
    if settings.LOW_CACHE:
        key = f'category_{pk}'
        category = cache.get(key)
        if category is None:
            category = get_object_or_404(ProductCategory, pk=pk)
            cache.set(key, category)
        return category
    else:
        return get_object_or_404(ProductCategory, pk=pk)


def get_hot_product():
    product_list = Product.objects.all()
    return random.sample(list(product_list), 1)[0]


def get_same_products(product):
    same_products = Product.objects.filter(category_id=product.category_id).exclude(pk=product.pk).select_related(
        'category')[:3]
    return same_products


def main(request):
    products_list = Product.objects.all().order_by('?')[:4]
    trending_list = Product.objects.all().order_by('?')[:9]
    content = {
        'title': 'главная',
        'products': products_list,
        'trendingCatalog': trending_list,
    }
    return render(request, 'mainapp/index.html', content)


@cache_page(3600)
def contact(request):
    contacts = Contact.objects.all()[:3]
    products_list = Product.objects.all().order_by('?')[:4]
    content = {
        'title': 'контакты',
        'contacts': contacts,
        'products': products_list,
    }
    return render(request, 'mainapp/contacts.html', content)


@cache_page(3600)
def catalog(request, pk=None, page=1):

    links_menu = get_links_menu()
    # links_menu = ProductCategory.objects.all()

    products = Product.objects.all()
    # basket = sum(list(Basket.objects.filter(user=request.user).values_list('quantity',flat=True)))

    if pk is not None:
        if pk == 0:
            products = Product.objects.all()
            # products = Product.objects.filter(Q(category__pk=1) | Q(category__pk=2))
            category = {
                'pk': 0,
                'name': 'все'
            }
        else:
            category = get_category(pk)
            # category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category_id=pk).order_by('-price')

        paginator = Paginator(products, 3)
        try:
            products_paginator = paginator.page(page)
        except PageNotAnInteger:
            products_paginator = paginator.page(1)
        except EmptyPage:
            products_paginator = paginator.page(paginator.num_pages)

        content = {
            'title': 'каталог',
            'list_names': links_menu,
            'catalog_products': products_paginator,
            'category': category,
        }
        return render(request, 'mainapp/catalog.html', content)

    content = {
        'title': 'каталог',
        'list_names': links_menu,
        'catalog_products': products,
    }
    return render(request, 'mainapp/catalog.html', content)


# @never_cache
def product(request, pk=None):
    product_item = get_object_or_404(Product, pk=pk)
    title = product_item.name

    links_menu = get_links_menu()
    # links_menu = ProductCategory.objects.all()

    same_products = get_same_products(product_item)
    content = {
        'title': title,
        'list_names': links_menu,
        'product': product_item,
        'same_products': same_products,
    }
    return render(request, 'mainapp/product.html', content)
