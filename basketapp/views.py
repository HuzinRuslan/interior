from django.contrib.auth.decorators import login_required
from django.db.models import F
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse

from basketapp.models import Basket
from mainapp.models import Product, ProductCategory, Contact


@login_required
def basket(request):
    title = 'корзина'
    products_list = Product.objects.all().order_by('?')[:4]
    content = {
        # 'basket': Basket.objects.filter(user=request.user),
        'products': products_list,
        'title': title
    }
    return render(request, 'basketapp/basket.html', content)


@login_required
def basket_add(request, pk):  # pk = product_pk

    if 'login' in request.META.get('HTTP_REFERER'):
        return HttpResponseRedirect(reverse('catalog:product', args=[pk]))

    product = get_object_or_404(Product, pk=pk)
    old_basket_item = Basket.get_product(user=request.user, product=product)

    if old_basket_item:
        # old_basket_item[0].quantity += 1
        old_basket_item[0].quantity = F('quantity') + 1
        old_basket_item[0].save()
    else:
        new_basket_item = Basket(user=request.user, product=product)
        new_basket_item.quantity += 1
        new_basket_item.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))  # отправляет пользователя обратно на ту же страницу


@login_required
def basket_remove(request, pk):  # pk = basket_pk
    basket_item = get_object_or_404(Basket, pk=pk)
    basket_item.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def edit(request, pk, quantity):
    if request.is_ajax():
        quantity = int(quantity)
        new_basket_item = Basket.objects.get(pk=int(pk))
        if quantity > 0:
            new_basket_item.quantity = quantity
            new_basket_item.save()
        else:
            new_basket_item.delete()
        basket_items = Basket.objects.filter(user=request.user)
        content = {
            'basket': basket_items
        }
        result = render_to_string('basketapp/includes/inc_basket_list.html', content)
        return JsonResponse({'result': result})
