from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from djangoapp.models import ProfileClient


class RegisterClientViewSetTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('register-client')

        self.profile_client = ProfileClient.objects.create(
            name="John Doe",
            tax_id="454.001.710-10",
            loan_value="3000",
        )

        self.profile_client.addresses.create(
            street="123 Main St",
            state="California",
            number="444"
        )

    def test_create_valid_profile(self):
        data = {
          "client": {
            "name": "John Doe",
            "tax_id": "429.343.480-16",
            "loan_value": "3000"
          },
          "address": {
            "street": "123 Main St",
            "state": "California",
            "number": "456"
          }
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['message'],
                         'Usuário cadastrado com sucesso, sua solicitação de crédito está sendo avaliada')

    def test_create_invalid_profile(self):
        data = {
            "client": {
                "name": "John Doe",
                "tax_id": "454.001.710-10",
                "loan_value": "3000"
            },
            "address": {
                "street": "123 Main St",
                "state": "California",
                "number": "456"
            }
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['message'],  "Não foi possivel fazer o cadatro, verifique os dados preechidos")
