from django.urls import register_converter, path
from . import converters, views


register_converter(converters.NegativeIntConverter, 'negint')

urlpatterns = [
    path('<negint:number>', views.NumberTranslation.as_view(), name='number-translation'),
]
