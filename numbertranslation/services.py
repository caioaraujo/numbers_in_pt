from rest_framework.exceptions import NotAcceptable


class NumberTranslationService:

    MAX_LIMIT_ERROR = 'Número acima do limite válido'
    ZERO = 'zero'

    UNITS = {
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

    HUNDREDS = {
        '2': 'duzentos',
        '3': 'trezentos',
        '4': 'quatrocentos',
        '5': 'quinhentos',
        '6': 'seiscentos',
        '7': 'setecentos',
        '8': 'oitocentos',
        '9': 'novecentos'
    }

    THOUSANDS = {
        '1': 'mil',
        '2': 'dois mil',
        '3': 'três mil',
        '4': 'quatro mil',
        '5': 'cinco mil',
        '6': 'seis mil',
        '7': 'sete mil',
        '8': 'oito mil',
        '9': 'nove mil'
    }

    def get_number_in_portuguese(self, number, result=""):
        """
        Given a number, returns it extension name in portuguese

        :param number: a valid number between -99999 and 99999
        :param result: the final result as string
        :return: result
        """
        number_as_str = str(number)

        # Check if the first char is a "-" sign
        first_position = number_as_str[0]
        if "-" == first_position:
            # Removes the negative sign from number
            result = "menos"
            return self.get_number_in_portuguese(number=number_as_str[1::], result=result)

        number_len = len(number_as_str)

        if number_len > 1 and self._is_zero_sequence(number_as_str):
            return result.strip()

        if first_position == '0':
            if number_len > 1:
                return self.get_number_in_portuguese(number=number_as_str[1::], result=result)
            if not result or result == '-':
                return self.ZERO

        if number_len > 5:
            raise NotAcceptable(detail=self.MAX_LIMIT_ERROR)

        if number_len == 5:
            first_two_positions = number_as_str[0] + number_as_str[1]
            result = ' '.join([result, self._get_two_digits_number_in_extension(first_two_positions), 'mil'])

            return self.get_number_in_portuguese(number=number_as_str[2::], result=result)

        if number_len == 4:
            result = ' '.join([result, self.THOUSANDS[first_position]])

            if self._is_zero_sequence(number_as_str[1::]):
                return result.strip()
            second_position = number_as_str[1]
            third_position = number_as_str[2]
            fourth_position = number_as_str[3]
            if second_position == '0' or (third_position == '0' and fourth_position == '0'):
                result = ' '.join([result, 'e'])

            return self.get_number_in_portuguese(number=number_as_str[1::], result=result)

        if number_len == 3:
            # Number is in [-999, -100], [100, 999]
            is_following_zeros = self._is_zero_sequence(number_as_str[1::])

            if first_position == '1':
                if is_following_zeros:
                    result = ' '.join([result, 'cem'])
                    return result.strip()
                result = ' '.join([result, 'cento e'])
                return self.get_number_in_portuguese(number=number_as_str[1::], result=result)
            result = ' '.join([result, self.HUNDREDS[first_position]])
            if is_following_zeros:
                return result.strip()
            result = ' '.join([result, 'e'])
            return self.get_number_in_portuguese(number=number_as_str[1::], result=result)

        if number_len == 2:
            # Number is in [-99, -10], [10, 99]
            result = ' '.join([result, self._get_two_digits_number_in_extension(number_as_str)])
            return result.strip()

        if number_len == 1:

            # Number is in [-9, 9]
            result = ' '.join([result, self.UNITS[number_as_str]])

        return result.strip()

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

    def _is_zero_sequence(self, numeric_string):
        """ Returns true if numeric_string is composed by zeros """
        for number in numeric_string:
            if number != '0':
                return False
        return True
