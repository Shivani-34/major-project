# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-09 19:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0002_propertydetails_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='propertydetails',
            name='cost',
            field=models.CharField(default='0', max_length=400),
        ),
    ]
