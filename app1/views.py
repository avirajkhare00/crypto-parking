# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from app1.core.get_account_ballence import get_account_bal

# Create your views here.

def app(request):

    return render(request, 'app.html')

def check_parking_space(request):

    return render(request, 'check_parking_space.html')

def get_account_bal_view(request):

    account_bal = get_account_bal()

    return render(request, 'get_account_bal.html', {
        'account_bal' : account_bal
    })

def confirm_parking(request):

    return render(request, 'confirmed_parking.html')

def confirmed_confirmed_parking(request):

    return render(request, 'confirmed_confirmed_parking.html')

def confirm_parking_space(request):

    location_id = request.GET['location_id']

    if location_id == '1':

        return render(request, 'confirm_parking.html', {
            'location_name' : 'Tata Starbucks',
            'parking_charges' : '22'
        })

    if location_id == '2':

        return render(request, 'confirm_parking.html', {
            'location_name': 'Kormangala Social',
            'parking_charges': '40'
        })

    if location_id == '3':

        return render(request, 'confirm_parking.html', {
            'location_name': 'Truffles',
            'parking_charges': '80'
        })
