class NegativeIntConverter:
    """ From: https://stackoverflow.com/questions/48867977/django-2-url-path-matching-negative-value """

    regex = '-?\d+'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return '%d' % value
