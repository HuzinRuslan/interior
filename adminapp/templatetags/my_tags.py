from django import template
from django.conf import settings
import re
register = template.Library()


def media_folder_products(string):
    if not string:
        string = 'products_images/default.jpg'

    return f'{settings.MEDIA_URL}{string}'


register.filter('media_folder_products', media_folder_products)


@register.filter(name='media_folder_users')
def media_folder_users(string):
    if not string:
        string = 'users_avatars/default.jpg'

    if bool(re.match('https', str(string))):
        return f'{string}'

    return f'{settings.MEDIA_URL}{string}'
