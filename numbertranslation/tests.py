from rest_framework import status
from rest_framework.test import APITestCase


class TestNumberTranslationAPI(APITestCase):

    def test_positive_numbers(self):
        response = self.client.get(path='/0')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual({'extenso': 'zero'}, response.data)

        response = self.client.get(path='/4')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual({'extenso': 'quatro'}, response.data)

        response = self.client.get(path='/15')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual({'extenso': 'quinze'}, response.data)

        response = self.client.get(path='/20')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual({'extenso': 'vinte'}, response.data)

        response = self.client.get(path='/041')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual({'extenso': 'quarenta e um'}, response.data)

        response = self.client.get(path='/100')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual({'extenso': 'cem'}, response.data)

        response = self.client.get(path='/119')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual({'extenso': 'cento e dezenove'}, response.data)

        response = self.client.get(path='/608')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual({'extenso': 'seiscentos e oito'}, response.data)

        response = self.client.get(path='/900')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual({'extenso': 'novecentos'}, response.data)

        response = self.client.get(path='/1000')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual({'extenso': 'mil'}, response.data)

        response = self.client.get(path='/1080')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual({'extenso': 'mil e oitenta'}, response.data)

        response = self.client.get(path='/3400')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual({'extenso': 'três mil e quatrocentos'}, response.data)

        response = self.client.get(path='/9999')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual({'extenso': 'nove mil e novecentos e noventa e nove'}, response.data)

        response = self.client.get(path='/10000')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual({'extenso': 'dez mil'}, response.data)

        response = self.client.get(path='/20001')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual({'extenso': 'vinte mil e um'}, response.data)

        response = self.client.get(path='/5781')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual({'extenso': 'cinco mil e setecentos e oitenta e um'}, response.data)

    def test_negative_numbers(self):
        response = self.client.get(path='/-8')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual({'extenso': 'menos oito'}, response.data)

        response = self.client.get(path='/-19')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual({'extenso': 'menos dezenove'}, response.data)

        response = self.client.get(path='/-60')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual({'extenso': 'menos sessenta'}, response.data)

        response = self.client.get(path='/-100')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual({'extenso': 'menos cem'}, response.data)

        response = self.client.get(path='/-101')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual({'extenso': 'menos cento e um'}, response.data)

        response = self.client.get(path='/-301')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual({'extenso': 'menos trezentos e um'}, response.data)

        response = self.client.get(path='/-500')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual({'extenso': 'menos quinhentos'}, response.data)

        response = self.client.get(path='/-232')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual({'extenso': 'menos duzentos e trinta e dois'}, response.data)

        response = self.client.get(path='/-3050')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual({'extenso': 'menos três mil e cinquenta'}, response.data)

        response = self.client.get(path='/-8880')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual({'extenso': 'menos oito mil e oitocentos e oitenta'}, response.data)

    def test_invalid_range(self):
        response = self.client.get(path='/111111')
        self.assertEqual(status.HTTP_406_NOT_ACCEPTABLE, response.status_code)
        self.assertEqual('Número fora do limite válido', response.data['detail'])

    def test_invalid_path(self):
        response = self.client.get(path='/dois')
        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)

        response = self.client.get(path='/-')
        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)
