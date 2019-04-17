from rest_framework.exceptions import NotAcceptable


class NumberTranslationService:

    MAX_LIMIT_ERROR = 'Número acima do limite válido'

    UNITS = {
        '0': 'zero',
        '1': 'um',
        '2': 'dois',
        '3': 'três',
        '4': 'quatro',
        '5': 'cinco',
        '6': 'seis',
        '7': 'sete',
        '8': 'oito',
        '9': 'nove'
    }

    TEN_TO_NINETEEN = {
        '10': 'dez',
        '11': 'onze',
        '12': 'doze',
        '13': 'treze',
        '14': 'quatorze',
        '15': 'quinze',
        '16': 'dezesseis',
        '17': 'dezessete',
        '18': 'dezoito',
        '19': 'dezenove'
    }

    DOZENS = {
        '2': 'vinte',
        '3': 'trinta',
        '4': 'quarenta',
        '5': 'cinquenta',
        '6': 'sessenta',
        '7': 'setenta',
        '8': 'oitenta',
        '9': 'noventa'
    }

    def get_number_in_portuguese(self, number):
        """
        Given a number, returns it extension name in portuguese

        :param number: a valid number between -99999 and 99999
        :return: string (number in portuguese)
        """

        result = ""

        number_as_str = str(number)

        # Check if the first char is a "-" sign
        first_char = number_as_str[0]
        if "-" == first_char:
            result = "menos"

            # Removes the negative sign from number
            number_as_str = number_as_str[1::]

        number_len = len(number_as_str)

        if number_len == 1:
            # Number is -9 to -1
            result = ' '.join([result, self.UNITS[number_as_str]])
            return result.strip()

        if number_len == 2:
            result = ' '.join([result, self._get_two_digits_number_in_extension(number_as_str)])
            return result.strip()



        if number_len > 5:
            raise NotAcceptable(detail=self.MAX_LIMIT_ERROR)

    def _get_two_digits_number_in_extension(self, numeric_string):
        first_position = numeric_string[0]

        if first_position == '1':
            # Number is 10-19
            return self.TEN_TO_NINETEEN[numeric_string]

        # Number is 20-99
        result = self.DOZENS[first_position]
        second_position = numeric_string[1]
        if second_position == '0':
            # Number has two digitis, ending in zero
            return result
        # Number has two digits, ending in a number 1-9
        return ' e '.join([result, self.UNITS[second_position]])
