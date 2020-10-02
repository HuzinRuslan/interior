from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from basketapp.models import Basket
from mainapp.models import Product, ProductCategory, Contact


def basket(request):
    pass


def basket_add(request, pk):  # pk = product_pk
    product = get_object_or_404(Product, pk=pk)

    basket_item = Basket.objects.filter(product=product, user=request.user).first()

    if not basket_item:
        basket_item = Basket.objects.create(product=product, user=request.user)
    basket_item.quantity += 1
    basket_item.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))  # отправляет пользователя обратно на ту же страницу


def basket_remove(request, pk):  # pk = basket_pk
    pass
