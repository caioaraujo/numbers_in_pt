from rest_framework import status
from rest_framework.test import APITestCase


class TestNumberTranslationAPI(APITestCase):

    def test_positive_numbers(self):
        one_hundred_and_one = 101
        three_hundred_and_five = 305
        over_nine_thousand = 9814
        twelve_thousand_five_hundred_and_fourty_two = 12542

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

    def test_invalid_range(self):
        response = self.client.get(path='/111111')
        self.assertEqual(status.HTTP_406_NOT_ACCEPTABLE, response.status_code)
        self.assertEqual('Número acima do limite válido', response.data['detail'])

    def test_invalid_path(self):
        response = self.client.get(path='/AAA')
        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)

        response = self.client.get(path='/-')
        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)
