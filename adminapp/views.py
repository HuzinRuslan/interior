from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from adminapp.forms import ShopUserAdminEditForm, ProductCategoryEditForm, ProductEditForm
from authapp.models import ShopUser
from mainapp.models import Product, ProductCategory


def get_user(user):
    user = ShopUser.objects.get(pk=user.pk)
    return user


@user_passes_test(lambda u: u.is_superuser)
def user_create(request):
    title = 'пользователи / создание'
    if request.method == "POST":
        user_form = ShopUserAdminEditForm(request.POST, request.FILES)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('admin:users'))
    else:
        user_form = ShopUserAdminEditForm()

    content = {
        'title': title,
        'user': get_user(request.user),
        'update_form': user_form
    }
    return render(request, 'adminapp/user_update.html', content)


@user_passes_test(lambda u: u.is_superuser)
def users(request):
    title = 'пользователи'
    users_list = ShopUser.objects.all()
    content = {
        'title': title,
        'objects': users_list,
        'user': get_user(request.user)
    }
    return render(request, 'adminapp/users.html', content)


@user_passes_test(lambda u: u.is_superuser)
def user_update(request, pk):
    title = 'пользователи / редактирование'
    edit_user = get_object_or_404(ShopUser, pk=pk)
    if request.method == "POST":
        user_form = ShopUserAdminEditForm(request.POST, request.FILES, instance=edit_user)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('admin:user_update', args=[edit_user.pk]))
    else:
        user_form = ShopUserAdminEditForm(instance=edit_user)

    content = {
        'title': title,
        'user': get_user(request.user),
        'update_form': user_form
    }
    return render(request, 'adminapp/user_update.html', content)


@user_passes_test(lambda u: u.is_superuser)
def user_delete(request, pk):
    title = 'пользователи / удаление'
    edit_user = get_object_or_404(ShopUser, pk=pk)
    if request.method == "POST":
        # edit_user.is_active = False
        # edit_user.save()
        edit_user.delete()
        return HttpResponseRedirect(reverse('admin:users'))

    content = {
        'title': title,
        'user': get_user(request.user),
        'user_to_delete': edit_user
    }
    return render(request, 'adminapp/user_delete.html', content)


@user_passes_test(lambda u: u.is_superuser)
def category_create(request):
    title = 'категории / создание'
    if request.method == "POST":
        category_form = ProductCategoryEditForm(request.POST, request.FILES)
        if category_form.is_valid():
            category_form.save()
            return HttpResponseRedirect(reverse('admin:categories'))
    else:
        category_form = ProductCategoryEditForm()

    content = {
        'title': title,
        'user': get_user(request.user),
        'update_form': category_form
    }
    return render(request, 'adminapp/category_update.html', content)


@user_passes_test(lambda u: u.is_superuser)
def categories(request):
    title = 'категории'
    categories_list = ProductCategory.objects.all()

    content = {
        'title': title,
        'objects': categories_list
    }
    return render(request, 'adminapp/categories.html', content)


@user_passes_test(lambda u: u.is_superuser)
def category_update(request, pk):
    title = 'категории / редактирование'
    category_item = get_object_or_404(ProductCategory, pk=pk)
    if request.method == "POST":
        category_form = ProductCategoryEditForm(request.POST, request.FILES, instance=category_item)
        if category_form.is_valid():
            category_form.save()
            return HttpResponseRedirect(reverse('admin:category_update', args=[category_item.pk]))
    else:
        category_form = ProductCategoryEditForm(instance=category_item)

    content = {
        'title': title,
        'user': get_user(request.user),
        'update_form': category_form
    }
    return render(request, 'adminapp/category_update.html', content)


@user_passes_test(lambda u: u.is_superuser)
def category_delete(request, pk):
    title = 'категории / удаление'
    category_item = get_object_or_404(ProductCategory, pk=pk)
    if request.method == "POST":
        category_item.is_active = False
        category_item.save()
        # edit_user.delete()
        return HttpResponseRedirect(reverse('admin:categories'))

    content = {
        'title': title,
        'user': get_user(request.user),
        'category_to_delete': category_item
    }
    return render(request, 'adminapp/category_delete.html', content)


@user_passes_test(lambda u: u.is_superuser)
def product_create(request, pk):
    title = 'продукт / создание'
    if request.method == "POST":
        product_form = ProductEditForm(request.POST, request.FILES)
        if product_form.is_valid():
            product_form.save()
            return HttpResponseRedirect(reverse('admin:products', args=[pk]))
    else:
        product_form = ProductEditForm()

    content = {
        'title': title,
        'user': get_user(request.user),
        'update_form': product_form
    }
    return render(request, 'adminapp/product_update.html', content)


@user_passes_test(lambda u: u.is_superuser)
def products(request, pk):
    title = 'продукты'
    category_item = get_object_or_404(ProductCategory, pk=pk)
    products_list = Product.objects.filter(category=category_item)

    content = {
        'title': title,
        'objects': products_list,
        'category': category_item
    }
    return render(request, 'adminapp/products.html', content)


@user_passes_test(lambda u: u.is_superuser)
def product(request, pk):
    pass


@user_passes_test(lambda u: u.is_superuser)
def product_update(request, pk):
    title = 'продукт / редактирование'
    product_item = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        product_form = ProductEditForm(request.POST, request.FILES, instance=product_item)
        if product_form.is_valid():
            product_form.save()
            return HttpResponseRedirect(reverse('admin:product_update', args=[product_item.pk]))
    else:
        product_form = ProductEditForm(instance=product_item)

    content = {
        'title': title,
        'user': get_user(request.user),
        'update_form': product_form
    }
    return render(request, 'adminapp/category_update.html', content)


@user_passes_test(lambda u: u.is_superuser)
def product_delete(request, pk):
    title = 'продукт / удаление'
    product_item = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        product_item.is_active = False
        product_item.save()
        # product_item.delete()
        return HttpResponseRedirect(reverse('admin:categories'))

    content = {
        'title': title,
        'user': get_user(request.user),
        'product_to_delete': product_item
    }
    return render(request, 'adminapp/product_delete.html', content)
