import requests
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CurrencySerializer


def index(request):
    return render(request, 'converter/index.html', locals())


class CurrencyList(APIView):
    def get(self, request):
        data = self.currency_convert
        results = CurrencySerializer(data, many=True).data
        return Response(results)

    @property
    def currency_convert(self):
        amount = self.request.GET.get('amount')
        from_currency = self.request.GET.get('from')
        to_currency = self.request.GET.get('to')
        result = requests.get(f'https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}')
        amount_from = result.json()['amount']
        from_ = result.json()['base']
        amount_to = result.json()['rates'].get('SEK')
        key_amount = result.json()['rates'].keys()
        date = result.json()['date']
        result = [{'amount_from': amount_from, 'to': list(key_amount)[0], 'from_': from_, 'amount_to': amount_to, 'date': date}]
        return result

