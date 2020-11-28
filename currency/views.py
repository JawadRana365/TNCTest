from django.shortcuts import render,redirect
from .forms import CurrencyForm,CurrencyFaitsForm
from currency.models import Currency,CurrencyFaits
from django.contrib import messages
from currency.tables import CurrencyFaitsTable
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
import json

# Create your views here.
def home(response):
	if response.session.get('login_token') is not None:
		currencyFaitsData = CurrencyFaitsTable()
		if response.method == "POST":
			currentForm = CurrencyForm(response.POST)
			currencyFaitsForm = CurrencyFaitsForm(response.POST)
			if currentForm.is_valid():
				currentForm.save()
				messages.error(response, 'Currency Saved Successfully')
				return render(response, "index.html", {"currentForm":currentForm,"currencyFaitsForm":currencyFaitsForm,"currencyFaitsData":currencyFaitsData})
			else:
				messages.error(response, 'Currency validation error')
			if currencyFaitsForm.is_valid():
				currencyFaitsForm.save()
				messages.error(response, 'Currency Fait Saved Successfully')
				return render(response, "index.html", {"currentForm":currentForm,"currencyFaitsForm":currencyFaitsForm,"currencyFaitsData":currencyFaitsData})
			else:
				messages.error(response, 'Currency Fait validation error')
		else:
			currentForm = CurrencyForm()
			currencyFaitsForm = CurrencyFaitsForm()
		return render(response, "index.html", {"currentForm":currentForm,"currencyFaitsForm":currencyFaitsForm,"currencyFaitsData":currencyFaitsData})
	else:
		return redirect("/login")

def updateFait(response):
	if response.method == "POST":
		recordid = response.POST.get('id', '')
		conversionFactor = response.POST.get('conversionFactor', '')
		CurrencyFaits.objects.filter(id=recordid).update(conversionFactor=conversionFactor)
		return HttpResponse({"status":200,"message":"success"},content_type="application/json")
	else:
		return HttpResponse({"status":400,"message":"failed"},content_type="application/json")

def fates(response):
	if response.session.get('login_token') is not None:
		curencies = Currency.objects.all()
		return render(response, "fates.html",{'currencies':curencies})
	else:
		return redirect("/login")
