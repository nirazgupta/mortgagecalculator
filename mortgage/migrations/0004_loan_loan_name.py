# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-18 04:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mortgage', '0003_remove_user_mortgage_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan',
            name='loan_name',
            field=models.CharField(default='DEFAULT VALUE', max_length=250),
        ),
    ]
