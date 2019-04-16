from django.urls import path
from . import views

urlpatterns = [
    path('<int:number>', views.NumberTranslation.as_view(), name='number-translation'),
]
