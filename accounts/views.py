from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm
from accounts.models import User
from accounts.serializer import UserSerializer
import jwt
from django.contrib import messages

# Create your views here.
def register(response):
    if response.method == "POST":
	    form = RegisterForm(response.POST)
	    if form.is_valid():
	        form.save()
	        serialized_user = UserSerializer(User.objects.latest('id')).data
	        token = jwt.encode({'user': serialized_user}, 'MySecretKey', algorithm='HS256')
	        response.session['login_token'] = token.decode("utf-8")
	        return redirect("home")
	    else:
	    	form = RegisterForm()
	    	messages.error(response, 'Password and Confirm Password does not match')
    else:
	    form = RegisterForm()
    return render(response, "register/register.html", {"form":form})

def login(response):
    if response.method == "POST":
	    form = LoginForm(response.POST)
	    if form.is_valid():
	    	user = User.objects.filter(name=form.cleaned_data.get("name")).filter(password=form.cleaned_data.get("password"))
	    	if user.exists():
	    		serialized_user = UserSerializer(user.get()).data
	    		token = jwt.encode({'user': serialized_user}, 'MySecretKey', algorithm='HS256')
	    		response.session['login_token'] = token.decode("utf-8") 
	    		return redirect("/home")
	    	else:
	    		form = LoginForm()
	    	messages.error(response, 'User Login Mis-Match')
	    else:	
	    	form = LoginForm()
	    	messages.error(response, 'Form Validation Failed')
    else:
	    form = LoginForm()
    return render(response, "register/login.html", {"form":form})
