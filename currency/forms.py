from django.forms import ModelForm
from django import forms
from currency.models import Currency,CurrencyFaits
from django.contrib import messages


class CurrencyForm(ModelForm):
	class Meta:
		model = Currency
		fields = ["name", "key"]

class CurrencyFaitsForm(ModelForm):
	class Meta:
		model = CurrencyFaits
		fields = ["name","conversionFactor" , "fromcurrency","tocurrency"]