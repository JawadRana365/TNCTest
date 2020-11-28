from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from rest_framework import viewsets

class CurrencyFatesAPIView(APIView):
    def get(self,request):
        allFaits=CurrencyFaits.objects.all().values()
        return Response({"Message":"List of Currencies", "Currency Faits":allFaits})

    def post(self,request):
        amount = request.POST.get("amount","")
        recordid = request.POST.get("currency","")
        currentCurrency = Currency.objects.filter(id=recordid).values()
        allFaits=CurrencyFaits.objects.filter(fromcurrency=recordid).values()
        rates = []
        count = 1
        for fait in allFaits:
            rates.append({
                'id' : count,
                'amount' : amount,
                'currentcurrency' : currentCurrency[0]['key'],
                'fromcurrency' : Currency.objects.filter(id=fait['tocurrency_id']).values()[0]['key'],
                'rate' : float(amount) * float(fait['conversionFactor'])
                })
            count += 1

        alltoFaits=CurrencyFaits.objects.filter(tocurrency=recordid).values()
        for fait in alltoFaits:
            rates.append({
                'id' : count,
                'amount' : amount,
                'currentcurrency' : currentCurrency[0]['key'],
                'fromcurrency' : Currency.objects.filter(id=fait['fromcurrency_id']).values()[0]['key'],
                'rate' : float(amount) / float(fait['conversionFactor'])
                })
            count += 1
        return Response({"Message":"Fate Calculated!", 
            "rates": rates})

