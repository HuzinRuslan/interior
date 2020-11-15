from django.core.management import call_command
from django.test import TestCase, Client

from mainapp.models import ProductCategory, Product


class TestMainappTestCase(TestCase):
    expected_success_code = 200

    def setUp(self):
        # call_command('flush', '--noinput')
        # call_command('loaddata', 'test_db.json')

        self.client = Client()

    def test_mainapp_urls(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, self.expected_success_code)

        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, self.expected_success_code)

        response = self.client.get('/catalog/0/1/')
        self.assertEqual(response.status_code, self.expected_success_code)

        # response = self.client.get('/catalog/2/1/')
        # self.assertEqual(response.status_code, self.expected_success_code)

        for category in ProductCategory.objects.all():
            response = self.client.get(f'/catalog/{category.pk}/1/')
            self.assertEqual(response.status_code, self.expected_success_code)

        for product in Product.objects.all():
            response = self.client.get(f'/catalog/product/{product.pk}/')
            self.assertEqual(response.status_code, self.expected_success_code)

    # def tearDown(self):
    #     call_command('sqlsequencereset', 'mainapp', 'authapp', 'ordersapp','basketapp')