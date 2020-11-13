from django.contrib.auth.decorators import user_passes_test
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from adminapp.forms import ShopUserAdminEditForm, ProductCategoryEditForm, ProductEditForm
from authapp.forms import ShopUserRegisterForm
from authapp.models import ShopUser
from mainapp.models import Product, ProductCategory
from orderapp.models import Order


def get_user(user):
    user = ShopUser.objects.get(pk=user.pk)
    return user


@user_passes_test(lambda u: u.is_superuser)
def user_create(request):
    title = 'пользователи / создание'
    if request.method == "POST":
        user_form = ShopUserRegisterForm(request.POST, request.FILES)
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


class UsersListView(ListView):
    model = ShopUser
    template_name = 'adminapp/users.html'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Пользователи'
        return context_data

    # def get_queryset(self):
    #     qs = super().get_queryset()
    #     return qs.filter(is_active=True)


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


class ProductCategoryCreateView(CreateView):
    model = ProductCategory
    template_name = 'adminapp/category_update.html'
    success_url = reverse_lazy('admin:categories')
    # fields = '__all__'
    form_class = ProductCategoryEditForm


@user_passes_test(lambda u: u.is_superuser)
def categories(request):
    title = 'категории'
    categories_list = ProductCategory.objects.all()

    content = {
        'title': title,
        'objects': categories_list
    }
    return render(request, 'adminapp/categories.html', content)


class ProductCategoryUpdateView(UpdateView):
    model = ProductCategory
    template_name = 'adminapp/category_update.html'
    success_url = reverse_lazy('admin:categories')
    form_class = ProductCategoryEditForm


class ProductCategoryDeleteView(DeleteView):
    model = ProductCategory
    template_name = 'adminapp/category_delete.html'
    success_url = reverse_lazy('admin:categories')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())


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


class ProductDetailView(DetailView):
    model = Product
    template_name = 'adminapp/product_read.html'


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


class OrdersListView(ListView):
    model = Order
    template_name = 'adminapp/orders.html'

    def get_queryset(self):
        idx = list(Order.objects.values_list('id', flat=True))

        return super(OrdersListView, self).get_queryset().exclude(status=Order.CANCEL).filter(
            id__in=idx).select_related('user')


def order_status_change(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if order.status == Order.FORMING:
        order.status = Order.SENT_TO_PROCEED
    elif order.status == Order.SENT_TO_PROCEED:
        order.status = order.PROCEEDED
    order.save()
    return HttpResponseRedirect(reverse('adminapp:orders'))


@receiver(pre_save, sender=ProductCategory)
def product_is_active_productcategory_save(sender, instance, **kwargs):
    if instance.pk:
        if instance.is_active:
            instance.product_set.update(is_active=True)
        else:
            instance.product_set.update(is_active=False)
