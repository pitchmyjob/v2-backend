from __future__ import unicode_literals, absolute_import
from django.test import TestCase
from backend.apps.pro.models import Pro
from backend.authentification.models import User
from backend.apps.datas.models import Industry
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token

class ProModelTest(TestCase):

    def create_Pro(self):
        validated_data = {
            'email' : 'tannier.yannis@gmail.com',
            'password' : 'azazazaz',
            'first_name' : 'Yannis',
            'last_name' : 'Tannier',
            'company' : 'Pitch my job',
            'phone' : '0689564512'
        }
        Industry.objects.create(name="Indifferent", id=1)
        return Pro.signup(**validated_data)

    def test_create_Pro(self):

        w = self.create_Pro()
        self.assertTrue(isinstance(w, Pro))
        self.assertTrue(isinstance(w.user_set.first(), User))


class ProApiTest(APITestCase):

    def test_api_create_and_get_pro(self):
        data = {
            'email': 'yannis@gmail.com',
            'password': 'azazazaz',
            'first_name': 'Yannis',
            'last_name': 'Tannier',
            'company': 'Pitch my job',
            'phone': '0689564512'
        }
        url = reverse('pro_signup')
        Industry.objects.create(name="Indifferent", id=1)
        response = self.client.post(url, data, format='json')

        user = User.objects.first()

        token = Token.objects.get(user=user)
        headers = {
            'Authorization': ' Token ' + str(token)
        }
        pro = self.client.get(reverse('pro_pro'), headers=headers)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
