# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-01 09:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_auto_20171001_0721'),
    ]

    operations = [
        migrations.CreateModel(
            name='TokenInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token_name', models.CharField(blank=True, max_length=100, null=True)),
                ('token_address', models.CharField(blank=True, max_length=100, null=True)),
                ('wallet_address', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]