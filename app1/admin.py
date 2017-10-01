# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from app1.models import ParkingCustomers, TokenInfo

# Register your models here.

admin.site.register(ParkingCustomers)
admin.site.register(TokenInfo)