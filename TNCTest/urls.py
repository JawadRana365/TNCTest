"""TNCTest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from accounts import views as accountsView
from currency import views as currencyView
from django.conf.urls import url
from currency import restapi as apiView


urlpatterns = [
    path('admin/', admin.site.urls),
    path("register/", accountsView.register, name="register"),  # <-- added
    path("login/", accountsView.login, name="login"),  # <-- added
    path("home/", currencyView.home, name="home"),  # <-- added
    path("updatefait/", currencyView.updateFait, name="updatefait"),  # <-- added
    path("fates/", currencyView.fates, name="fates"),  # <-- added
    url("calfate/",apiView.CurrencyFatesAPIView.as_view(), name="calfate"), #new
]
