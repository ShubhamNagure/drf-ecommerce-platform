from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

User = get_user_model()


class APITestCase(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='password')

    def test_create_product(self):
        self.client.login(username='testuser', password='password')
        response = self.client.post('/api/products/',
                         {'name': 'Test Product', 'description': 'Test Description', 'price': '10.99', 'stock': 100})
        self.assertEqual(response.status_code, 201)
