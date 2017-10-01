# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class ParkingCustomers(models.Model):

    user = models.CharField(max_length=100, null=True, blank=True)
    wallet_address = models.CharField(max_length=100, null=True, blank=True)
    car_number = models.CharField(max_length=20, null=True, blank=True)
    social_security_number = models.CharField(max_length=100, null=True, blank=True)

    def __unicode__(self):

        return self.user

class TokenInfo(models.Model):

    token_name = models.CharField(max_length=100, null=True, blank=True)
    token_address = models.CharField(max_length=100, null=True, blank=True)
    wallet_address = models.CharField(max_length=100, null=True, blank=True)

    def __unicode__(self):

        return self.token_name