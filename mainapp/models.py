from django.db import models
from random import randint


class ProductCategory(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name='Имя')
    description = models.TextField(blank=True, verbose_name='Описание')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=128, verbose_name='имя')
    image = models.ImageField(upload_to='products_images', blank=True)
    short_desc = models.CharField(max_length=128, blank=True)
    description = models.TextField(blank=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return f'{self.name} {self.category.name}'


randProduct = randint(0, len(Product.objects.all()))
