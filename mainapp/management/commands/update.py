from django.conf import settings
from django.core.management.base import BaseCommand

from authapp.models import ShopUser, ShopUserProfile
from mainapp.models import Product, ProductCategory, Contact


class Command(BaseCommand):

    def handle(self, *args, **options):
        users = ShopUser.objects.all()
        for user in users:
            user_profile = ShopUserProfile.objects.create(user=user)
            user_profile.save()
