from django.forms import ModelForm
from django import forms
from accounts.models import User
from django.contrib import messages


class RegisterForm(ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	confirmpassword = forms.CharField(widget=forms.PasswordInput)
	conditions = forms.BooleanField(required=True)
	policies = forms.BooleanField(required=True)
	class Meta:
		model = User
		fields = ["name", "password", "confirmpassword", "conditions","policies"]

	def clean(self):
		cleaned_data = super(RegisterForm, self).clean()
		password = cleaned_data.get("password")
		confirmpassword = cleaned_data.get("confirmpassword")
		if password != confirmpassword:
			raise forms.ValidationError("password and confirmpassword does not match")

class LoginForm(ModelForm):
	password = forms.CharField(widget=forms.PasswordInput,required=True)
	name = forms.CharField(required=True)
	class Meta:
		model = User
		fields = ["name", "password"]