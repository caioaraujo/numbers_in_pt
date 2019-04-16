from rest_framework.response import Response
from rest_framework.views import APIView

from .services import NumberTranslationService


class NumberTranslation(APIView):

    def get(self, request, number):
        """
        Get a number and return its translation in portuguese
        """

        number_in_portuguese = NumberTranslationService().get_number_in_portuguese(number)

        return Response({'extenso': number_in_portuguese})
