from django.urls import path

from currencyConverter.views import CurrencyList
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('currencyConverter/', CurrencyList.as_view())
]
urlpatterns = format_suffix_patterns(urlpatterns)
