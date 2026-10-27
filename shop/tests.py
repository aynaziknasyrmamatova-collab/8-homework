from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from .models import Product, Shop


class ProductCrudTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.shop = Shop.objects.create(name='Market', color='green')
        self.products_url = '/shop/products/'
        self.product = Product.objects.create(
            shop=self.shop,
            name='Tea',
            description='Green tea',
            price='4.50',
        )

    def test_product_crud(self):
        response = self.client.get(self.products_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

        detail_url = f'{self.products_url}{self.product.pk}/'
        response = self.client.get(detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Tea')

        response = self.client.post(
            self.products_url,
            {
                'shop': self.shop.pk,
                'name': 'Coffee',
                'description': 'Ground coffee',
                'price': '8.25',
            },
            format='json',
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        created_product_id = response.data['id']

        created_detail_url = f'{self.products_url}{created_product_id}/'
        response = self.client.put(
            created_detail_url,
            {
                'shop': self.shop.pk,
                'name': 'Coffee beans',
                'description': 'Whole beans',
                'price': '9.00',
            },
            format='json',
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Coffee beans')

        response = self.client.patch(
            created_detail_url,
            {'price': '9.50'},
            format='json',
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['price'], '9.50')

        response = self.client.delete(created_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Product.objects.filter(pk=created_product_id).exists())
