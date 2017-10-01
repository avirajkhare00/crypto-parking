"""smart_parking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app1.views import app, check_parking_space, confirm_parking_space, get_account_bal_view, confirm_parking, confirmed_confirmed_parking

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^check_parking_space/$', check_parking_space, name='check_parking_space'),
    url(r'^confirm_parking_space/$', confirm_parking_space, name='confirm_parking_space'),
    url(r'^get_account_bal/$', get_account_bal_view, name='get_account_bal'),
    url(r'^confirm_parking/$', confirm_parking, name='confirm_parking'),
    url(r'^confirmed_confirmed_parking/$', confirmed_confirmed_parking, name='parking_confirmed'),
    url(r'^$', app, name='main_app_page')
]
