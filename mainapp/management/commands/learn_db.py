from django.conf import settings
from django.core.management.base import BaseCommand
from django.db.models import Q

from authapp.models import ShopUser, ShopUserProfile
from mainapp.models import Product, ProductCategory, Contact


class Command(BaseCommand):
    def handle(self, *args, **options):
        test_products = Product.objects.filter(Q(category__pk=1) | Q(category__pk=2))
        print(test_products)
